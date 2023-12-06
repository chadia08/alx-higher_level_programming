#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")

 # binary_tree_balance - A function that measures the balance factor of a
 # binary tree.
 # @tree: Pointer to root node to calculate balance factor.
 # Return: The balance factor of the tree.
 #
