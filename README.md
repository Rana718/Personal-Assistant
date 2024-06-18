# Tom: Your Personal Assistant

Tom is a personal assistant program developed in Python. It integrates various libraries and APIs to provide functionalities such as web browsing, weather updates, translations, playing music, and more. This project demonstrates the use of Python for creating a voice-controlled assistant with diverse capabilities.

## Features

- **Voice Interaction:** Uses `pyttsx3` for text-to-speech and `speech_recognition` for speech-to-text functionalities.
- **Web Integration:** Opens websites like YouTube and provides weather updates using web browsers and APIs.
- **Weather Updates:** Fetches weather information using the OpenWeatherMap API.
- **Translations:** Translates text and speech to different languages using `googletrans`.
- **Miscellaneous:** Includes functionalities like system control, jokes, email sending, and more.

## Libraries Used

The project uses the following libraries:

- `wolframalpha`
- `pyttsx3`
- `speech_recognition`
- `datetime`
- `wikipedia`
- `webbrowser`
- `os`
- `pyaudio`
- `pyjokes`
- `smtplib`
- `pathlib`
- `textwrap`
- `ctypes`
- `shutil`
- `sys`
- `subprocess`
- `winshell`
- `requests`
- `json`
- `win32com.client`
- `google.generativeai`
- `IPython.display`
- `googletrans`
- `gtts`
- `dotenv`

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/tom-assistant.git
   cd tom-assistant

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Set Up API Keys:**
    `.env` file in the root directory and your API Keys:
    ```plaintext
    GEMINI_KEY=your_google_gemini_api_key
    OPEN_KEY=your_openweathermap_api_key

## Usage
Run the Script
    ```
    python main.py
    ```

Interact with Tom by typing commands. Here are some example commands:
- open youtube
- play music
- what is the time
- weather
- translate text

## Commands
- Web Commands: Open YouTube, play music.
- Weather: Get current weather information.
- Translation: Translate text or speech to various languages.
- Miscellaneous: Lock windows, shutdown system, speech-to-text conversion, jokes, etc.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
