# Deepfake Riot Detector

Prototype repository for a lightweight audio similarity check to flag suspicious WhatsApp voice notes (deepfakes in local dialects).

---

## Context
India’s first AI-driven riot is unlikely to start with a viral video — it will start with a 20-second fake voice note in a Tier-2 town.  
This prototype demonstrates how such fakes can be flagged quickly using simple signal processing.

---

## How it works
- Extracts MFCC features from reference and suspect audio clips.  
- Compares vectors using cosine similarity.  
- Flags suspicious mismatches above a threshold.  

This is a demo only, not a production detector.

---

## Quickstart

```bash
git clone https://github.com/ainahar/deepfake-riot-detector.git
cd deepfake-riot-detector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python detect.py data/sample_clips/reference.wav data/sample_clips/suspect.wav

## License
MIT — prototype only.

---
Note: This repository contains prototype/demo code for research and policy discussion. It is not intended for production use.
