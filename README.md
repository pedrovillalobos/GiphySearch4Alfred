# Giphy Search for Alfred

This Alfred workflow lets you instantly **search for GIFs on Giphy** and quickly copy them for use in WhatsApp, Telegram, iMessage, or any app! You can search, preview, and copy GIFs without leaving your keyboard.

## Workaround

At the moment, there are still dependency issues, to overcome those you can follow this in your Terminal:

1. Ensure you have pip installed:
```
# Check your pip version
/usr/bin/python3 -m pip --version
# If you get an error like "no module named pip", run:
/usr/bin/python3 -m ensurepip --upgrade
```

2. Install required modules:
```
/usr/bin/python3 -m pip install --upgrade --user requests urllib3 charset_normalizer
```
You should now be able to run the search without an issue.

---

## ✨ Features

- **Instant GIF Search:** Type `gif {query}` in Alfred to search Giphy.
- **Preview in Alfred:** See GIF previews right in your Alfred results.
- **Copy as Image:** Press `Enter` on any result to copy the GIF as an image (great for WhatsApp, iMessage, etc).
- **Copy as Link:** Press `Cmd+Enter` to copy the GIF URL (great for Telegram and Slack).
- **Quick Search Link:** Always includes a "Search in Giphy" option to open the full results in your browser.
- **Cleans Up Automatically:** Workflow manages temp files so your system stays clean.
- **Privacy:** No analytics or tracking.

---

## 🚀 Setup

1. **Get Your Giphy API Key**

   - Visit [developers.giphy.com](https://developers.giphy.com/) and log in (or sign up).
   - Click **"Create an App"** to generate your personal API key.
   - Copy your API key.

2. **Install the Workflow**

   - Double click the Import the [GiphySearch.alfredworkflow](GiphySearch.alfredworkflow) file into Alfred.

3. **Set Your API Key in Alfred**

   - Open the workflow in Alfred preferences.
   - Click the `Configure Workflow` button at the top left of the workflow editor.
   - **Giphy API Key:** `Your_Giphy_API`
   - **Results to Show:** `Select how many results you want to appear`

---

## 📝 Usage

- **Search GIFs:**  
  Type `gif` followed by your search (e.g. `gif cat dance`).
- **Preview GIFs:**  
  Results show previews for each GIF.
- **Copy as image:**  
  Select a result and hit `Enter` – pastes animated GIF in most messengers (WhatsApp, iMessage, Mail, etc).
- **Copy as link:**  
  Hold `Cmd` and hit `Enter` – copies the Giphy direct link to your clipboard (recommended for Telegram, Slack, Discord, etc).
- **Open in Giphy:**  
  Select "Search in Giphy…" at the end of results to open your search in the browser.

---

## 🛠️ Troubleshooting

- **Nothing is returned?**  
  Double-check your API key is correct.
- **GIF not animating in some apps?**  
  Some apps (like Telegram) require the GIF file as a URL, not an image. Use `Cmd+Enter` for those.
- **Want more results?**  
  Increase the "Results to Show" in the "Workflow configuration".

---

## 🗝️ API Key Security

Your API key is stored _locally_ and used only for your own Giphy searches.  
If needed, you can reset or delete your key at [developers.giphy.com](https://developers.giphy.com/).

---

## 🤝 Credits

- Built by [Pedro Villalobos](https://github.com/pedrovillalobos/)
- Powered by [Giphy API](https://developers.giphy.com/)

---

##IMPORTANT DISCLAIMER

This workflow is not a product of Giphy.com and is not affiliated with, endorsed, or sponsored by Giphy or its parent company in any way.  
It is an independent, unofficial project that uses the public Giphy API for personal, non-commercial use.

---

## 🛡️ License

This workflow is provided as-is with no warranty.
You are responsible for usage in accordance with Giphy's terms.
