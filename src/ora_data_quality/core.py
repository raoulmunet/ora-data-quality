from __future__ import annotations
from dataclasses import dataclass,asdict
import re
from ora_doc import parse_tables

@dataclass(frozen=True)
class Rule:
    table:str
    column:str
    kind:str
    rationale:str
    sql:str
    confidence:str
    def to_dict(self): return asdict(self)

def generate_rules(ddl:str)->list[Rule]:
    rules=[]
    for table in parse_tables(ddl):
        for col in table.columns:
            qtable=table.name
            qcol=col.name
            if not col.nullable:
                rules.append(Rule(qtable,qcol,"not_null","Column is declared NOT NULL.",
                    f"SELECT COUNT(*) AS violations FROM {qtable} WHERE {qcol} IS NULL;","deterministic"))
            if re.search(r"(^|_)EMAIL($|_)",qcol,re.I):
                rules.append(Rule(qtable,qcol,"email_shape","Column name suggests an email address.",
                    f"SELECT COUNT(*) AS violations FROM {qtable} WHERE {qcol} IS NOT NULL AND ({qcol} NOT LIKE '%@%' OR {qcol} LIKE '% %');","heuristic"))
            if re.search(r"(^|_)COUNTRY_CODE$",qcol,re.I):
                rules.append(Rule(qtable,qcol,"country_code_length","Column name suggests a two-character country code.",
                    f"SELECT COUNT(*) AS violations FROM {qtable} WHERE {qcol} IS NOT NULL AND LENGTH(TRIM({qcol})) <> 2;","heuristic"))
            if re.search(r"(^|_)(BIRTH|CREATED|UPDATED|START|END)_?DATE$",qcol,re.I) or qcol.endswith("_DATE"):
                rules.append(Rule(qtable,qcol,"date_future_review","Date-like column may require a future-date business rule; review semantics.",
                    f"SELECT COUNT(*) AS candidates FROM {qtable} WHERE {qcol} > SYSDATE;","heuristic"))
    return rules
