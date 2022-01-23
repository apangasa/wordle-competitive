from __future__ import annotations

from enum import Enum

import numpy as np
import json

from pprint import pprint


class Status(Enum):
    GREY = 1
    YELLOW = 2
    GREEN = 3


class GuessLetter:
    def __init__(self, letter: str, status: Status):
        self.letter = letter
        self.status = status

    def __str__(self):
        return f'{self.letter}, {self.status}'

    def __repr__(self):
        return f'{self.letter}, {self.status}'


class Guess:
    def __init__(self, word: str, answer: str):
        self.word = word
        self.answer = answer
        self.guess_letters = [None] * len(word)
        self.compute_statuses()

    def validate(self, valid_words) -> bool:
        return self.word in valid_words

    def compute_statuses(self) -> None:
        for guess_idx, guess_letter in enumerate(self.word):
            answer_indices = []

            answer_idx = self.answer.find(guess_letter)
            while answer_idx != -1:
                answer_indices.append(answer_idx)
                answer_idx = self.answer.find(guess_letter, answer_idx + 1)

            if len(answer_indices) == 0:
                self.guess_letters[guess_idx] = GuessLetter(
                    guess_letter, Status.GREY)
            elif guess_idx in answer_indices:
                self.guess_letters[guess_idx] = GuessLetter(
                    guess_letter, Status.GREEN)
            else:
                self.guess_letters[guess_idx] = GuessLetter(
                    guess_letter, Status.YELLOW)


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
    guesses_left = num_guesses = 6

    words = load_words(length=length_choice)
    answers = load_answers(length=length_choice)

    answer = pick_word(answers)

    # print(answer)

    board = [[None] * length_choice] * num_guesses
    pprint(board)

    while guesses_left:
        guess = Guess(input('Enter guess: ').upper(), answer)
        board[num_guesses - guesses_left] = guess.guess_letters
        guesses_left -= 1

        pprint(board)

    print(answer)


if __name__ == '__main__':
    main()
