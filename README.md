# csv-to-json

[![Build Status](https://travis-ci.org/hex7c0/csv-to-json.svg?branch=master)](https://travis-ci.org/hex7c0/csv-to-json)

Build json file, from csv file matrix

## API

Run through bash

```bash
python3 ctj.py file.csv
```

### csv-to-json(options)

#### options

 - `csv` - **String** Csv path *(default "required")*
 - `-d`- **String** Delimiter for csv *(default ";")*
 - `-q` - **String** Quotechar for csv *(default """)*
 - `-s` - **Boolean** Sort csv with "row x column" *(default "column x row")*
 - `-j` - **String** Path of json file *(default "ctj.json")*
 - `-w`- **String** Wrapper for csv *(default "False")*
 - `-i` - **Integer** Indent for csv *(default "4")*
 - `-s` - **Boolean** Sort keys for json *(default "True")*
 - `-h`, `--help` - Show this help message and exit
 - `-v`, `--version` - Show program's version number and exit

## Examples

Take a look at my [examples](examples)

### [License GPLv3](LICENSE)
