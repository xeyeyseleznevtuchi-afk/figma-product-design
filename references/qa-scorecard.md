# Evidence-based quality scorecard and release gate

Use N/A only with stated reason. Score each dimension 0=fail, 1=partial, 2=pass with evidence.

| Dimension | Evidence | Hard failure examples |
| --- | --- | --- |
| Intent and user goal | brief + task flow | required task impossible |
| Flow and recovery | state matrix + transitions | no errors/recovery |
| Visual direction | reference comparison screenshots | arbitrary brand/style drift |
| Typography/content | measured text bounds + screenshot | clipped text or placeholders |
| Responsive | viewport fixtures | inaccessible primary action |
| Component architecture | published component props + instances | duplicate primitives |
| Tokens/styles | bindings and scopes | false token linkage |
| Accessible design | contrast/target/focus checks | unreadable text, invisible focus |
| Scope protection | pre/post ID inventory | unexpected changes elsewhere |
| Handoff | known limits, behavior, links | undocumented dependency |

Block delivery on any zero for applicable dimension or on an unreviewed screenshot. A numerical score is supporting evidence, not a substitute for critical judgment. Do not falsely certify accessibility. Distinguish design QA from runtime implementation tests.
