def count_words(str):
    return len(str.split())

def count_letters(str):
    str = str.lower()
    counter = {}
    for c in str:
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    return counter

def sort_counter(counter):
    return sorted(filter(lambda c: c[0].isalpha(), list(counter.items())),key=lambda x: x[1], reverse=True)

path = "books/frankenstein.txt"

with open(path) as f:
    file_contents = f.read()
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_contents)} words found in the document")
    sorted_counter = sort_counter(count_letters(file_contents))
    for pair in sorted_counter:
        print(f"The '{pair[0]}' character was found {pair[1]} times")
    print("--- End report ---")