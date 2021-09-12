import builtins


def make_tree(buliding, x):
    mid = len(buliding) // 2
    binary_Tree[x].append(buliding[mid])

    if len(buliding) == 1:
        return

    make_tree(buliding[:mid], x+1) # 앞
    make_tree(buliding[mid+1:], x+1) # 뒤


if __name__ == "__main__":
    K = int(input())
    buliding = list(map(int, input().split()))
    binary_Tree = [[] for _ in range(K)]

    make_tree(buliding, 0)

    for i in binary_Tree:
        print(" ".join(map(str, i)))