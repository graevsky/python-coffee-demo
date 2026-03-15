from datetime import date

from src.io import DataRow
from src.report import build_median_coffee_report


def test_build_median_coffee_report() -> None:
    rows = [
        DataRow(
            student="A",
            date=date(2024, 6, 1),
            coffee_spent=10.0,
            sleep_hours=8.0,
            study_hours=3.0,
            mood="ok",
            exam="Math",
        ),
        DataRow(
            student="A",
            date=date(2024, 6, 2),
            coffee_spent=20.0,
            sleep_hours=7.5,
            study_hours=4.0,
            mood="ok",
            exam="Math",
        ),
        DataRow(
            student="B",
            date=date(2024, 6, 1),
            coffee_spent=200.0,
            sleep_hours=5.0,
            study_hours=10.0,
            mood="tired",
            exam="Math",
        ),
        DataRow(
            student="B",
            date=date(2024, 6, 2),
            coffee_spent=0.0,
            sleep_hours=9.0,
            study_hours=1.0,
            mood="ok",
            exam="Math",
        ),
        DataRow(
            student="C",
            date=date(2024, 6, 1),
            coffee_spent=300.0,
            sleep_hours=4.0,
            study_hours=12.0,
            mood="zombie",
            exam="Physics",
        ),
        DataRow(
            student="C",
            date=date(2024, 6, 2),
            coffee_spent=660.0,
            sleep_hours=3.5,
            study_hours=14.0,
            mood="zombie",
            exam="Physics",
        ),
        DataRow(
            student="C",
            date=date(2024, 6, 3),
            coffee_spent=480.0,
            sleep_hours=3.0,
            study_hours=16.0,
            mood="dead",
            exam="Programming",
        ),
        DataRow(
            student="D",
            date=date(2024, 6, 1),
            coffee_spent=400.0,
            sleep_hours=6.0,
            study_hours=8.0,
            mood="ok",
            exam="Math",
        ),
        DataRow(
            student="E",
            date=date(2024, 6, 1),
            coffee_spent=10.0,
            sleep_hours=8.5,
            study_hours=2.0,
            mood="great",
            exam="Math",
        ),
    ]

    report = build_median_coffee_report(rows)

    assert report.headers == ("student", "median_coffee")
    assert len(report.rows) == 5

    assert report.rows[0] == ("C", 480.0)
    assert report.rows[1] == ("D", 400.0)
    assert report.rows[2] == ("B", 100.0)
    assert report.rows[3] == ("A", 15.0)
    assert report.rows[4] == ("E", 10.0)
