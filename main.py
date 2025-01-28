from typing import Annotated
from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
from tqdm import tqdm
import numpy as np
from fastapi import FastAPI, UploadFile, File

encoder = VoiceEncoder()

app = FastAPI()

async def writeFile(file: UploadFile, filename: str):
    with open(filename, "wb") as f:
        f.write(await file.read())

@app.post("/verify-voice", status_code=200)
async def verifyVoice(verification: UploadFile = File(...), cloning: UploadFile = File(...)):
    await writeFile(verification, "verification.wav")
    await writeFile(cloning, "cloning.wav")

    verificationWav = preprocess_wav("verification.wav")
    cloningWav = preprocess_wav("cloning.wav")

    utteranceEmbedA = encoder.embed_utterance(verificationWav)
    utteranceEmbedB = encoder.embed_utterance(cloningWav)

    utteranceSimilarityScore: float = np.dot(utteranceEmbedA, utteranceEmbedB) / (np.linalg.norm(utteranceEmbedA) * np.linalg.norm(utteranceEmbedB))
    return {'similarityScore': float(utteranceSimilarityScore)}