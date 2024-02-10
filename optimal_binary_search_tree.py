def optimal_bst(keys, freq):
    n = len(keys)

    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                c = cost[i][r - 1] if r > i else 0
                c += cost[r + 1][j] if r < j else 0
                c += sum(freq[i:j + 1])

                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root


def construct_bst(keys, root, i, j):
    if i > j:
        return None

    root_index = root[i][j]
    root_node = Node(keys[root_index])

    root_node.left = construct_bst(keys, root, i, root_index - 1)
    root_node.right = construct_bst(keys, root, root_index + 1, j)

    return root_node


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


if __name__ == "__main__":
    keys = [1,2,3,4,5,6]
    freq = [0.01,0.02,0.04,0.08,0.16,0.69]

    cost, root = optimal_bst(keys, freq)

    print("Optimal Binary Search Tree Cost Table:")
    for row in cost:
        print(row)

    print("\nOptimal Binary Search Tree Root Table:")
    for row in root:
        print(row)

    bst_root = construct_bst(keys, root, 0, len(keys) - 1)

    print("\nInorder Traversal of Optimal BST:")
    inorder_traversal(bst_root)