from random import sample
from typing import Self

from alphabet import (
    alphabet,
    vowels_alphabet
)
from user_interface import (
    RAND_MATRIX_GENERATED_MSG,
    ONLY_ENG_LETTERS_MSG,
    ONLY_FIVE_LETTERS_MSG,
    USER_FILLED_MATRIX_MSG,
    MATRIX_WAS_SORTED_MSG,
    input_word_ask_msg,
)

__all__ = ["Matrix"]


class Matrix:
    _matrix: list
    _matrix_size: int
    _is_sorted: bool

    def __init__(self, matrix: list[list[str]], matrix_size: int) -> None:
        self._matrix = matrix
        self._matrix_size = matrix_size
        self._is_sorted = False

    @classmethod
    def from_random(cls, matrix_size: int) -> Self:
        matrix = []

        for row in range(matrix_size):
            matrix_row = []
            for column in range(matrix_size):
                matrix_row.append("".join(sample(alphabet, 5)))

            matrix.append(matrix_row)

        print(RAND_MATRIX_GENERATED_MSG)
        return cls(matrix, matrix_size)

    @classmethod
    def from_user(cls, matrix_size: int) -> Self:
        matrix = []

        for row in range(matrix_size):
            matrix_row = []
            while len(matrix_row) < matrix_size:
                print(input_word_ask_msg(row))
                word = input()
                if any(letter not in alphabet for letter in word):
                    print(ONLY_ENG_LETTERS_MSG)
                    continue
                elif len(word) != 5:
                    print(ONLY_FIVE_LETTERS_MSG)
                    continue

                matrix_row.append(word)

            matrix.append(matrix_row)

        print(USER_FILLED_MATRIX_MSG)
        return cls(matrix, matrix_size)

    def sort_matrix(self) -> None:
        for row in range(len(self._matrix)):
            for column in range(len(self._matrix)):
                self._matrix[row][column] = "".join(sorted(self._matrix[row][column]))

        self._is_sorted = True
        print(MATRIX_WAS_SORTED_MSG)

    def __str__(self) -> str:
        vowel, consonant = 0, 0
        matrix_msg = "\nResult matrix is:\n\n"

        for row in self._matrix:
            for word in row:
                matrix_msg += word + " "
            matrix_msg += '\n'

        for row in self._matrix:
            for word in row:
                for letter in word:
                    if letter in vowels_alphabet:
                        vowel += 1
                    else:
                        consonant += 1

        matrix_msg += f"\nVowel letters: {vowel}.\nConsonant letters: {consonant}.\n"

        return matrix_msg
