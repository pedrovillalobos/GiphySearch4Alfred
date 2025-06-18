import sys
import re
import subprocess
import tempfile
import requests
import os
import json
import webbrowser

def clear_temp_files(gif_url):
    TEMP_DIR = tempfile.gettempdir()
    MAPPING_FILE = os.path.join(TEMP_DIR, "alfred_giphy_tempfiles.json")
    try:
        with open(MAPPING_FILE, "r") as f:
            mapping = json.load(f)
    except Exception:
        mapping = {}
    temp_path = mapping.pop(gif_url, None)
    if temp_path and os.path.exists(temp_path):
        try:
            os.remove(temp_path)
        except Exception:
            pass
    # Update mapping file (remove used entry)
    with open(MAPPING_FILE, "w") as f:
        f.write(json.dumps(mapping))

def main():
    arg = sys.argv[1]

    # 1. Copy GIF URL to clipboard (Cmd+Enter)
    if re.match(r"^copylink:https?://.*\.gif$", arg):
        url = arg.replace("copylink:", "", 1)
        # Copy as text to clipboard
        subprocess.run('pbcopy', input=url.encode(), check=True)
        clear_temp_files(url)
        return

    # 2. Copy image as GIF to clipboard (Enter on GIF)
    if re.match(r"^https?://.*\.gif$", arg):
        gif_url = arg
        # Download the GIF to a temp file
        with tempfile.NamedTemporaryFile(suffix='.gif', delete=False) as tmp:
            r = requests.get(gif_url)
            tmp.write(r.content)
            tmp_path = tmp.name

        # Use AppleScript to put the GIF file on the clipboard
        applescript = f'''
        set the clipboard to (read (POSIX file "{tmp_path}") as GIF picture)
        '''
        subprocess.run(['osascript', '-e', applescript])

        os.remove(tmp_path)
        clear_temp_files(gif_url)
        return

    # 3. Open URL in browser (last menu item)
    if arg.startswith("http"):
        webbrowser.open(arg)
        return

    # Fallback
    print("Unknown argument:", arg)

if __name__ == "__main__":
    main()