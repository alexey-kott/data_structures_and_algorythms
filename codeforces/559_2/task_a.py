
def get_input() -> str:
    input()
    operatinos = input()
    return operatinos


def is_enough_stones(stones: int, operations: str) -> bool:
    for operation in operations:
        if operation == '+':
            stones += 1
        else:
            stones -= 1
        if stones < 0:
            return False
    return True


def main():
    operations = get_input()

    for i in range(101):
        stones = i
        if is_enough_stones(i, operations):
            break

    for operation in operations:
        if operation == '+':
            stones += 1
        else:
            stones -= 1

    print(stones)


if __name__ == "__main__":
    main()
