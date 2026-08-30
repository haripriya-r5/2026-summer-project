## final version

def strip_trailing_whitespace(file):
    with open(file):
        for line in file:
            cleaned = line.strip()
            print(cleaned)

# not necessary here as it is a function and not in the main script, but useful for future
if __name__ == "__main__":
    strip_trailing_whitespace("pjo-book2-extract.txt")


## initial attempt
"""
with open("pjo-book2-extract.txt") as file:
    for line in file:
        print(line.strip())
"""