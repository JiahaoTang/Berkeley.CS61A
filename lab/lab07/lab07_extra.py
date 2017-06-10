from lab07 import *

# Q6
def reverse_other(t):
    """Reverse the roots of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """

    """define a swap function that can reverse the root of branches"""
    def swap(lst):
        if len(lst) == 1:
            lst[0] = lst[0]
        elif len(lst) == 2:
            tempRoot = lst[0].root
            lst[0].root = lst[len(lst) - 1].root
            lst[len(lst) - 1].root = tempRoot
        elif len(lst) > 2:
            tempRoot = lst[0].root
            lst[0].root = lst[len(lst) - 1].root
            lst[len(lst) - 1].root = tempRoot
            swap(lst[1:len(lst) - 2])
    """the main function of reverse_other"""
    if t.branches == []:
        return t
    else:
        swap(t.branches)
        for branch in t.branches:
            for deepbranch in branch.branches:
                reverse_other(deepbranch)
# Q7
def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    if t.branches == []:
        t.root = t.root
        return t.root
    else:
        for branch in t.branches:
            cumulative_sum(branch)
        t.root = t.root + sum([branch.root for branch in t.branches])

# Q8
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print_link(link1)
    <9 <16> 25 36>
    """
    if link.rest == ():
        if isinstance(link.first, int):
            link.first = fn(link.first)
        elif isinstance(link.first, Link):
            deep_map_mut(fn, link.first)
    else:
        if isinstance(link.first, int):
            link.first = fn(link.first)
            deep_map_mut(fn, link.rest)
        elif isinstance(link.first, Link):
            deep_map_mut(fn, link.first)
            deep_map_mut(fn, link.rest)
    
# Q9
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    s = link.rest
    while s != link:
        s = s.rest
        if s == ():
            return False
    return True

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    s = link.rest
    while s != link:
        s = s.rest
        if s == ():
            return False
    return True
    """This question I cannot solve so I use the same solution. 
    The solution of the CS61A website use the double node, the
    fast one and the slow one. Maybe this is the more efficient
    solution. I have to learn more about efficiency"""
