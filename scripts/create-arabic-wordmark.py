#!/usr/bin/env python3
"""Shape the Arabic wordmark with an official local font; export vector outlines.
Requires HarfBuzz's hb-view (brew install harfbuzz). No font binary is copied.
Usage: python3 scripts/create-arabic-wordmark.py FONT.otf OUTPUT.svg
"""
import copy
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit(__doc__)
font, output = map(Path, sys.argv[1:])
svg = subprocess.check_output([
    'hb-view', '--direction=rtl', '--language=ar', '--font-size=100',
    '--margin=20', '--background=ffffff00', '--output-format=svg',
    str(font), 'مصطفى صابر',
])
ns = 'http://www.w3.org/2000/svg'
xlink = '{http://www.w3.org/1999/xlink}href'
source = ET.fromstring(svg)
defs = {item.attrib['id']: item for item in source.iter() if 'id' in item.attrib}
ET.register_namespace('', ns)
root = ET.Element(f'{{{ns}}}svg', {
    'viewBox': source.attrib['viewBox'], 'fill': 'currentColor', 'aria-hidden': 'true'
})
root.append(ET.Comment(' مصطفى صابر · Thmanyah Serif Display Medium · HarfBuzz-shaped outlines; no embedded font software. '))
count = 0
for use in source.iter(f'{{{ns}}}use'):
    glyph = defs[use.attrib[xlink].lstrip('#')]
    for original in glyph.iter(f'{{{ns}}}path'):
        path = copy.deepcopy(original)
        path.set('transform', f"translate({use.get('x', '0')} {use.get('y', '0')})")
        root.append(path)
        count += 1
if count < 8:
    raise SystemExit('Unexpected number of Arabic glyph outlines')
output.parent.mkdir(parents=True, exist_ok=True)
ET.ElementTree(root).write(output, encoding='unicode')
print(f'Exported {count} glyph outlines to {output}')
