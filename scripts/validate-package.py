#!/usr/bin/env python3
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[1]
md=list(root.rglob('*.md'))
errors=[]
s=(root/'SKILL.md').read_text()
if not s.startswith('---\n') or 'name: figma-product-design' not in s:errors.append('frontmatter')
for path in md:
 text=path.read_text()
 for target in re.findall(r'`((?:references|templates|examples|scripts)/[^`]+)`',text):
  if not (root/target).is_file():errors.append(f'{path.name}: missing {target}')
if errors:
 print('FAIL:',*errors,sep='\n- ');sys.exit(1)
print(f'PASS: {len(md)} markdown files; internal file references and frontmatter verified')
