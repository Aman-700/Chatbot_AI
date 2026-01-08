import google.generativeai as genai
import sys
import argparse
import datetime
import os
import speech_recognition as sr
import pyttsx3

# =========================
# CONFIG
# =========================
GEMINI_API_KEY = "ENTER Your API"

genai.configure(api_key=GEMINI_API_KEY)

# Initialize speech recognizer
r = sr.Recognizer()

# =========================
# ARGUMENT PARSER
# =========================
def parse_argument():
    parser = argparse.ArgumentParser(
        description="AI Chatbot using Google Gemini",
        epilog="Use --text or --voice"
    )
    parser.add_argument("--text", action="store_true", help="Text based chat")
    parser.add_argument("--voice", action="store_true", help="Voice based chat")
    parser.add_argument("--speak", action="store_true", help="Speak chatbot response")
    return parser.parse_args()

# =========================
# GEMINI CHAT
# =========================
def chat_with_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

# =========================
# TEXT TO SPEECH
# =========================
def speak_text(text: str):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()

# =========================
# VOICE INPUT
# =========================
def voice_search():
    print("🎤 Speak now...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print("Speech service error:", e)
        return ""

# =========================
# LOGGING
# =========================
def todays_date():
    return datetime.date.today().isoformat()

def write_log(time, prompt, status, response):
    log_dir = r"C:\VS Code\Working\Chatbot ai"
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, f"chat-{todays_date()}.log")

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(
            f"[{time}] STATUS: {status}\n"
            f"You: {prompt}\n"
            f"Bot: {response}\n\n"
        )

def read_logs():
    log_path = os.path.join(
        r"C:\VS Code\Working\Chatbot ai",
        f"chat-{todays_date()}.log"
    )

    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("No logs found for today.")

# =========================
# MAIN
# =========================
def main():
    args = parse_argument()

    if not (args.text or args.voice):
        print("❌ Use --text or --voice")
        sys.exit(1)

    while True:
        if args.text:
            user_input = input("You: ")
        else:
            user_input = voice_search()
            print("You:", user_input)

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break

        if user_input.lower() in ["history", "logs"]:
            read_logs()
            continue

        if not user_input.strip():
            continue

        try:
            now = datetime.datetime.now()
            response = chat_with_gemini(user_input)
            print("Chatbot:", response)

            if args.speak:
                speak_text(response)

            write_log(now, user_input, "success", response)

        except Exception as e:
            print("❌ Error:", e)
            write_log(datetime.datetime.now(), user_input, "failed", str(e))

# =========================
if __name__ == "__main__":
    main()

