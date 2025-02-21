import json
from typing import List


def load_data(filename: str) -> List[dict]:
    with open(filename, "r") as f:
        data = json.load(f)
    return data
