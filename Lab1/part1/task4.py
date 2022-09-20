import argparse


def to_int(num_str):
    try:
        numbers = list(map(int, num_str))
        return numbers
    except ValueError:
        print(f"Wrong value type - {num_str}")


def find_max_weight(capacity, weights, n):
    knapsack = [[0 for val in range(capacity + 1)] for val in range(n + 1)]
    for i in range(n + 1):
        for c in range(capacity + 1):
            if not i or not c:
                knapsack[i][c] = 0
            elif weights[i-1] <= c:
                knapsack[i][c] = max(weights[i-1] + knapsack[i-1][c-weights[i-1]],
                                     knapsack[i-1][c])
            else:
                knapsack[i][c] = knapsack[i-1][c]
    return knapsack[n][capacity]

def main():

    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-W", "--capacity", type=str, nargs='*', default=None)
    parser.add_argument("-w", "--weights",  type=str, nargs='*', default=None)
    parser.add_argument("-n", "--bars_number", type=str, nargs='*', default=None)

    args = parser.parse_args()

    try:
        if not args.bars_number or not args.weights or not args.capacity \
                or len(args.capacity) != 1 or len(args.bars_number) != 1:
            raise TypeError
        else:
            args.capacity = to_int(args.capacity)
            args.weights = to_int(args.weights)
            args.bars_number = to_int(args.bars_number)

            if args.bars_number[0] != len(args.weights):
                raise IndexError

            print(find_max_weight(args.capacity[0], args.weights, args.bars_number[0]))

    except TypeError:
        print("Wrong number of arguments")
    except IndexError:
        print("Number of bars you entered is wrong")


if __name__ == "__main__":
    main()
