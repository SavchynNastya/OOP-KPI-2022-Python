codes = {
        ("001", 1): 100,
        ("002", 2): 160,
        ("003", 3): 620,
        ("004", 4): 500,
        ("005", 5): 230,
        ("006", 6): 180,
        ("007", 7): 120,
        ("008", 8): 150,
        ("009", 9): 300,
        ("010", 10): 790
    }


def search_node(node, code_value):
    if node is None:
        return False
    if node.code == code_value:
        return True

    left_tree = search_node(node.left, code_value)
    if left_tree:
        return True

    right_tree = search_node(node.right, code_value)
    return right_tree


class BinaryTree:

    def __init__(self, code, qty):
        self.left = None
        self.right = None

        self.code = code
        self.price = next(v for k, v in codes.items() if self.code in k)
        self.quantity = qty

    def insert(self, code, qty):
        if not search_node(self, code):
            if int(code) < int(self.code):
                if self.left is None:
                    self.left = BinaryTree(code, qty)
                else:
                    self.left.insert(code, qty)
            elif int(code) > int(self.code):
                if self.right is None:
                    self.right = BinaryTree(code, qty)
                else:
                    self.right.insert(code, qty)
            else:
                self.code = code
        else:
            raise ValueError("This item is already added.")


def compute_cost(products):
    if products is None:
        return 0
    return products.price * products.quantity + compute_cost(products.left) + compute_cost(products.right)


def get_cost(products):
    print(f"Totally - {compute_cost(products)}$")


def main():
    tree = 0
    while True:
        try:
            order = input("Enter the code of product (001-010) and quantity you want to order or 'q' to stop: ")
            if order == "q" or order == 'Q':
                break
            else:
                code, quantity = order.split()

                if int(code) < 1 or int(code) > 10:
                    raise ValueError

                quantity = int(quantity)

                if not tree:
                    tree = BinaryTree(code, quantity)
                else:
                    tree.insert(code, quantity)

        except ValueError as e:
            if "not enough values to unpack" in str(e):
                print("Not enough arguments entered (should be 2)")
            elif "too many values" in str(e):
                print("Too many arguments entered (should be 2)")
            elif "invalid literal" in str(e):
                print("You should enter only integers")
            elif "item is already added" in str(e):
                print("This item is already added.")
            else:
                print("Invalid value entered, code should be in range of 001-010")

    get_cost(tree)


if __name__ == "__main__":
    main()
