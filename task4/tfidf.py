import os
import re
import math
from collections import Counter


PAGES_FOLDER = "../task1/pages"
TOKENS_FOLDER = "../task2/output"

TERMS_OUTPUT = "terms_tfidf"
LEMMAS_OUTPUT = "lemmas_tfidf"


# -----------------------------
# load tokens file
# -----------------------------
def load_tokens(file_path):

    tokens = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            tokens.append(line.strip())

    return tokens


# -----------------------------
# load lemmas file
# -----------------------------
def load_lemmas(file_path):

    lemmas = {}

    with open(file_path, "r", encoding="utf-8") as f:

        for line in f:

            parts = line.strip().split()

            lemma = parts[0]
            forms = parts[1:]

            lemmas[lemma] = forms

    return lemmas


# -----------------------------
# compute idf
# -----------------------------
def compute_idf(all_docs_terms):

    N = len(all_docs_terms)

    df = {}

    for terms in all_docs_terms:

        unique = set(terms)

        for term in unique:

            df[term] = df.get(term, 0) + 1

    idf = {}

    for term in df:

        idf[term] = math.log(N / df[term])

    return idf


# -----------------------------
# main
# -----------------------------
def main():

    os.makedirs(TERMS_OUTPUT, exist_ok=True)
    os.makedirs(LEMMAS_OUTPUT, exist_ok=True)

    files = sorted(os.listdir(TOKENS_FOLDER))

    all_docs_terms = []

    doc_tokens = {}

    for file in files:

        if file.startswith("tokens_"):

            path = os.path.join(TOKENS_FOLDER, file)

            tokens = load_tokens(path)

            doc_id = file.split("_")[1].replace(".txt", "")

            doc_tokens[doc_id] = tokens

            all_docs_terms.append(tokens)


    idf = compute_idf(all_docs_terms)


    for doc_id, tokens in doc_tokens.items():

        total_terms = len(tokens)

        counter = Counter(tokens)

        output_file = os.path.join(
            TERMS_OUTPUT,
            f"terms_tfidf_{doc_id}.txt"
        )

        with open(output_file, "w", encoding="utf-8") as f:

            for term in counter:

                tf = counter[term] / total_terms
                term_idf = idf.get(term, 0)
                tfidf = tf * term_idf

                f.write(f"{term} {term_idf:.6f} {tfidf:.6f}\n")


    # process lemmas

    for file in files:

        if file.startswith("lemmas_"):

            path = os.path.join(TOKENS_FOLDER, file)

            lemmas = load_lemmas(path)

            doc_id = file.split("_")[1].replace(".txt", "")

            tokens = doc_tokens[doc_id]

            total_terms = len(tokens)

            output_file = os.path.join(
                LEMMAS_OUTPUT,
                f"lemmas_tfidf_{doc_id}.txt"
            )

            with open(output_file, "w", encoding="utf-8") as f:

                for lemma, forms in lemmas.items():

                    count = 0

                    for form in forms:

                        count += tokens.count(form)

                    if count == 0:
                        continue

                    tf = count / total_terms
                    lemma_idf = idf.get(forms[0], 0)
                    tfidf = tf * lemma_idf

                    f.write(f"{lemma} {lemma_idf:.6f} {tfidf:.6f}\n")


    print("TF-IDF calculation completed")


if __name__ == "__main__":
    main()