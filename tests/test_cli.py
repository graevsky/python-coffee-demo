from pathlib import Path

import pytest

from src.cli import main


def test_cli_prints_table_for_median_coffee(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    math_file = tmp_path / "math.csv"
    physics_file = tmp_path / "physics.csv"

    math_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Аня,2024-06-01,10,8,3,ok,Math\n"
        "Аня,2024-06-02,30,7,4,ok,Math\n"
        "Борис,2024-06-01,100,5,8,tired,Math\n",
        encoding="utf-8",
    )
    physics_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Аня,2024-06-03,50,6,5,tired,Physics\n"
        "Борис,2024-06-02,0,9,1,ok,Physics\n",
        encoding="utf-8",
    )

    code = main(
        [
            "--files",
            str(math_file),
            str(physics_file),
            "--report",
            "median-coffee",
        ]
    )
    assert code == 0

    out = capsys.readouterr().out
    assert "student" in out
    assert "median_coffee" in out

    assert "| Борис" in out
    assert "| Аня" in out

    assert "50" in out
    assert "30" in out

    assert out.index("| Борис") < out.index("| Аня")


def test_cli_errors_on_unknown_report(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    data_file = tmp_path / "data.csv"
    data_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Аня,2024-06-01,10,8,3,ok,Math\n",
        encoding="utf-8",
    )

    with pytest.raises(SystemExit) as exc_info:
        main(["--files", str(data_file), "--report", "unknown"])

    assert exc_info.value.code == 2

    err = capsys.readouterr().err
    assert "Unsupported report: unknown" in err
    assert "median-coffee" in err


def test_cli_errors_on_missing_file(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    missing = tmp_path / "nope.csv"

    with pytest.raises(SystemExit) as exc_info:
        main(["--files", str(missing), "--report", "median-coffee"])

    assert exc_info.value.code == 2

    err = capsys.readouterr().err
    assert f"File not found: {missing}" in err
