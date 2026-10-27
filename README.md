# CodeAlpha Language Translation Tool

A Python-based language translation application developed as part of the CodeAlpha AI Internship. The application allows users to translate text between multiple languages using an online translation service.

## Features

- Translate text between multiple languages.
- Select source and target languages.
- Display translated text in a clear interface.
- Copy translated text using the built-in copy control.
- Validate empty input and prevent selecting the same source and target language.
- Handle network errors, timeouts, and unsuccessful translation requests.
- Simple and interactive user interface built with Streamlit.

## Technologies Used

- Python
- Streamlit
- Requests
- MyMemory Translation API

## Project Structure

```text
CodeAlpha_LanguageTranslationTool/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Noor72353/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### 2. Create a virtual environment

```bash
py -3.13 -m venv venv
```

### 3. Activate the environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL that you can open in your browser.

## Translation Service

This application uses the MyMemory Translation API. An internet connection is required, and service availability, language support, and usage limits may vary.

## Internship Task

**CodeAlpha AI Internship — Task 1: Language Translation Tool**

## Author

Noorwali Khan
