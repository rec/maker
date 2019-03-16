import itertools
from kivy.uix import boxlayout


class BoxLayout(boxlayout.BoxLayout):
    def add_all(self, *entries):
        is_vertical = self.orientation == 'vertical'

        total = 0
        items = []
        it = iter(entries)

        for item, weight in itertools.zip_longest(it, it):
            items.append(item)
            if weight is None:
                weight = 1 - total
            else:
                total += weight
            item.size_hint = (1, weight) if is_vertical else (weight, 1)

        for item in items:
            self.add_widget(item)
