import pathlib
from itertools import chain


def group(values: list, n: int):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[index:index + n] for index in range(0, len(values), n)]


def create_grid(puzzle: str):
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def read_sudoku(path):
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def display(grid) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def get_row(grid, pos) -> str:
    """ Возвращает все значения для номера строки, указанной в pos

    get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """

    return grid[pos[0]]


def get_col(grid, pos) -> list:
    """ Возвращает все значения для номера столбца, указанного в pos

    get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """

    return [grid[0][pos[1]], grid[1][pos[1]], grid[2][pos[1]]]


def get_block(grid, pos) -> list:
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    grid = read_sudoku('puzzle1.txt')
    get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    # PUT YOUR CODE HERE

    start_i, start_y = (pos[1] // 3) * 3, (pos[0] // 3) * 3
    return list(chain(*[grid[y][start_i:start_i + 3] for y in range(start_y, start_y + 3)]))


grid = read_sudoku('puzzle1.txt')

display(grid)

print(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)))
print(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)))
print(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)))
print('---------------------')
print(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)))
print(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)))
print(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)))
print('---------------------')
print(get_block(grid, (0, 1)))
print(get_block(grid, (4, 7)))
print(get_block(grid, (8, 8)))
