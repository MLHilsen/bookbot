from collections import defaultdict

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = word_cnt(file_contents)
    letter_frequency = letter_freq(file_contents)

    print(report(word_count, letter_frequency))


def word_cnt(file_contents):
    return len(file_contents.split())


def letter_freq(file_contents):
    letter_freq = defaultdict(int)
    file_contents = file_contents.lower()

    for letter in file_contents:
        letter_freq[letter] += 1

    return letter_freq


def report(word_count, letter_frequency):
    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{word_count} words found in document", end='\n\n')

    for char in letter_frequency:
        if char.isalpha():
            print(f"The '{char}' character was found {letter_frequency[char]} times")




main()