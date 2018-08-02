import traceback


def simple_children(node):
    if isinstance(node, dict):
        return node.items()

    if isinstance(node, (tuple, list)):
        return enumerate(node)

    return ()


def no_visit(node, key, parent):
    pass


def visit(node, pre=no_visit, post=no_visit, children=simple_children, **kwds):
    def recurse(node, key, parent):
        pre(node, key, parent, **kwds)

        for child_key, child_node in children(node):
            recurse(child_node, child_key, node)

        post(node, key, parent, **kwds)

    recurse(node, '', None)
