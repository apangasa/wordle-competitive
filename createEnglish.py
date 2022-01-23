from nltk import corpus

import json


def populate_words_nltk(words: set):
    words.update(set(corpus.words.words()))
    return words


if __name__ == '__main__':
    words = set()

    words = populate_words_nltk(words)

    with open('./valid_words.json', 'w') as word_file:
        json.dump(list(words), word_file)
