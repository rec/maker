OBJECT = '_object'
CLASS = '_class'
TYPENAME = 'typename'


def simple_children(node):
    if isinstance(node, dict):
        return node.items()

    if isinstance(node, (tuple, list)):
        return enumerate(node)

    return ()


def visit_none(node, key, parent):
    pass


def visit(node, pre=visit_none, post=visit_none, children=simple_children):
    def recurse(node, key, parent):
        pre(node, key, parent)

        for child_key, child_node in children(node):
            recurse(child_node, child_key, node)

        post(node, key, parent)

    recurse(node, '', None)
