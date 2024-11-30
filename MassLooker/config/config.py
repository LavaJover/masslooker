import json
from typing import Any


def load_config(filename: str = 'config.json') -> Any:
    with open(filename, "r") as f:
        return json.load(f)


if __name__ == '__main__':
    print(load_config('config.json'))