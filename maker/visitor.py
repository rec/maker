OBJECT = '_object'
CLASS = '_class'
TYPENAME = 'typename'


class Visitor:
    def __init__(self, desc, name='', parent=None):
        self.desc = desc
        self.name = name
        self.parent = parent

    def visit(self):
        self.pre()

        for child_name, child_desc in self.children():
            self.child(child_desc, child_name).visit()

        self.post()

    def pre(self):
        pass

    def post(self):
        pass

    def children(self):
        return ()

    def child(self, child_desc, child_name):
        return self.__class__(child_desc, child_name, self.desc)


class DictVisitor(Visitor):
    def children(self):
        if isinstance(self.desc, dict):
            return self.desc.items()
        if isinstance(self.desc, (tuple, list)):
            return enumerate(self.desc)
        return ()
