from typing import List, Union


def get_input() -> str:
    with open('input.txt') as file:
        return file.read()


def get_key(symbol: str) -> Union[int, str]:
    for key, symbols in KEYBOARD.items():
        if symbol in symbols:
            return key

    raise ValueError(f"Unexpected symbol: {symbol}")


def get_key_sequence(sms: str) -> List:
    sequence = []
    for symbol in sms:
        key = get_key(symbol)
        if len(sequence) == 0:
            sequence.append(key)
        elif sequence[-1] != key:
            sequence.append(key)

    return sequence


def main():
    input_data = get_input()
    length, sms = input_data.split('\n')
    sms = sms.lower()

    print(sms)
    key_sequence = get_key_sequence(sms)
    print(key_sequence)


if __name__ == "__main__":
    KEYBOARD = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    main()