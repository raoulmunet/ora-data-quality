from ora_data_quality import generate_rules

DDL="""CREATE TABLE customer (
  customer_id NUMBER NOT NULL,
  email VARCHAR2(200),
  country_code CHAR(2)
);"""

def test_rules():
    rules=generate_rules(DDL)
    assert any(r.kind=="not_null" and r.column=="CUSTOMER_ID" for r in rules)
    assert any(r.kind=="email_shape" for r in rules)
    assert any(r.kind=="country_code_length" for r in rules)
