from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
from tqdm import tqdm
import numpy as np

encoder = VoiceEncoder()

wavFilePaths = list(Path("./audioFiles").glob("*.wav"))
wavs = np.array(list(map(preprocess_wav, tqdm(wavFilePaths, "Preprocessing wavs.", len(wavFilePaths)))), dtype=object)

utteranceEmbedA = encoder.embed_utterance(wavs[0])
utteranceEmbedB = encoder.embed_utterance(wavs[1])

utteranceSimilarityMatrix = np.dot(utteranceEmbedA, utteranceEmbedB) / (np.linalg.norm(utteranceEmbedA) * np.linalg.norm(utteranceEmbedB))

print(utteranceSimilarityMatrix)
