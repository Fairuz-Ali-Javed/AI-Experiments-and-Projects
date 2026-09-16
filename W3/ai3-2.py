import os
import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(a, b):
    return np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))

model = SentenceTransformer("all-MiniLM-L6-v2")
# text = "AND HIS NAME IS JOHN CENA"

# embedded = model.encode(text)
# print(embedded)
# print(len(embedded)) #384


version1 = "How is the weather?"
# version2 = "Whats the forecast?"
version2 = "What is theory of relativity?"

v1 = model.encode(version1)
v2 = model.encode(version2)

print(cosine_similarity(v1, v2))

