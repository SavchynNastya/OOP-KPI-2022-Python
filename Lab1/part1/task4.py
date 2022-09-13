import argparse


parser = argparse.ArgumentParser()

# add optional arguments
parser.add_argument("-W", "--capacity", type=int, default=10)  # ??
parser.add_argument("-w", "--weights",  type=int, nargs='*')
parser.add_argument("-n", "--bars_number", type=int)


def find_max_weight(capacity, weights):
    store = [[True] + [False] * capacity]
    for weight in range(len(weights)):
        store.append(store[-1][:])
        # print(f"STOREE: {store}")
        for w in range(weights[weight], capacity + 1):
            store[-1][w] = store[-2][w] or store[-2][w - weights[weight]]
            # print(f"stpre: {store}")
        store = store[-1:]
        # print(f"sTOREE: {store}")
    for w in range(capacity, -1, -1):
        if store[-1][w]:
            return w


args = parser.parse_args()
# print(args)

print(find_max_weight(args.capacity, args.weights))
