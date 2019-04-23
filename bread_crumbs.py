from typing import Dict, List

a = {
    'b': 4,
    'c': {
        'd': 3,
        'e': 5,
        'f': {
            'g': 8,
        }
    }
}

b = [('b', 4), ('c.d', 3), ('c.e', 5), ('c.f.g', 8)]


def extract(node: Dict, path: str = '') -> List:
    paths = []

    for key, value in node.items():
        if path:
            nested_path = path+'.'+key
        else:
            nested_path = key

        if isinstance(value, int):
            paths.append((nested_path, value))
        elif isinstance(value, dict):
            nested_paths = extract(value, nested_path)
            paths.extend(nested_paths)

    return paths


if __name__ == "__main__":
    assert b == extract(a)
