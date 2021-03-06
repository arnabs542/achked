#!/usr/bin/env python3

from tree_creation import *

def pushleft(node, st):
    while node:
        if node.right:
            st.append(node.right)
        st.append(node)
        node = node.left

def post_iter(root):
    st = []
    node = root

    pushleft(node, st)

    while st:
        node = st.pop(-1)

        if st:
            nxt_node = st[-1]
        else:
            nxt_node = None

        if not node.right and not node.left:
            print(node.data, end = ' ')
        elif node.right == nxt_node:
            # 
            st.pop(-1)
            st.append(node)
            pushleft(nxt_node, st)
        else:
            print(node.data, end = ' ')
    print()

def pre_order(root):
    node = root
    st = []
    st.append(node)

    while st:
        node = st.pop(-1)
        print(node.data, end = ' ')

        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)

    print()

def pushleft_only(node, st):
    while node:
        st.append(node)
        node = node.left

def inorder_iter(root):
    st = []
    node = root
    pushleft_only(node, st)

    while st:
        node = st.pop(-1)
        print(node.data, end = ' ')
        if node.right:
            pushleft_only(node.right, st)
    print()

def main():
    l = [10, 6, 9, 8, 7, 11, 13, 12]
    root = create_tree(l)
    print_level_tree(root)
    print("Postorder traversal: ", end = '')
    post_iter(root)
    print("Preorder traversal:  ", end = '')
    pre_order(root)
    print("Inorder traversal:  ", end = '')
    inorder_iter(root)

if __name__ == '__main__':
    main()

