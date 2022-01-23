from __future__ import annotations

from nltk import corpus  # must download words
import english_words

import wordfreq

import json


DEFAULT_LENGTHS = [5, 6, 7]

# Minimum Zipf frequency for a word to be a possible answer
FREQUENCY_THRESHOLD = 4.0


def frequency_is_above(word: str, frequency_threshold: float = FREQUENCY_THRESHOLD) -> bool:
    return wordfreq.zipf_frequency(word, 'en') >= frequency_threshold


def populate_words(current_words: set, new_words: set) -> set:
    current_words.update(new_words)
    return current_words


def write_to_json(fname: str, words: list[str]) -> None:
    if len(words) == 0:
        print(fname, words)
    with open(fname, 'w') as file:
        json.dump(words, file)


def main():
    words = set()

    # Add words from NLTK WordNet
    words = populate_words(words, set(corpus.words.words()))

    # Add words from https://svnweb.freebsd.org/csrg/share/dict/
    words = populate_words(words, set(english_words.english_words_set))

    words = set(map(lambda word: word.upper(), words))
    answers = set(filter(lambda word: frequency_is_above(word), words))

    write_to_json('./data/valid_words.json', list(words))
    write_to_json('./data/answers.json', list(answers))

    for length in DEFAULT_LENGTHS:
        filtered_words = list(filter(lambda word: len(word) == length, words))
        filtered_answers = list(
            filter(lambda word: frequency_is_above(word), filtered_words))

        write_to_json(
            f'./data/valid_words_{length}.json', list(filtered_words))
        write_to_json(f'./data/answers_{length}.json', list(filtered_answers))


if __name__ == '__main__':
    main()
