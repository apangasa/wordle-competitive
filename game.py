from __future__ import annotations

from enum import Enum

import numpy as np
import json


class Status(Enum):
    GREY = 1
    YELLOW = 2
    GREEN = 3


class Guess:
    def __init__(self, word: str):
        self.word = word
        self.status_list = [None] * len(word)

    def validate(self, valid_words) -> bool:
        return self.word in valid_words

    def compute_status_list(self, answer: str) -> list[Status]:
        for guess_idx, guess_letter in enumerate(self.word):
            answer_indices = []

            answer_idx = answer.find(guess_letter)
            while answer_idx != -1:
                answer_indices.append(answer_idx)
                answer_idx = answer.find(guess_letter, start=answer_idx + 1)
            
            if len(answer_indices) == 0:
                self.status_list[guess_idx] = Status.GREY
            elif guess_idx in answer_indices:
                self.status_list[guess_idx] = Status.GREEN
            else:
                self.status_list[guess_idx] = Status.YELLOW
        return self.status_list

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
    num_guesses = 6

    words = load_words(length=length_choice)
    answers = load_answers(length=length_choice)

    answer = pick_word(answers)

    print(answer)

    board = [[None] * length_choice] * num_guesses
    print(board)


if __name__ == '__main__':
    main()
