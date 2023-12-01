__all__ = [
    "ASK_MATRIX_SIZE_MSG",
    "ASK_FILLING_WAY_MSG",
    "KEYBOARD_INTERRUPT_MSG",
    "VALUE_ERROR_MSG",
    "SIZE_NOT_IN_INTERVAL_MSG",
    "FILLING_WAY_INCORRECT_INPUT_MSG",
    "RAND_MATRIX_GENERATED_MSG",
    "ONLY_ENG_LETTERS_MSG",
    "ONLY_FIVE_LETTERS_MSG",
    "USER_FILLED_MATRIX_MSG",
    "MATRIX_WAS_SORTED_MSG",
    "input_word_ask_msg",
]

ASK_MATRIX_SIZE_MSG = """Input num M (from 2 to 5), and i will create matrix MxM size."""

ASK_FILLING_WAY_MSG = """
Now we need to fill this matrix.
Should I fill it myself (1) or gonna do it yourself (2)?
Input 1 or 2 to answer."""

KEYBOARD_INTERRUPT_MSG = """
You just tried to break my programme, but u got no success.
Just try again mate, wish u luck, ha-ha ^-^"""

VALUE_ERROR_MSG = """
Input data must be INTEGER, just a num (from 2 to 5).  
Try again."""

SIZE_NOT_IN_INTERVAL_MSG = """
Input num must be FROM 2 TO 5.
Try again."""

FILLING_WAY_INCORRECT_INPUT_MSG = """
Input data must be 1 or 2.
Try again."""

RAND_MATRIX_GENERATED_MSG = """
Random matrix was generated."""

ONLY_ENG_LETTERS_MSG = """
Word must consist of English alphabet's letters.
Try again."""

ONLY_FIVE_LETTERS_MSG = """
Word must consist of 5 letters.
Try again."""

USER_FILLED_MATRIX_MSG = """
You have filled the matrix."""

MATRIX_WAS_SORTED_MSG = """
Matrix's words were sorted."""


def input_word_ask_msg(row: int) -> str:
    return f"Input a word for {row + 1} row. It must be from five letters"
