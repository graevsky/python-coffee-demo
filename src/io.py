from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True, slots=True)
class DataRow:
    student: str
    date: date
    coffee_spent: float
    sleep_hours: float
    study_hours: float
    mood: str
    exam: str


def read_data_rows(files: Iterable[str]) -> list[DataRow]:
    rows: list[DataRow] = []

    for file_path in files:
        path = Path(file_path)
        if not path.exists() or not path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open("r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for raw_row in reader:
                rows.append(
                    DataRow(
                        student=raw_row["student"].strip(),
                        date=date.fromisoformat(raw_row["date"]),
                        coffee_spent=float(raw_row["coffee_spent"]),
                        sleep_hours=float(raw_row["sleep_hours"]),
                        study_hours=float(raw_row["study_hours"]),
                        mood=raw_row["mood"].strip(),
                        exam=raw_row["exam"].strip(),
                    )
                )

    return rows
