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
