import traceback


def simple_children(value):
    if isinstance(value, dict):
        return value.items()

    if isinstance(value, (tuple, list)):
        return enumerate(value)

    return ()


def no_visit(value, key, parent):
    pass


def visit(project, post=no_visit, pre=no_visit, children=simple_children,
          **kwds):
    def recurse(value, key, parent):
        pre(value, key, parent, **kwds)

        for child_key, child_value in list(children(value)):
            recurse(child_value, child_key, value)

        post(value, key, parent, **kwds)

    recurse(project, '', None)
