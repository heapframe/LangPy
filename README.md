# LangPy
*Archived as I've finished secondary schooling and can no longer provide updates to this tool.*

A Python bot that automatically completes [Languagenut](https://www.languagenut.com) homework assignments. Spiritual successor to the original JavaScript-based LangPro (which has been privated), without the browser sandbox constraints like needing a CORS bypass extension.  
Proudly made without AI other than for polishing this README  

## Features

- Logs in with student credentials (interactive prompt or credential file)
- Lists all viewable homework assignments in a table
- Automatically fetches correct answers from the Languagenut API
- Submits perfect scores for vocabulary and exam task types
- Rate-limited submissions with randomised completion times to avoid detection

> **Note:** The code isnt really "polished" (as of right now, ill probably polish it later)

## Requirements

- Python 3.10+
- A Languagenut student account

## Installation

```bash
git clone https://github.com/Alpha-404/LangPy
cd LangPy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

**Interactive login:**
```bash
python main.py
```
You will be prompted for your username and password, with an option to save them to a file for future use.

**With a saved credential file:**
```bash
python main.py <loginfile>
```
The credential file must contain the username on line 1 and the password on line 2.

**Example credential file (`login`):**
```
your_username
your_password
```

Once logged in, a table of available homework assignments is displayed. Enter the ID of the assignment you want to complete and the bot handles the rest.

## How It Works

LangPy communicates directly with the Languagenut REST API (`api.languagenut.com`). For each task in a selected assignment it:

1. Detects the task type (vocab, exam, or grammar)
2. Fetches the correct answers via the appropriate translation endpoint
3. Submits a completed game score with all answers correct

## Known Limitations/Quick Notes

- Grammar tasks are not supported and will be skipped
- Language is hardcoded to German (`de`) from English (`en-GB`), but you can change this in `languagenut.py`
- Line 168 in `main.py` can be changed to tune the timings you want to show up on the languagenut panel (milliseconds)
- When running multiple times on the same homework, you can sometimes get funny scores like 1000%

## Project Structure

```
LangPy/
├── main.py           # Entry point and bot runner
├── languagenut.py    # Languagenut API wrapper
└── requirements.txt  # Python dependencies
```

## One last thing
I'd like to also release this race condition code which adds points, it uses a race condition to avoid the "max points for this activity" thing.  
Just paste it in the browser console to use it while on a task.
```js
let minsTaken = 15
let getIncorrect = 0
let repeat = 10

languagenutControllerObject.gameData.timeDifference = function(date1, date2) {
    return Math.max(((minsTaken * 60) + Math.floor(Math.random() * (120 - -120) ) + 120), 360);
}

getIncorrect = Math.min(languagenutControllerObject.gameData.catalog.length, 0)

languagenutControllerObject.gameData.correctVocabList = [[]];
languagenutControllerObject.gameData.selectedCorrectVocab = [[]];
languagenutControllerObject.gameData.selectedIncorrectVocab = [[]];
languagenutControllerObject.gameData.totalVocabList = [[]];
languagenutControllerObject.gameData.incorrectVocabList = [[]];
for (let i = 0; i < languagenutControllerObject.gameData.catalog.length; i++) {
    if (i <= getIncorrect && getIncorrect != 0) {
        languagenutControllerObject.gameData.incorrectVocabList[0].push(languagenutControllerObject.gameData.catalog[i].contentUid);
        languagenutControllerObject.gameData.incorrectVocabsArr[Number(languagenutControllerObject.gameData.catalog[i].contentUid)] = [[]];
        languagenutControllerObject.gameData.incorrectVocabsArr[Number(languagenutControllerObject.gameData.catalog[i].contentUid)].push(languagenutControllerObject.gameData.catalog[i].interfaceWord);
        languagenutControllerObject.gameData.selectedIncorrectVocab[0].push(languagenutControllerObject.gameData.catalog[i].interfaceWord);
    }else {
        languagenutControllerObject.gameData.correctVocabList[0].push(languagenutControllerObject.gameData.catalog[i].contentUid);
        languagenutControllerObject.gameData.correctVocabsArr[Number(languagenutControllerObject.gameData.catalog[i].contentUid)] = [[]];
        languagenutControllerObject.gameData.correctVocabsArr[Number(languagenutControllerObject.gameData.catalog[i].contentUid)].push(languagenutControllerObject.gameData.catalog[i].interfaceWord);
        languagenutControllerObject.gameData.selectedCorrectVocab[0].push(languagenutControllerObject.gameData.catalog[i].interfaceWord);
        languagenutControllerObject.gameData.totalVocabList[0].push(languagenutControllerObject.gameData.catalog[i].contentUid);
    }
}


Promise.all(
    Array.from({ length: repeat }, () => languagenutControllerObject.gameData.submit())
);

```
