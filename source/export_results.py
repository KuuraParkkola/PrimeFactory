from datetime import datetime
from pathlib import Path
from typing import Any


def export_results(path: Path, number: int, result: dict[str: Any]) -> None:
    time_now = datetime.now()
    output_path = Path.cwd()/f"output_{time_now.strftime('%Y%m%dT%H%M%S')}.txt" if path is None else path
    with output_path.open('w') as output_file:
        output_file.writelines([
            "PrimeFactory outputs\n",
            f"Date: {time_now.strftime('%a %b %d %Y %I:%M %p')}\n",
            f"Prime factors of number {number} are:\n",
            f"{', '.join(map(str, result['factors']))}\n",
            f"Which were found in {result['runtime']:.2f} seconds.\n"
        ])
