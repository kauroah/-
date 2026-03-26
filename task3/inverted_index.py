import os
import re


# Folder with pages from Task 1
PAGES_FOLDER = "../task1/pages"

# Output file
INDEX_FILE = "inverted_index.txt"


# -----------------------------
# Tokenization
# -----------------------------
def tokenize(text):

    tokens = re.findall(r"[A-Za-z]+", text)

    return [t.lower() for t in tokens if len(t) > 2]


# -----------------------------
# Build inverted index
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

        # remove html tags
        text = re.sub(r"<[^>]*>", " ", html)

        tokens = tokenize(text)

        for token in tokens:

            if token not in index:
                index[token] = set()

            index[token].add(doc_id)

    return index


# -----------------------------
# Save index to file
# -----------------------------
def save_index(index):

    with open(INDEX_FILE, "w", encoding="utf-8") as f:

        for term in sorted(index.keys()):

            docs = " ".join(str(d) for d in sorted(index[term]))

            f.write(f"{term}: {docs}\n")


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
            output.append(t)

    while stack:
        output.append(stack.pop())

    return output


# -----------------------------
# Boolean search
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

            stack.append(index.get(token, set()))

    return stack.pop() if stack else set()


# -----------------------------
# Main program
# -----------------------------
def main():

    print("Building inverted index...")

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