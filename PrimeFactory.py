from argparse import ArgumentParser
from pathlib import Path
from source.database import load_data, save_data
from source.export_results import export_results
from source.factorize import factorize


if __name__ == '__main__':
    ##
    #   Define commandline interface
    #
    parser = ArgumentParser(
        prog="PrimeFactory",
        description="This program uses Pollard's Rho algorithm to find prime factors of a given number. Fermat's primality test is used in validation.",
    )
    parser.add_argument('number', default=None, type=int, help="The number to factorize")
    parser.add_argument('-o', '--output', type=Path, help="Output filename, defaults to 'output_[ISO datetime].txt'")
    parser.add_argument('-d', '--db', default='./database.json', type=Path, help="Path to the results database")
    parser.add_argument('-c', action='store_true', help="Ignore first primality test for guaranteed composite numbers. Increases performance \
                        significantly but runs indefinitely if number is a prime.", dest='isComposite')

    ##
    #   Define and validate program arguments
    #
    number = None
    number_str = None
    output_fl = None
    database_fl = None
    is_composite = False

    try:
        args = parser.parse_args()
        number = args.number
        output_fl = args.output
        database_fl = args.db
        number_str = str(number)
        is_composite = args.isComposite
    except SystemExit as err:
        #   Program ended correctly, -h option was likely used
        if err.code == 0:
            exit(0)

        #   If arguments were not given on the commandline, request number input
        print("Commandline arguments were not given, please give a number")
        while number is None:
            number_str = input(">> ")
            try:
                number = int(number_str)
            except ValueError:
                print("This number could not be interpreted, please enter a valid number")
                number = None
        database_fl = Path.cwd()/'database.json'
    
    ##
    #   Start the program
    #
    # Load the database
    data = load_data(database_fl)
    result = None
    
    # Seek the results database for existing results or perform factorization
    if number_str in data:
        # Existing results found, output results
        result = data[number_str]
        print("Result found in database:")
        print(f"Number {number} has prime factors {result['factors']}, which took {result['runtime']:.2f} seconds to find")
    else:
        # No existing results, run the algorithm and store the results in the database
        print(f"Seeking factors for number {number}")
        result = factorize(number, is_composite, on_match=lambda n: print(f"Prime factor found: {n}"))
        print(f"All primes found in {result['runtime']:.2f} seconds")
        data[int(number)] = result

    # Export the results and save the database
    export_results(output_fl, number, result)
    save_data(database_fl, data)
    