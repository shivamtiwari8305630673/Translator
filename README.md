# Translator App

A Django web application for translating text between languages using Google Translate. Includes speech-to-text input and translation history.

## Features
- Translate text to Hindi, French, German, or English
- Speech-to-text input (Chrome only)
- Stores translation history in the database

## Requirements
- Python 3.12+
- Django
- googletrans==4.0.0-rc1

## Setup
1. Clone the repository or copy the project files.
2. Install dependencies:
   ```cmd
   pip install django googletrans==4.0.0-rc1
   ```
3. Apply migrations:
   ```cmd
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the development server:
   ```cmd
   python manage.py runserver
   ```
5. Open http://127.0.0.1:8000/ in your browser.

## Usage
- Enter text, select a target language, and click "Translate".
- Use the "Speak" button for speech input (supported in Chrome).
- Translated text will appear below the form.

## Troubleshooting
- If you see `Translation failed: no such table: translator_translationhistory`, run migrations as shown above.
- For speech input, use Google Chrome.

## License
This project is for educational purposes.
