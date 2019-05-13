from typing import List, Union, Set


def get_input() -> str:
    with open('input.txt') as file:
        return file.read()


def get_rook_attack_fields(v: str, h: Union[str, int]) -> List[str]:
    coords = []
    for i in range(1, 9):
        if i == h:
            continue
        coords.append(f"{v}{i}")

    for i in range(97, 105):  # 'a' and 'h' in ascii respectively
        if ord(v) == i:
            continue
        coords.append(f"{chr(i)}{h}")

    return coords


def get_bishop_attack_fields(v: str, h: Union[str, int]) -> List[str]:
    coords = []
    # for i in range(ord(v))

    return coords


def get_queen_fields(v: str, h: Union[str, int]) -> Set[str]:
    queen_fields = []
    queen_fields.extend(get_rook_attack_fields(v, h))
    queen_fields.extend(get_bishop_attack_fields(v, h))

    return set(queen_fields)


def get_pawn_attack_fields(v: str, h: Union[str, int]) -> Set[str]:
    coords = []
    # TODO: implement this function

    return set(coords)


def get_fields_under_attack(piece: str, field: str) -> List[str]:
    v, h = list(field)
    if piece == 'queen':
        fields = get_queen_fields(v, h)
    elif piece == 'rook':
        fields = get_rook_attack_fields(v, h)
    elif piece == 'bishop':
        fields = get_bishop_attack_fields(v, h)
    else:
        fields = get_pawn_attack_fields(v, h)

    return sorted(fields)


def main():
    input_data = get_input()

    queen_coords, rook_coords, knight_coords = input_data.lower().split(' ')
    fields = get_fields_under_attack('queen', queen_coords)
    print(fields)


if __name__ == "__main__":
    main()

    """На шахматной доске 8х8 расположены три фигуры: ферзь, ладья и конь. Требуется определить количество пустых полей 
    доски, которые находятся под боем. Для простоты будем полагать, что фигуры могут «бить» через другие фигуры.
    Например, в рассмотренной справа ситуации будем считать, что ферзь бьет D5 через ладью.
    
    Входные данные
    В единственной строке входного файла INPUT.TXT записаны через пробел координаты расположения трех фигур: ферзя, 
    ладьи и коня соответственно. Каждая координата состоит из одного английского символа (от A до H) и 
    одной цифры (от 1 до 8).
    
    Выходные данные
    В выходной файл OUTPUT.TXT нужно вывести количество пустых полей, которые бьют указанные во входных данных фигуры.
    """
