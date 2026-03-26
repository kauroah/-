import os
import math
from collections import defaultdict


TFIDF_FOLDER = "../task4/terms_tfidf"


# -----------------------------
# load document vectors
# -----------------------------
def load_vectors():

    vectors = {}

    files = sorted(os.listdir(TFIDF_FOLDER))

    for file in files:

        if not file.endswith(".txt"):
            continue

        doc_id = int(file.split("_")[-1].replace(".txt", ""))

        path = os.path.join(TFIDF_FOLDER, file)

        vector = {}

        with open(path, "r", encoding="utf-8") as f:

            for line in f:

                parts = line.split()

                term = parts[0]
                tfidf = float(parts[2])

                vector[term] = tfidf

        vectors[doc_id] = vector

    return vectors


# -----------------------------
# cosine similarity
# -----------------------------
def cosine_similarity(v1, v2):

    dot = 0
    norm1 = 0
    norm2 = 0

    for term in v1:

        if term in v2:
            dot += v1[term] * v2[term]

        norm1 += v1[term] ** 2

    for term in v2:
        norm2 += v2[term] ** 2

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot / (math.sqrt(norm1) * math.sqrt(norm2))


# -----------------------------
# build query vector
# -----------------------------
def build_query_vector(query):

    terms = query.lower().split()

    vector = defaultdict(int)

    for term in terms:
        vector[term] += 1

    return vector


# -----------------------------
# search
# -----------------------------
def search(query, doc_vectors):

    query_vector = build_query_vector(query)

    scores = []

    for doc_id, vector in doc_vectors.items():

        score = cosine_similarity(query_vector, vector)

        scores.append((doc_id, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores


# -----------------------------
# main
# -----------------------------
def main():

    print("Loading document vectors...")

    doc_vectors = load_vectors()

    print("Vector search ready")

    while True:

        query = input("\nEnter search query (or 'exit'): ")

        if query.lower() == "exit":
            break

        results = search(query, doc_vectors)

        print("\nTop results:")

        for doc_id, score in results[:10]:

            if score > 0:
                print(f"Document {doc_id}  score={score:.4f}")


if __name__ == "__main__":
    main()