import sys
import numpy as np
import librosa
from scipy.spatial.distance import cosine

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python detect.py reference.wav suspect.wav")
        sys.exit(1)

    ref_features = extract_features(sys.argv[1])
    sus_features = extract_features(sys.argv[2])

    similarity = 1 - cosine(ref_features, sus_features)
    print(f"Similarity score: {similarity:.2f}")

    if similarity < 0.75:
        print("⚠️ Potential deepfake detected.")
    else:
        print("✅ Likely authentic.")
