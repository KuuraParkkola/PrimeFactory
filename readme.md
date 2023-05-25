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
