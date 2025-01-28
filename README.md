# Voice Verification Concept

## Introduction

This concept was created as a way to determine if an in-house voice verification process would be feasible. The result is a fast-api endpoint that takes two audio files, **a verification script** and a **longer cloning script**, and outputs a **score** from 0 to 1 based on the likeness of the two audio files.

The process uses Resemble AI's **Resemblyzer** package to calculate the score.

## Setup

This project requires **Python 3.11** as it is the last version that supports certain packages that Resemblyzer uses.

1. Clone this repository and cd into it
2. Install python 3.11 [(link to download)](https://www.python.org/downloads/release/python-3110/)
3. Install virtualenv
   - python -m pip install --user virtualenv
4. Create a virtual python environment
   - virtualenv **environment-name** --python=python3.11
5. Activate the environment
   - ./**environment-name**/Scripts/activate
6. Download the requirements
   - pip install requirements.txt
7. Start the server
   - fastapi run main.py

## Testing Notes
- Scores are deterministic
- Able to accurately score my voice when using a short verification script (5s) and a longer cloning script (~1m) with a laptop microphone. Scores ranged from 0.90 to 0.97. This included using different voice moods and tones.
- When tested against differing voices the highest score I was able to obtain was 0.70.

## TO-DO

- Much more testing
  - Test different langauges