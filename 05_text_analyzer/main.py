"""
Text Analyzer Program

Reads a text file and generates a detailed analysis including:
- Line, word, character, and sentence counts
- Shortest and longest words
- Word frequency analysis
- CSV reports for summary, frequency, sorted frequency, and top words

Designed as a portfolio project demonstrating file handling,
text processing, and CSV report generation.
"""

import csv
import string
import os


def get_file_path():
    """
    Prompts the user for a text file path.

    If the user presses Enter without providing a path,
    a default sample file path is used.

    Returns:
        str: Path to the text file.
    """
    INPUT_FILE = "sample.txt"
    return input("Enter file path or press enter to use default: ") or INPUT_FILE


def read_text_file(path):
    """
    Reads the content of a text file.

    Args:
        path (str): Path to the text file.

    Returns:
        str | None: File content if successful, otherwise None.
    """
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {path} not found")
        return None


def clean_text(text):
    """
    Cleans and normalizes text by:
    - Converting to lowercase
    - Removing punctuation
    - Normalizing extra whitespace

    Args:
        text (str): Raw text content.

    Returns:
        str: Cleaned text.
    """
    text = text.lower()
    cleaned = ""

    for ch in text:
        if ch not in string.punctuation:
            cleaned += ch

    return " ".join(cleaned.split())


def count_chars(text):
    """Returns total number of characters including spaces."""
    return len(text)


def count_chars_no_space(text):
    """Returns total number of characters excluding spaces."""
    return len(text.replace(" ", ""))


def count_sentences(text):
    """
    Counts sentences based on punctuation markers.

    Sentence count is intentionally based on raw text
    to preserve '.', '!' and '?' markers.
    """
    return sum(1 for ch in text if ch in ["!", ".", "?"])


def shortest_longest(text):
    """
    Finds the shortest and longest words in the text.

    Args:
        text (str): Cleaned text.

    Returns:
        tuple: (shortest_word, longest_word) or (None, None) if no words exist.
    """
    words = text.split()
    if not words:
        return None, None

    return min(words, key=len), max(words, key=len)


def count_lines(text):
    """Counts non-empty lines in the text."""
    lines = text.splitlines()
    return sum(1 for line in lines if line.strip())


def count_words(text):
    """Returns total number of words."""
    return len(text.split())


def word_frequency(text):
    """
    Calculates frequency of each word in cleaned text.

    Args:
        text (str): Cleaned text.

    Returns:
        dict: Word frequency dictionary.
    """
    frequency = {}
    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def text_analyzer():
    """Main controller function for text analysis workflow."""
    path = get_file_path()
    content = read_text_file(path)

    if content is None:
        return

    cleaned = clean_text(content)

    line_count = count_lines(content)
    word_count = count_words(cleaned)
    char_count = count_chars(content)
    char_count_no_space = count_chars_no_space(content)
    sentence_count = count_sentences(content)
    shortest_word, longest_word = shortest_longest(cleaned)
    word_freq = word_frequency(cleaned)

    print("\nAnalysis Report")
    print("---------------------")
    print(f"Lines: {line_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Words: {word_count}")
    print(f"Total characters: {char_count}")
    print(f"Characters without spaces: {char_count_no_space}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Write summary CSV
    summary_file = "output/analysis_summary.csv"
    with open(summary_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Lines", "Sentences", "Words", "Characters",
            "Characters_No_Space", "Shortest_Word", "Longest_Word"
        ])
        writer.writerow([
            line_count, sentence_count, word_count,
            char_count, char_count_no_space,
            shortest_word, longest_word
        ])

    # Write word frequency CSV
    frequency_file = "output/frequency_word.csv"
    with open(frequency_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["word", "frequency"])
        writer.writeheader()
        for word, count in word_freq.items():
            writer.writerow({"word": word, "frequency": count})

    # Write sorted frequency CSV
    sorted_frequency = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_file = "output/sorted_frequency_word.csv"
    with open(sorted_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["word", "frequency"])
        writer.writeheader()
        for word, count in sorted_frequency:
            writer.writerow({"word": word, "frequency": count})

    # Write top N words CSV
    TOP_N = 10
    top_words = sorted_frequency[:TOP_N]
    top_words_file = "output/top_10_words.csv"
    with open(top_words_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["word", "frequency"])
        writer.writeheader()
        for word, count in top_words:
            writer.writerow({"word": word, "frequency": count})


if __name__ == "__main__":
    text_analyzer()
