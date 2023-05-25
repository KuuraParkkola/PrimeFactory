from pathlib import Path
from json import loads, dumps


def load_data(path: Path) -> dict[int, tuple[int]]:
    try:
        with path.open("r") as input_file:
            data = loads(input_file.read())
        return data
    except FileNotFoundError:
        return {}

def save_data(path: Path, data: dict[int, tuple[int]]) -> None:
    with path.open("w") as output_file:
        output_file.write(dumps(data, indent=2))
