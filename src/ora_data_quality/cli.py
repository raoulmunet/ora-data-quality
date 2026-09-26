from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import generate_rules

def main(argv=None):
    p=argparse.ArgumentParser(description="Generate Oracle data-quality rules from DDL.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json"),default="text")
    a=p.parse_args(argv)
    rules=generate_rules(Path(a.source).read_text(encoding="utf-8"))
    if a.format=="json":
        print(json.dumps([r.to_dict() for r in rules],indent=2))
    else:
        for r in rules:
            print(f"-- {r.confidence.upper()} {r.table}.{r.column}: {r.rationale}")
            print(r.sql)
            print()
    return 0
if __name__=="__main__": raise SystemExit(main())
