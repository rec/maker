import inspect, functools
from inspect import Parameter
ARGS = '_args'
KWDS = '_kwds'


KINDS = (
    Parameter.POSITIONAL_ONLY,
    Parameter.POSITIONAL_OR_KEYWORD,
    Parameter.VAR_POSITIONAL,
    Parameter.KEYWORD_ONLY,
    Parameter.VAR_KEYWORD,
)


class SignatureVerifier:
    def __init__(self, function):
        self.function
        self.by_kind = {k: [] for k in KINDS}

        self.parameters = inspect.signature(function).parameters

    def prepare_call(self, call_dict):
        errors, warnings = [], []
        cargs = list(call_dict.pop(ARGS, []))
        kwds = call_dict.pop(KWDS, {})

        po, pok, vp, ko, vk = (self.by_kind[k] for k in KINDS)
        if len(cargs) < len(po):
            errors.append(NOT_ENOUGH_PO % (len(po), len(cargs)))
        elif len(cargs) > len(po) + len(pok):
            errors.append(TOO_MANY_PO % (len(po) + len(po), len(cargs)))
        else:
            cargs = cargs[len(po):]

        return (
            errors, warnings, functools.partial(self.function, *cargs, **kwds))


NOT_ENOUGH_PO = 'Needed at least %d positional parameters, got %d'
TOO_MANY_PO = 'Needed at most %d positional parameters, got %d'
