import click
import os
from openpyxl import load_workbook


@click.command()
@click.option(
    '--input', '-i', required=True, help=u"input file or directory name.")
@click.option(
    '--output', '-o', required=True, help=u"output directory name.")
def cli(input, output):
    """
    Receive Excel file name or directory name as input argument.
    Receive directory name in output argument.
    Remove the formula in the Excel file received in the input argument
    and save it in the directory received in the output argument.

    Parameters
    ----------
    input : str
        input file or directory name
    output : str
        output directory name
    """
    xlsx_filelist = []
    try:
        if os.path.isfile(input) and input.endswith(".xlsx"):
            xlsx_filelist.append(input)
        elif os.path.isdir(input):
            filelist = os.listdir(input)
            for _file in filelist:
                if not _file.endswith(".xlsx"):
                    continue
                xlsx_filelist.append(
                    os.path.join(input, _file))
            if len(xlsx_filelist) == 0:
                print("Excel file is not exists.")
                return
        else:
            print("output is illegal value.")
            return

        if not os.path.exists(output):
            os.makedirs(output)
        if not os.path.isdir(output):
            print("output is illegal value.")
            return

        for xlsx in xlsx_filelist:
            filename = os.path.basename(xlsx)
            output_path = os.path.join(output, filename)
            try:
                book = load_workbook(xlsx, data_only=True)
                book.save(output_path)
                print("Succeed convert " + filename)
            except Exception:
                print("Failed convert " + filename)

    except Exception as e:
        print("Unexpected error occured.")
        print(e)
