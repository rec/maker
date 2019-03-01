class Base:
    def __init__(self, **kwds):
        self.kwds = kwds


class DMXLevel(Base):
    pass


class AbsLFOFader(Base):
    pass


class Selector(Base):
    pass


class Button(Base):
    pass


class Toggle(Base):
    pass


class Counter(Base):
    pass


class Bang(Base):
    pass
