import sys
import argparse

print("This is the name of the script: ", sys.argv)


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=float, nargs=2,
                    help='an integer for the accumulator')
parser.add_argument('-s', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')


parser.add_argument('--foo', nargs=2)
parser.add_argument('bar', nargs=1)
print(parser.parse_args('c --foo a b'.split()))
# Namespace(bar=['c'], foo=['a', 'b'])

args = parser.parse_args()
print(args.accumulate(args.integers))