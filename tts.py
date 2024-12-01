import subprocess
from RealtimeSTT import AudioToTextRecorder

def process_text(text):
    global recording
    print(f"Detected: {text}")
    if text.lower() == "start typing.":
        recording = True
        print("START")
    elif text.lower() == "stop typing.":
        recording = False
        print("STOP")
    elif recording:
        try:
            subprocess.run(['wtype', text], check=True)
        except Exception as e:
            print(f"Error typing text: {e}")

if __name__ == '__main__':
    recording = False
    recorder = AudioToTextRecorder()
    while True:
        recorder.text(process_text)

