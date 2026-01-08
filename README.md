# AI Chatbot using Google Gemini

A Python-based AI chatbot that leverages Google's Gemini models for intelligent conversations. It supports both text-based and voice-based interactions.

## Features

*   **Google Gemini Integration**: Powered by the `gemini-2.5-flash` model for fast and accurate responses.
*   **Dual Modes**:
    *   **Text Mode**: Chat via text input in the console.
    *   **Voice Mode**: Speak to the bot using microphone input (uses Google Speech Recognition).
*   **Text-to-Speech**: The bot can speak its responses aloud.
*   **Auto-Logging**: Automatically saves conversation history to daily log files (e.g., `chat-YYYY-MM-DD.log`).

## Prerequisites

*   Python 3.x
*   A Google Gemini API Key

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd "Chatbot ai"
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install google-generativeai SpeechRecognition pyttsx3 pyaudio
    ```

    *Note: `pyaudio` might require additional system tools (like PortAudio) on Linux/Mac.*

## Configuration

1.  Open `chatbot_ai.py`.
2.  Update the `GEMINI_API_KEY` variable with your valid API key:
    ```python
    GEMINI_API_KEY = "YOUR_API_KEY_HERE"
    ```

## Usage

### Quick Start (Windows)
Simply run the provided batch file:
```powershell
.\run_bot.bat
```

### Manual Execution

**Run in Text Mode:**
```bash
python chatbot_ai.py --text
```

**Run in Voice Mode:**
```bash
python chatbot_ai.py --voice
```

**Enable Text-to-Speech:**
Add the `--speak` flag to any command to hear the bot's response:
```bash
python chatbot_ai.py --voice --speak
```

## Commands
During the chat:
*   Type `exit`, `quit`, or `bye` to close the application.
*   Type `history` or `logs` to read the current day's chat logs.
