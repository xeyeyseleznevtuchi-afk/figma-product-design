#!/usr/bin/env python3
"""Validate a project artifact manifest. Stdlib only; exit 1 on invalid graph."""
import json,sys
from pathlib import Path
VALID={'PRODUCT','ENTITY','TASK','FLOW','SCREEN','CONTENT','VISUAL','TOKEN','COMPONENT','PATTERN','TEMPLATE','FIXTURE','QA'}
STATES={'proposed','reviewed','approved'}
def validate(data):
    issues=[]; arts=data.get('artifacts',[])
    if not isinstance(arts,list):return ['artifacts must be a list']
    ids=[x.get('id') for x in arts if isinstance(x,dict)]
    if len(ids)!=len(set(ids)):issues.append('duplicate artifact IDs')
    idx={x.get('id'):x for x in arts if isinstance(x,dict)}
    for x in arts:
        if not isinstance(x,dict):issues.append('artifact must be object');continue
        n=x.get('id')
        if not isinstance(n,str) or not n:issues.append('missing artifact id')
        if x.get('kind') not in VALID:issues.append(f'{n}: unknown kind')
        if x.get('status') not in STATES:issues.append(f'{n}: unknown status')
        if not x.get('revision'):issues.append(f'{n}: missing revision')
        if not x.get('source'):issues.append(f'{n}: missing provenance')
        deps=x.get('dependsOn',[])
        if not isinstance(deps,list):issues.append(f'{n}: dependsOn must be list');continue
        for d in deps:
            if d not in idx:issues.append(f'{n}: dangling reference {d}')
    # Only construction graph cycles are prohibited.
    active=set();done=set()
    def visit(n):
        if n in active:issues.append(f'cycle at {n}');return
        if n in done:return
        active.add(n)
        for d in idx[n].get('dependsOn',[]):
            if d in idx:visit(d)
        active.remove(n);done.add(n)
    for n in idx:visit(n)
    for x in arts:
        if isinstance(x,dict) and x.get('kind')=='SCREEN':
            kinds={idx[d].get('kind') for d in x.get('dependsOn',[]) if d in idx}
            for needed in ('FLOW','TEMPLATE','CONTENT'):
                if needed not in kinds:issues.append(f"{x.get('id')}: missing {needed} dependency")
    return issues
if __name__=='__main__':
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'templates'/'contract-manifest.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    problems=validate(data)
    for problem in problems:print('FAIL:',problem)
    if problems:sys.exit(1)
    print(f"PASS: {len(data['artifacts'])} artifacts; references and graph valid")
