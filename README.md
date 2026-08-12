# Text Analyzer

A beginner-friendly Python project for analyzing text.

## Features

- Character count
- Word count
- Sentence count
- Longest word
- Word frequency
- Text cleaning
- JSON output
- Save and read analysis results

## Run the Project

Activate the virtual environment and run:

```bash
python app.py

## Example
If user inputs this text "Dono files fix ho gayi aur test bhi kar liya"
Then a json file is returned as an output which looks like this

{
    "character_count": 44,
    "word_count": 10,
    "sentence_count": 0,
    "longest_word": "files",
    "frequecy_count": {
        "dono": 1,
        "files": 1,
        "fix": 1,
        "ho": 1,
        "gayi": 1,
        "aur": 1,
        "test": 1,
        "bhi": 1,
        "kar": 1,
        "liya": 1
    }
}