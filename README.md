# Devil's Advocate Bot - Step by Step Setup

## Step 1: Python Install Check
Terminal-la இது run பண்ணுங்க:
```
python3 --version
```
Python 3.8+ இருந்தா OK. இல்லனா python.org-la இருந்து install பண்ணுங்க.

## Step 2: Project Folder-க்கு போங்க
```
cd devils_advocate_bot
```

## Step 3: Virtual Environment Create பண்ணுங்க (Recommended)
```
python3 -m venv venv
```

Activate பண்ண:
- **Mac/Linux:** `source venv/bin/activate`
- **Windows:** `venv\Scripts\activate`

## Step 4: Libraries Install பண்ணுங்க
```
pip install -r requirements.txt
```

## Step 5: Gemini API Key வாங்குங்க
1. https://aistudio.google.com/apikey போங்க
2. Google account-ல login பண்ணுங்க
3. "Create API Key" button click பண்ணுங்க
4. Key-ஐ copy பண்ணுங்க

## Step 6: .env File Create பண்ணுங்க
`.env.example` file-ஐ `.env` -ஆ rename பண்ணுங்க, அதுக்குள்ள உங்க real API key போடுங்க:
```
GEMINI_API_KEY=AIzaSy...உங்க_actual_key_இங்க
```

⚠️ **முக்கியம்:** `.env` file-ஐ யாருகிட்டயும் share பண்ணாதீங்க, GitHub-லயும் upload பண்ணாதீங்க.

## Step 7: Server Run பண்ணுங்க
```
python3 app.py
```

இது மாதிரி output வரும்:
```
* Running on http://127.0.0.1:5000
```

## Step 8: Browser-ல Open பண்ணுங்க
```
http://127.0.0.1:5000
```

இப்போ chat பண்ண ஆரம்பிக்கலாம்! ஏதாவது opinion type பண்ணுங்க, bot எதிர் side-ல argue பண்ணும்.

---

## Common Errors & Fixes

| Error | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | `pip install -r requirements.txt` திரும்ப run பண்ணுங்க (venv activate ஆகியிருக்கான்னு check பண்ணுங்க) |
| `GEMINI_API_KEY not found` | `.env` file correct-ஆ create ஆகியிருக்கான்னு, key சரியா paste பண்ணிருக்கான்னு check பண்ணுங்க |
| `Address already in use` (port 5000) | Terminal-ல `app.run(debug=True, port=5001)` -ன்னு port மாத்துங்க app.py-ல |
| API key invalid error | Google AI Studio-ல key active-ஆ இருக்கான்னு verify பண்ணுங்க |

## Reset Chat
"Reset Chat" button click பண்ணா, bot memory clear ஆகிடும், fresh-ஆ ஆரம்பிக்கலாம்.
