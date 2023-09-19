import whisper

model = whisper.load_model("base")
transcription = model.transcribe("audio01.mp3")

with open("transcription.txt", "w") as file:
    file.write(transcription['text'])
