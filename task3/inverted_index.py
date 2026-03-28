import os
import re


PAGES_FOLDER = "../task1/pages"
INDEX_FILE = "inverted_index.txt"


# -----------------------------
# Tokenize
# -----------------------------
def tokenize(text):

    tokens = re.findall(r"[A-Za-z]+", text)

    return [t.lower() for t in tokens if len(t) > 2]


# -----------------------------
# Simple lemmatizer
# -----------------------------
def lemmatize(word):

    endings = ["ing", "ed", "es", "s"]

    for end in endings:
        if word.endswith(end) and len(word) > len(end) + 2:
            return word[:-len(end)]

    return word


# -----------------------------
# Build inverted index (LEMMA)
# -----------------------------
def build_index():

    index = {}

    files = sorted(os.listdir(PAGES_FOLDER))

    for file in files:

        if not file.endswith(".txt"):
            continue

        doc_id = int(file.replace(".txt", ""))

        path = os.path.join(PAGES_FOLDER, file)

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

        text = re.sub(r"<[^>]*>", " ", html)

        tokens = tokenize(text)

        for token in tokens:

            lemma = lemmatize(token)

            if lemma not in index:
                index[lemma] = set()

            index[lemma].add(doc_id)

    return index


# -----------------------------
# Save index
# -----------------------------
def save_index(index):

    with open(INDEX_FILE, "w", encoding="utf-8") as f:

        for lemma in sorted(index.keys()):

            docs = " ".join(str(d) for d in sorted(index[lemma]))

            f.write(f"{lemma}: {docs}\n")


# -----------------------------
# Convert query to postfix
# -----------------------------
def to_postfix(query):

    precedence = {"not": 3, "and": 2, "or": 1}

    tokens = query.replace("(", " ( ").replace(")", " ) ").split()

    output = []
    stack = []

    for token in tokens:

        t = token.lower()

        if t in ("and", "or", "not"):

            while stack and stack[-1] != "(" and precedence.get(stack[-1], 0) >= precedence[t]:
                output.append(stack.pop())

            stack.append(t)

        elif token == "(":
            stack.append(token)

        elif token == ")":

            while stack and stack[-1] != "(":
                output.append(stack.pop())

            stack.pop()

        else:
            output.append(token)

    while stack:
        output.append(stack.pop())

    return output


# -----------------------------
# Boolean search with lemma query
# -----------------------------
def boolean_search(index, query):

    postfix = to_postfix(query)

    all_docs = set()

    for docs in index.values():
        all_docs |= docs

    stack = []

    for token in postfix:

        if token == "and":

            b = stack.pop()
            a = stack.pop()
            stack.append(a & b)

        elif token == "or":

            b = stack.pop()
            a = stack.pop()
            stack.append(a | b)

        elif token == "not":

            a = stack.pop()
            stack.append(all_docs - a)

        else:

            lemma = lemmatize(token.lower())

            stack.append(index.get(lemma, set()))

    return stack.pop() if stack else set()


# -----------------------------
# Main
# -----------------------------
def main():

    print("Building inverted index (based on lemmas)...")

    index = build_index()

    save_index(index)

    print("Inverted index saved to inverted_index.txt")

    print("\nBoolean Search Ready")

    while True:

        query = input("\nEnter query (or 'exit'): ")

        if query.lower() == "exit":
            break

        result = boolean_search(index, query)

        print("Documents:", sorted(result))


if __name__ == "__main__":
    main()