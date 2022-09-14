import argparse

parser = argparse.ArgumentParser()

# add optional arguments
parser.add_argument("-W", "--capacity", type=int)
parser.add_argument("-w", "--weights",  type=int, nargs='*')
parser.add_argument("-n", "--bars_number", type=int)


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

# def find_max_weight(capacity, weights):
    # store = [[True] + [False] * capacity]
    # for weight in range(len(weights)):
    #     store.append(store[-1][:])
    #     for w in range(weights[weight], capacity + 1):
    #         store[-1][w] = store[-2][w] or store[-2][w - weights[weight]]
    #     store = store[-1:]
    # for w in range(capacity, -1, -1):
    #     if store[-1][w]:
    #         return w


args = parser.parse_args()
# print(args)

print(find_max_weight(args.capacity, args.weights, args.bars_number))
