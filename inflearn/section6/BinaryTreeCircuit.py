# 전위 순회
def preorder_traversal(v: int):
    if v > 7:
        return
    print(v, end=" ")
    preorder_traversal(v * 2)
    preorder_traversal(v * 2 + 1)


# 중위 순회
def inorder_traversal(v: int):
    if v > 7:
        return
    inorder_traversal(v * 2)
    print(v, end=" ")
    inorder_traversal(v * 2 + 1)


# 후위 순회
def postorder_traversal(v: int):
    if v > 7:
        return
    postorder_traversal(v * 2)
    postorder_traversal(v * 2 + 1)
    print(v, end=" ")


print("전위순회 출력:", end=" ")
preorder_traversal(1)
print()

print("중위순회 출력:", end=" ")
inorder_traversal(1)
print()

print("후위순회 출력:", end=" ")
postorder_traversal(1)
print()
