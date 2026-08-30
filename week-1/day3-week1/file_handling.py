## read file
# read entire file
with open("practice_file-handling.txt", "r") as file:
    content = file.read()
print(content)

# read line by line
with open("practice_file-handling.txt", "r") as file:
    for line in file:
        print(line.strip())

# read into a list
with open("practice_file-handling.txt", "r") as file:
    lines = file.readlines()
    print(lines)

## extract

# extract words
with open("practice_file-handling.txt") as file:
    words = file.read().split()
print(words)

# extract lines
with open("practice_file-handling.txt") as file:
    #overcomplicated version of read file line by line
    new_lines = []
    for line in file:
        new_lines = line.strip()
        print(new_lines)


# extract characters
with open("practice_file-handling.txt") as file:
    characters = []
    for line in file:
        characters += line.strip()
print(characters)