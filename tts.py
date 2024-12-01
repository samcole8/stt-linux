import subprocess
from RealtimeSTT import AudioToTextRecorder

def process_text(text):
    try:
        subprocess.run(['wtype', text], check=True)
    except Exception as e:
        print(f"Error typing text: {e}")

if __name__ == '__main__':
    recorder = AudioToTextRecorder()
    while True:
        recorder.text(process_text)
