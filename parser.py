from argparse import ArgumentParser
from func import prod

def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="Simple Calculator")
    # Add argument
    parser.add_argument("numbers",type=int, nargs="+")
    # Boolean Argument
    parser.add_argument("-reverse", action='store_true')
    # Group of arguments, mutually exclusive
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-sum", dest="oper", action='store_const', const=sum)
    group.add_argument("-prod", dest="oper", action='store_const', const=prod)
    # Retrieve Arguments
    args = parser.parse_args()
    # Accessing different variables in args
    list_numbers = args.numbers
    operation = args.oper
    reverse = args.reverse
    
    return list_numbers, operation, reverse