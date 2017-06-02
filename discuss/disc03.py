def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def square_tree(t):
    t[0] = t[0] * t[0]
    for branch in branches(t):
        square_tree(branch)
    return t

def tree_height(t):
    def height_measure(x, height,height_number=0):
        if is_leaf(x):
            height.append(height_number)
        else:
            height_number += 1
            for branch in branches(x):
                height_measure(branch, height, height_number)
        return max(height)
    height = []
    return height_measure(t,height)

def tree_max(t):
    def find_max_node(x):
        node.append(root(x))
        for branch in branches(x):
            find_max_node(branch)
        return max(node)
    node = []
    return find_max_node(t)

def fast_tree_max(t):
    if root(t) >= max_node:
        max_node = root(t)
    for branch in branches(t):
        fast_tree_max(branch)
    return max_node
