from __future__ import annotations

import argparse
from typing import Sequence

from tabulate import tabulate

from .io import read_data_rows
from .report import REPORTS, TableReport


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="student-exam-report",
        description="Build reports from student exam CSV data",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files (multiple files allowed).",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name. Supported: " + ", ".join(sorted(REPORTS.keys())),
    )
    return parser


def _format_cell(value: object) -> object:
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        return round(value, 2)
    return value


def render_report(report: TableReport) -> str:
    table = [[_format_cell(cell) for cell in row] for row in report.rows]
    return tabulate(table, headers=report.headers, tablefmt="github")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    report_name: str = args.report

    if report_name not in REPORTS:
        parser.error(
            f"Unsupported report: {report_name}. "
            f"Supported: {', '.join(sorted(REPORTS.keys()))}"
        )

    try:
        rows = read_data_rows(args.files)
    except FileNotFoundError as exc:
        parser.error(str(exc))

    report_builder = REPORTS[report_name]
    report = report_builder(rows)

    print(render_report(report))
    return 0
