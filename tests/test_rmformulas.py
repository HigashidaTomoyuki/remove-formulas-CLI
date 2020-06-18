import os
import pytest
import shutil
from rmformulas.rmformulas import cli
from openpyxl import load_workbook


def test_cli_illigal_input(runner):
    """
    Test for illigal input.

    Parameters
    ----------
    runner : click.testing.CliRunner
        Test for click object
    """
    input = "hogehoge.txt"
    output = "for_test_result"
    runner.invoke(cli, ['-i', input, '-o', output])
    assert not os.path.exists(output)


def test_cli_excel_not_exists(runner):
    """
    Test for excel file does not exist in input directory.

    Parameters
    ----------
    runner : click.testing.CliRunner
        Test for click object
    """
    input = "rmformulas"
    output = "for_test_result"
    runner.invoke(cli, ['-i', input, '-o', output])
    assert not os.path.exists(output)


def test_cli_illigal_output(runner, fixture_illigal_dir):
    """
    Test for illigal output.

    Parameters
    ----------
    runner : click.testing.CliRunner
        Test for click object
    fixture_illigal_dir : str
        Illigal directory path
    """
    input = "tests"
    output = fixture_illigal_dir
    output_path = os.path.join(output, "test.xlsx")
    runner.invoke(cli, ['-i', input, '-o', output])
    assert not os.path.exists(output_path)


def test_cli_broken_excel(runner, fixture_broken_excel):
    """
    Test for broken excel file input.

    Parameters
    ----------
    runner : click.testing.CliRunner
        Test for click object
    fixture_broken_excel : str
        Broken Excel path
    """
    input = fixture_broken_excel
    output = "for_test_result"
    output_path = "for_test_result/test.xlsx"
    runner.invoke(cli, ['-i', input, '-o', output])
    assert not os.path.exists(output_path)


@pytest.mark.parametrize(
    ("input"),
    [("tests"), ("tests/test.xlsx")]
)
def test_cli_normal(runner, input):
    """
    Test for normal pattern.

    Parameters
    ----------
    runner : click.testing.CliRunner
        Test for click object
    input : str
        Input argument
    """
    output = "for_test_result"
    output_path = "for_test_result/test.xlsx"
    cell_value = cell_value = {
        "A1": 2,
        "B1": 4,
        "C1": 6,
        "A2": 6,   # "=SUM(A1,B1)"
        "B2": 10,  # "=B1+C1"
        "C2": 8    # "=C1+A1"
    }
    runner.invoke(cli, ['-i', input, '-o', output])

    assert os.path.exists(output_path)
    book = load_workbook(output_path)
    sheet = book.active
    for cell in cell_value:
        assert sheet[cell].value == cell_value[cell]
    if os.path.exists(output):
        shutil.rmtree(output)


def test_cli_abnormal(runner):
    """
    Test for abnormal pattern.

    Parameters
    ----------
    runner : click.testing.CliRunner
        Test for click object
    """
    input = Exception
    output = "for_test_result"
    runner.invoke(cli, ['-i', input, '-o', output])
    assert not os.path.exists(output)
