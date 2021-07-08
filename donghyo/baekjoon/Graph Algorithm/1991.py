def pre_Order(start_node):
    if start_node == '.':
        return
    print(start_node, end="")
    pre_Order(tree[start_node][0])
    pre_Order(tree[start_node][1])


def in_Order(start_node):
    if start_node == '.':
        return
    in_Order(tree[start_node][0])
    print(start_node, end="")
    in_Order(tree[start_node][1])


def post_Order(start_node):
    if start_node == ".":
        return
    post_Order(tree[start_node][0])
    post_Order(tree[start_node][1])
    print(start_node, end="")


tree = {}
N = int(input())
for i in range(N):
    root_node, left_node, right_node = map(str, input().split())
    tree[root_node] = [left_node, right_node]

pre_Order('A')
print()
in_Order('A')
print()
post_Order('A')
