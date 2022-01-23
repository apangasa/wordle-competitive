from __future__ import annotations

from nltk import corpus  # must download words
import english_words

import json


DEFAULT_LENGTHS = [5, 6, 7]


def populate_words(current_words: set, new_words: set) -> set:
    current_words.update(new_words)
    return current_words


def write_to_json(fname: str, words: list[str]) -> None:
    with open(fname, 'w') as file:
        json.dump(words, file)


def main():
    words = set()

    # Add words from NLTK WordNet
    words = populate_words(words, set(corpus.words.words()))

    # Add words from https://svnweb.freebsd.org/csrg/share/dict/
    words = populate_words(words, set(english_words.english_words_set))

    words = set(map(lambda word: word.upper(), words))

    write_to_json('./valid_words.json', list(words))

    for length in DEFAULT_LENGTHS:
        filtered_words = filter(lambda word: len(word) == length, words)
        write_to_json(f'./valid_words_{length}.json', list(filtered_words))


if __name__ == '__main__':
    main()
