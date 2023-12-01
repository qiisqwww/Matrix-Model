from matrix import Matrix
from user_interface import (
    ASK_MATRIX_SIZE_MSG,
    KEYBOARD_INTERRUPT_MSG,
    VALUE_ERROR_MSG,
    SIZE_NOT_IN_INTERVAL_MSG,
    ASK_FILLING_WAY_MSG,
    FILLING_WAY_INCORRECT_INPUT_MSG
)


def choose_matrix_size() -> int:
    try:
        size = int(input())
    except ValueError:
        print(VALUE_ERROR_MSG)
        return choose_matrix_size()

    if size not in range(2, 5 + 1):
        print(SIZE_NOT_IN_INTERVAL_MSG)
        return choose_matrix_size()

    return size


def get_filled_matrix(matrix_size: int) -> Matrix:
    state: str = input()

    match state:
        case "1":
            return Matrix.from_random(matrix_size)
        case "2":
            return Matrix.from_user(matrix_size)
        case _:
            print(FILLING_WAY_INCORRECT_INPUT_MSG)
            return get_filled_matrix(matrix_size)


def main() -> None:
    print(ASK_MATRIX_SIZE_MSG)
    matrix_size: int = choose_matrix_size()

    print(ASK_FILLING_WAY_MSG)
    matrix: Matrix = get_filled_matrix(matrix_size)

    matrix.sort_matrix()
    print(matrix)


if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print(KEYBOARD_INTERRUPT_MSG)
            continue
