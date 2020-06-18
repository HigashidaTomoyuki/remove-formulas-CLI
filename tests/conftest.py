import os
import pytest
import shutil
from click.testing import CliRunner


@pytest.fixture(scope="module")
def runner():
    """
    Return CliRunner.

    Returns
    ------
    runner : click.testing.CliRunner
        Test for click object
    """
    return CliRunner()


@pytest.fixture(scope="function", autouse=False)
def fixture_illigal_dir():
    """
    A fixture that creates an illigal directory.

    Yields
    ------
    tmp_test_path : str
        Illigal directory path
    """
    tmp_test_dir = "for_test"
    tmp_test_file = "test"
    tmp_test_path = os.path.join(tmp_test_dir, tmp_test_file)
    if os.path.exists(tmp_test_dir):
        shutil.rmtree(tmp_test_dir)
    os.makedirs(tmp_test_dir)
    with open(tmp_test_path, "w") as f:
        f.write("test")
    yield tmp_test_path
    if os.path.exists(tmp_test_dir):
        shutil.rmtree(tmp_test_dir)


@pytest.fixture(scope="function", autouse=False)
def fixture_broken_excel():
    """
    A fixture that creates a broken Excel.

    Yields
    ------
    tmp_test_path : str
        Broken Excel path
    """
    tmp_test_dir = "for_test"
    tmp_test_file = "test.xlsx"
    tmp_test_path = os.path.join(tmp_test_dir, tmp_test_file)
    if os.path.exists(tmp_test_dir):
        shutil.rmtree(tmp_test_dir)
    os.makedirs(tmp_test_dir)
    with open(tmp_test_path, "w") as f:
        f.write("test")
    yield tmp_test_path
    if os.path.exists(tmp_test_dir):
        shutil.rmtree(tmp_test_dir)
