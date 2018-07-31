OBJECT = '_object'
CLASS = '_class'
TYPENAME = 'typename'


class Visitor:
    def __init__(self, desc, key='', parent=None):
        self.desc = desc
        self.key = key
        self.parent = parent

    def visit(self):
        self.pre()

        for child_key, child_desc in self.children():
            self.child(child_desc, child_key).visit()

        self.post()

    def pre(self):
        pass

    def post(self):
        pass

    def children(self):
        return ()

    def child(self, child_desc, child_key):
        return self.__class__(child_desc, child_key, self.desc)


class DictVisitor(Visitor):
    def children(self):
        if isinstance(self.desc, dict):
            return self.desc.items()
        if isinstance(self.desc, (tuple, list)):
            return enumerate(self.desc)
        return ()


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
