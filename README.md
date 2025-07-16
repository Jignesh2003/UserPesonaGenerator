# Reddit User Persona Extractor

This is a Python script that uses the Reddit API (via [PRAW](https://praw.readthedocs.io/)) to collect a Reddit user's recent posts and comments and generate a basic **user persona file** based on their activity.

---
## 🚀 Features

- Accepts a Reddit profile URL as input (e.g., `https://www.reddit.com/user/kojied/`)
- Extracts the user's most recent posts and comments
- Saves the output in a structured text file showing sample content
- Basic starting point for further persona analysis

---
## 🧰 Requirements

- Python 3.x
- PRAW (Python Reddit API Wrapper)

Install dependencies:

```bash
pip install praw
```

---
🛠️ Setup

You must have a Reddit account and create an app to get API credentials:
 1.Go to https://www.reddit.com/prefs/apps
 2.Click "Create another app"
 3.Choose script as the app type
 4.Set a name, e.g., RedditPersonaTool
 5.Set redirect URI to http://localhost
 6.Copy the client ID (under the app name) and secret

Update the following section in the script with your credentials:

```bash
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="script:reddit.persona:v1.0 (by u/YOUR_USERNAME)"
)
```
---
📦 How to Use

1. Run the script:

```bash
python app.py
```
2. Enter a Reddit profile URL when prompted:

```bash
Enter Reddit profile URL: https://www.reddit.com/user/kojied/
```

3. The script will create a text file like:

```bash
user_persona_kojied.txt
```

---
📁 Sample Output

```bash
User Persona for Reddit User: kojied
==================================================

Sample Posts:
- Title: My experience with mindfulness
  URL: https://reddit.com/r/selfimprovement/comments/...
  Body: I’ve been practicing mindfulness for...

Sample Comments:
- That’s actually very helpful, thank you...
  URL: https://reddit.com/r/GetDisciplined/comments/...
```
