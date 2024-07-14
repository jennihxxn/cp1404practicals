"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 25 minutes
Actual:   37 minutes
"""
def main():
    text = input("Text: ")

    word_counts = {}
    for word in text.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    max_word_length = max(len(word) for word in word_counts)

    for word in sorted(word_counts):
        print(f"{word:{max_word_length}} : {word_counts[word]}")

if __name__ == "__main__":
    main()