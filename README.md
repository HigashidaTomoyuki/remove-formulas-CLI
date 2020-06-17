# remove-formulas-CLI
Remove formulas from Excel

## Installation
Install with the following command.
```bash
python setup.py install
```

If you want to uninstall, execute the following command.
```bash
python setup.py install --record files.txt
cat files.txt | xargs rm -rf
pip uninstall rmformulas -y
```

## Usage

### help
```bash
rmformulas --help
```

### remove formulas

```bash
rmformulas --input <input file or dir> --output <output dir>
```

#### Options

`--input, -i`: input file or directory name.


`--output, -o`: output directory name.
