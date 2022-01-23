import json
import numpy as np


def load_words(length: int = None) -> None:
    words = None
    fname = './data/valid_words.json'
    if length is not None:
        fname = f'./data/valid_words_{length}.json'

    with open(fname, 'r') as word_file:
        words = json.load(word_file)
    return set(words)


def load_answers(length: int = None) -> None:
    words = None
    fname = './data/answers.json'
    if length is not None:
        fname = f'./data/answers_{length}.json'

    with open(fname, 'r') as word_file:
        words = json.load(word_file)
    return set(words)


def pick_word(words: set) -> str:
    return np.random.choice(list(words))


def main():
    length_choice = 5

    words = load_words(length=length_choice)
    answers = load_answers(length=length_choice)

    answer = pick_word(answers)

    print(answer)


if __name__ == '__main__':
    main()
