# stt-linux

Simple script for global speech to text on Linux with Wayland support.

## Usage

To start recording, say start typing. To stop recording, say stop typing. Letters will be entered via a virtual keyboard as if they were typed.

## Setup

1. Create and activate a virtual environment with Python:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install pip dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install wtype:
    The method of installation will depend on your package manager. 
    For apt:
    ```bash
    sudo apt install wtype
    ```
    For pacman:
    ```bash
    sudo pacman -S wtype
    ```
4. Run the script.
    ```
    python3 tts.py
    ``` 
