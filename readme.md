# PrimeFactory
This project is my implementation of the task "primenumbers" in the job application process for VALA. This program seeks unique prime number factors of a given number leveraging Pollard's Rho factorization algorithm and Fermat's primality test.

## Usage
After cloning the repository, go to the directory containing the file `PrimeFactory.py`. The program is run on the commandline as follows:

__usage__: python PrimeFactory.py [-h] [-o OUTPUT] [-d DB] number

### _positional arguments_

  __number__
  The number to factorize

### _options_

  __-h, --help__
  show help message and exit

  __-o OUTPUT, --output OUTPUT__
  Output filename, defaults to 'output\_[ISO datetime].txt'

  __-d DB, --db DB__
  Path to the results database

  __-c__
  Ignore first primality test for guaranteed composite numbers. Increases performance significantly but runs indefinitely if number is a prime.

## Examples
python PrimeFactory.py 26541
_Finds factors for the number 26541_

python PrimeFactory.py -c 2654135
_Finds factors, ignores some initial checks for faster performance_

python PrimeFactory.py -o ./my_output.txt 265413
_Finds factors, stores outputs to the file ./my\_output.txt instead of the default_

python PrimeFactory.py -d ./my_db.json 26541
_Finds factors, seeks existing results from a database file at ./my\_db.json_
