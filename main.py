#!/usr/bin/python3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
import requests
import urllib.parse
import json
import tempfile

# ---- CONFIG ----
GIPHY_API_KEY = os.getenv("Your_Giphy_API")
RESULT_LIMIT = os.getenv("Results_to_Show")
TEMP_DIR = tempfile.gettempdir()
MAPPING_FILE = os.path.join(TEMP_DIR, "alfred_giphy_tempfiles.json")

# ---- CLEANUP OLD TEMP FILES ----
if os.path.exists(MAPPING_FILE):
    try:
        with open(MAPPING_FILE, "r") as f:
            old_mapping = json.load(f)
        for path in old_mapping.values():
            if os.path.exists(path):
                try:
                    os.remove(path)
                except Exception:
                    pass
        os.remove(MAPPING_FILE)
    except Exception:
        pass

query = ' '.join(sys.argv[1:]).strip()

if not query:
    print(json.dumps({"items": [{"title": "Type to search GIFs", "valid": False}]}))
    exit()

# URL encode for API call and for web search
q = urllib.parse.quote(query)
url = (
    f"https://api.giphy.com/v1/gifs/search"
    f"?api_key={GIPHY_API_KEY}&q={q}&limit={RESULT_LIMIT}&bundle=low_bandwidth"
)
resp = requests.get(url)
data = resp.json()

items = []
tempfiles_map = {}

for gif in data.get('data', []):
    title = gif.get('title') or 'GIF'
    gif_media_url = gif['images']['original']['url']

    # Use the fast, static thumbnail
    thumb_url = (
        gif['images'].get('fixed_height_still', {}).get('url') or
        gif['images'].get('fixed_width_still', {}).get('url') or
        gif['images'].get('downsized_still', {}).get('url') or
        gif['images'].get('preview', {}).get('url') or
        gif['images']['original']['url']
    )

    # Download thumbnail to temp file (fast)
    fd, temp_path = tempfile.mkstemp(suffix='.gif')
    os.close(fd)
    try:
        img_data = requests.get(thumb_url, timeout=5).content
        with open(temp_path, 'wb') as f:
            f.write(img_data)
    except Exception:
        temp_path = ""

    if temp_path:
        tempfiles_map[gif_media_url] = temp_path

    items.append({
        "title": title[:40],  # Alfred Grid truncates long titles
        "subtitle": gif_media_url,
        "arg": gif_media_url,  # Enter = GIF as image
        "icon": {
            "type": "image",
            "path": temp_path
        },
        "quicklookurl": gif_media_url,  # <-- Enable spacebar preview in Alfred
        "mods": {
            "cmd": {
                "valid": True,
                "arg": "copylink:" + gif_media_url,
                "subtitle": "Copy GIF link to clipboard"
            }
        },
        "text": {
            "copy": gif_media_url,
            "largetype": title
        }
    })

# ---- Add "Search in Giphy" as the last item ----
search_url = f"https://giphy.com/search/{query}"
default_icon_path = os.path.join(os.path.dirname(__file__), "giphy_icon.png")
if not os.path.exists(default_icon_path):
    default_icon_path = temp_path  # fallback

items.append({
    "title": "Search in Giphy…",
    "subtitle": f"Open all results for '{query}' on Giphy.com",
    "arg": search_url,
    "valid": True,
    "quicklookurl": search_url  # optional
})

if tempfiles_map:
    with open(MAPPING_FILE, "w") as f:
        f.write(json.dumps(tempfiles_map))

if not items:
    items = [{"title": "No GIFs found", "valid": False}]

print(json.dumps({"items": items}))