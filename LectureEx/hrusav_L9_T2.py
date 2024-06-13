import sys
import re

#bigrams shoud be in sentences only instead of in between sentences so after splitting sentence I should look for bigrams in it and print them out.

def extract_words_and_sentences(text):
    # Extract words (all non-whitespace sequences)
    words = re.findall(r'\S+', text)

    # Extract sentences (split by periods, question marks, and exclamation marks)
    sentences = re.split(r'[.!?]+', text)

    # Extract bigrams
    words_lower = [word.lower() for word in words]
    bigrams = [(words_lower[i], words_lower[i+1]) for i in range(len(words_lower)-1)]

    return words, sentences, bigrams

def save_to_files(words, sentences, bigrams, word_file, sentence_file, bigram_file):
    # Save words to file
    with open(word_file, 'w') as f:
        for word in words:
            f.write(word + '\n')

    # Save sentences to file
    with open(sentence_file, 'w') as f:
        for sentence in sentences:
            f.write(sentence.strip() + '\n')

    # Save bigrams to file
    with open(bigram_file, 'w') as f:
        for bigram in bigrams:
            f.write(' '.join(bigram) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use python3 analyze_text.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        # Read text from input file
        with open(input_file, 'r') as f:
            text = f.read()

        # Extract words, sentences, and bigrams
        words, sentences, bigrams = extract_words_and_sentences(text)

        # Save to files
        save_to_files(words, sentences, bigrams, 'words.txt', 'sentences.txt', 'bigrams.txt')

        print("Results saved to 'words.txt', 'sentences.txt', and 'bigrams.txt'.")
    except FileNotFoundError:
        print("File not found. Please check the path to the input file.")
    except Exception as e:
        print(f"An error occurred: {e}")

