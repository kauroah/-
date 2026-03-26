import os
import re
from collections import defaultdict


INPUT_FOLDER = "../task1/pages"
OUTPUT_FOLDER = "output"


STOPWORDS = {
    "the","and","for","with","that","this","from","are","was","were",
    "have","has","had","not","but","you","your","about","into","their",
    "there","they","them","then","than","also","such","only","other",
    "when","what","which","while","where","who","whom","because",
    "before","after","between","during","above","below","over",
    "under","again","further","once","here","there","why","how"
}


# -----------------------------
# Remove HTML
# -----------------------------
def remove_html(text):
    return re.sub(r"<[^>]*>", " ", text)


# -----------------------------
# Extract tokens
# -----------------------------
def extract_tokens(text):

    tokens = re.findall(r"[A-Za-z]+", text)

    cleaned = []

    for token in tokens:

        token = token.lower()

        if len(token) < 3:
            continue

        if token in STOPWORDS:
            continue

        cleaned.append(token)

    return cleaned


# -----------------------------
# Simple Lemmatizer
# -----------------------------
def simple_lemma(word):

    endings = ["ing","ed","es","s"]

    for end in endings:
        if word.endswith(end) and len(word) > len(end) + 2:
            return word[:-len(end)]

    return word


# -----------------------------
# MAIN
# -----------------------------
def main():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    files = sorted(os.listdir(INPUT_FOLDER))

    for file in files:

        if not file.endswith(".txt"):
            continue

        doc_id = file.replace(".txt", "")

        print("Processing:", file)

        path = os.path.join(INPUT_FOLDER, file)

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

        text = remove_html(html)

        tokens = extract_tokens(text)

        tokens_unique = sorted(set(tokens))


        # Save tokens_i.txt
        token_file = os.path.join(OUTPUT_FOLDER, f"tokens_{doc_id}.txt")

        with open(token_file, "w", encoding="utf-8") as f:
            for token in tokens_unique:
                f.write(token + "\n")


        # Group by lemmas
        lemma_dict = defaultdict(set)

        for token in tokens_unique:

            lemma = simple_lemma(token)

            lemma_dict[lemma].add(token)


        # Save lemmas_i.txt
        lemma_file = os.path.join(OUTPUT_FOLDER, f"lemmas_{doc_id}.txt")

        with open(lemma_file, "w", encoding="utf-8") as f:

            for lemma in sorted(lemma_dict.keys()):

                words = " ".join(sorted(lemma_dict[lemma]))

                f.write(f"{lemma} {words}\n")


    print("DONE")
    print("All tokens_i.txt and lemmas_i.txt files created")


if __name__ == "__main__":
    main()