import functools, loady, traceback
from . import visitor

OBJECT = '_object'
CLASS = '_class'
ERROR = '_error'
TYPENAME = 'typename'
NOTHING = object()
ATTRIBUTES = 'CONTROLY_ATTRIBUTES'
RAISE = True


def fill(project):
    visitor.visit(project, _fill_class)
    visitor.visit(project, _construct)
    visitor.visit(project, _set_attributes)


def _errors(fn):
    @functools.wraps(fn)
    def wrapper(value, key, parent, **kwds):
        try:
            fn(value, key, parent, **kwds)
        except:
            if RAISE:
                raise

            error = fn.__name__, value, key, parent, traceback.format_exc()
            parent.setdefault(ERROR, []).append(error)

    return wrapper


@_errors
def _fill_class(value, key, parent):
    if key == TYPENAME:
        parent[CLASS] = loady.code.load_code(value)


@_errors
def _construct(value, key, parent):
    if key == CLASS:
        parent[OBJECT] = value()


@_errors
def _set_attributes(value, key, parent):
    if not parent or key == TYPENAME or (
            OBJECT not in parent or key.startswith('_')):
        return

    cls = parent[CLASS]

    attributes = getattr(cls, ATTRIBUTES, None)
    if not (attributes is None or key.startswith('_') or key in attributes):
        raise ValueError('Unknown attribute ' + key)

    if isinstance(attributes, dict):
        attr = attributes[key]
        if callable(attr):
            value = attr(value)

    setattr(parent[OBJECT], key, value)
