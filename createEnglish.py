from nltk import corpus  # must download words
import english_words

import json


def populate_words(current_words: set, new_words: set):
    current_words.update(new_words)
    return current_words


def main():
    words = set()

    # Add words from NLTK WordNet
    words = populate_words(words, set(corpus.words.words()))

    # Add words from https://svnweb.freebsd.org/csrg/share/dict/
    words = populate_words(words, set(english_words.english_words_set))

    with open('./valid_words.json', 'w') as word_file:
        json.dump(list(words), word_file)


if __name__ == '__main__':
    main()
