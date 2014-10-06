# csv-to-json

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
 - `-j` - **String** Path of json file *(default "ctj.json")*
 - `-w`- **String** Wrapper for csv *(default "False")*
 - `-i` - **Integer** Indent for csv *(default "4")*
 - `-s` - **Boolean** Sort keys for json *(default "True")*
 - `-h`, `--help` - Show this help message and exit
 - `-v`, `--version` - Show program's version number and exit

## Examples

Take a look at my [examples](https://github.com/hex7c0/csv-to-json/tree/master/examples)

### [License GPLv3](http://opensource.org/licenses/GPL-3.0)
