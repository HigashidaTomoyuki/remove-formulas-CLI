[![PyPI version](https://badge.fury.io/py/rmformulas.svg)](https://badge.fury.io/py/rmformulas)
[![codecov](https://codecov.io/gh/HigashidaTomoyuki/remove-formulas-CLI/branch/master/graph/badge.svg?token=GVS7ZL920C)](https://codecov.io/gh/HigashidaTomoyuki/remove-formulas-CLI)

# remove-formulas-CLI
Remove formulas from Excel

## Installation
Install with the following command.
```bash
pip install rmformulas
```

If you want to uninstall, execute the following command.
```bash
pip uninstall -y rmformulas
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

#### Warning
If you specify the same directory for input and output, the original Excel file will be overwritten.

#### Options

`--input, -i` : input file or directory name.


`--output, -o` : output directory name.
