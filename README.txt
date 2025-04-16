Driver Face ID Authentication System
====================================

Features:
- Face Registration and Authentication
- AES-256 Secure Storage of Face Embeddings
- Cosine Similarity for Matching

Dependencies:
- face_recognition
- numpy
- opencv-python
- cryptography

To Install:
pip install face_recognition numpy opencv-python cryptography

To Run:
python main.py

Usage:
1. Register a face with clear front view.
2. Authenticate by showing the same face.
3. If matched (cosine similarity >= 0.6), you'll see "Authentication Successful"
   otherwise "Authentication Failed".