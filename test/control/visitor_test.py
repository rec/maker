import unittest
from control import visitor


class VisitorTest(unittest.TestCase):
    maxDiff = 10000

    def test_all(self):
        results = []

        class Visitor(visitor.DictVisitor):
            def pre(self):
                results.append(('pre', self.name, self.desc))

            def post(self):
                results.append(('post', self.name, self.desc))

        Visitor(DATA).visit()
        print(*results, sep=',\n    ')
        self.assertEquals(results, EXPECTED)


DATA = {
    'foo': 'bar',
    'baz': [0, True, None, 3.5],
    'bing': {
        'bong': {}
    }
}

EXPECTED = [
    ('pre', '', DATA),
    ('pre', 'foo', 'bar'),
    ('post', 'foo', 'bar'),
    ('pre', 'baz', [0, True, None, 3.5]),
    ('pre', 0, 0),
    ('post', 0, 0),
    ('pre', 1, True),
    ('post', 1, True),
    ('pre', 2, None),
    ('post', 2, None),
    ('pre', 3, 3.5),
    ('post', 3, 3.5),
    ('post', 'baz', [0, True, None, 3.5]),
    ('pre', 'bing', {'bong': {}}),
    ('pre', 'bong', {}),
    ('post', 'bong', {}),
    ('post', 'bing', {'bong': {}}),
    ('post', '', DATA)
]
