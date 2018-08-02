import traceback


OBJECT = '_object'
CLASS = '_class'
ERROR = '_error'
TYPENAME = 'typename'
NOTHING = object()


def pre(node, key, parent, class_loader):
    if key == TYPENAME:
        try:
            parent[CLASS] = class_loader(node)
        except:
            parent[ERROR] = traceback.format_exc()


def fill_classes(class_loader):
    pass


def no_op(*args, **kwds):
    pass


def _call_optional_method(object, name, *args, default=no_op, **kwds):
    method = getattr(object, name, default)
    return method(*args, **kwds)
