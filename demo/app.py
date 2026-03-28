import os
import math
from collections import defaultdict
from flask import Flask, render_template, request


TFIDF_FOLDER = "../task4/terms_tfidf"

app = Flask(__name__)

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


doc_vectors = load_vectors()


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


def build_query_vector(query):

    terms = query.lower().split()

    vector = defaultdict(int)

    for term in terms:
        vector[term] += 1

    return vector


def search(query):

    query_vector = build_query_vector(query)

    scores = []

    for doc_id, vector in doc_vectors.items():

        score = cosine_similarity(query_vector, vector)

        scores.append((doc_id, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:10]

@app.route("/", methods=["GET", "POST"])
def index():

    results = []

    if request.method == "POST":

        query = request.form["query"]

        results = search(query)

    return render_template("index.html", results=results)


if __name__ == "__main__":

    app.run(debug=True)