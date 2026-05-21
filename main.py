"""
Pascal's Triangle with mod systems /
Modify the variables at the top of the file to change parameters
Software by me (Tejas Bhagawatula)
"""

ROWS = 10
MOD = 10


def pascal_triangle(n: int, mod: int = 10) -> list[list[int]]:
    """
    args:
        n:   Number of rows to generate.
        mod: Modulus applied to each element. Defaults to 10.

    returns:
        A list of rows, where each row is a list of integers.
    """
    triangle: list[list[int]] = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = (
            [1]
            + [(prev_row[j - 1] + prev_row[j]) % mod for j in range(1, i)]
            + [1]
        )
        triangle.append(new_row)

    return triangle


def print_triangle(triangle: list[list[int]]) -> None:
    """
    Print Pascal's triangle centered w/ row numbers on the right

    args:
        triangle: The triangle as returned by `pascal_triangle`.
    """
    n = len(triangle)
    # Widest row determines the padding needed for centring
    max_width = len(" ".join(str(v) for v in triangle[-1]))

    for row_index, row in enumerate(triangle):
        row_str = " ".join(str(v) for v in row)
        padding = (max_width - len(row_str)) // 2
        spaces = " " * padding
        print(f"| {spaces}{row_str}{spaces} | {row_index + 1}")


if __name__ == "__main__":
    print(f"Pascal's triangle mod({MOD}) up to row {ROWS}")
    print("To change, modify ROWS and MOD at the top of the file.\n")
    print_triangle(pascal_triangle(ROWS, MOD))
