#!/usr/bin/env python3
from pathlib import Path
import re,sys
p=Path(__file__).resolve().parents[1]
files=list(p.rglob('*.md')); errors=[]
s=(p/'SKILL.md').read_text()
if not s.startswith('---\n') or 'name: figma-product-design' not in s: errors.append('SKILL frontmatter')
for f in files:
 t=f.read_text()
 for x in re.findall(r'`((?:references|templates|scripts)/[^`\n]+)`',t):
  if not (p/x).exists(): errors.append(f'{f.name}: missing {x}')
 if not t.strip(): errors.append(f'{f.name}: empty')
print(f'Markdown files: {len(files)}; errors: {len(errors)}')
for e in errors: print('ERROR:',e)
sys.exit(bool(errors))
