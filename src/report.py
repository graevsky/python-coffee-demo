from __future__ import annotations

from dataclasses import dataclass
from statistics import median
from typing import Callable, Iterable

from .io import DataRow


@dataclass(frozen=True, slots=True)
class TableReport:
    headers: tuple[str, ...]
    rows: list[tuple[object, ...]]


ReportBuilder = Callable[[Iterable[DataRow]], TableReport]


def build_median_coffee_report(rows: Iterable[DataRow]) -> TableReport:
    spending_by_student: dict[str, list[float]] = {}

    for row in rows:
        spending_by_student.setdefault(row.student, []).append(row.coffee_spent)

    report_rows = [
        (student, median(spending)) for student, spending in spending_by_student.items()
    ]
    report_rows.sort(key=lambda item: (-item[1], item[0]))

    return TableReport(
        headers=("student", "median_coffee"),
        rows=report_rows,
    )


REPORTS: dict[str, ReportBuilder] = {
    "median-coffee": build_median_coffee_report,
}
