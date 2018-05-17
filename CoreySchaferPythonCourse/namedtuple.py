# namedtuple.py
# based on http://www.youtube.com/watch?v=GfxJYp9_nJA&t=6s

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(red=55, green=155, blue=255)

print(color[2])
print(getattr(color, 'green'))
print color.red

print('\n')
# tuples are inmutables! dicts are mutables... that's why better in this case to use namedtuple.

white = Color(255,255,255)
print(white)
