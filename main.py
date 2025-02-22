from fastapi import FastAPI, File, UploadFile
from pydub import AudioSegment
import shutil
import os

app = FastAPI()

@app.post("/merge-audio/")
async def merge_audio(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    try:
        # Save uploaded files
        with open(file1.filename, "wb") as buffer:
            shutil.copyfileobj(file1.file, buffer)
        with open(file2.filename, "wb") as buffer:
            shutil.copyfileobj(file2.file, buffer)

        # Load audio files
        audio1 = AudioSegment.from_file(file1.filename)
        audio2 = AudioSegment.from_file(file2.filename)

        # Merge audio
        merged_audio = audio1 + audio2
        merged_filename = "merged_audio.mp3"
        merged_audio.export(merged_filename, format="mp3")

        # Return the merged file as a response
        return {"message": "Audio merged successfully!", "download_url": f"/download/{merged_filename}"}
    
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/download/{filename}")
async def download_file(filename: str):
    return FileResponse(filename, media_type="audio/mpeg", filename=filename)
