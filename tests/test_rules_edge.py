"""Tests for rules edge distinct"""

def test_rules_edge_0():
    from apps.rules.models import RulesEntity
    r=RulesEntity()
    res=r.rule_explainable_0({"staged_score":0.9,"repeat_2y":3,"shell_score":0.8})
    assert "flag" in res and "reason" in res

def test_rules_edge_1():
    from apps.rules.models import RulesEntity
    r=RulesEntity()
    res=r.rule_explainable_1({"staged_score":0.9,"repeat_2y":3,"shell_score":0.8})
    assert "flag" in res and "reason" in res

def test_rules_edge_2():
    from apps.rules.models import RulesEntity
    r=RulesEntity()
    res=r.rule_explainable_2({"staged_score":0.9,"repeat_2y":3,"shell_score":0.8})
    assert "flag" in res and "reason" in res

def test_rules_edge_3():
    from apps.rules.models import RulesEntity
    r=RulesEntity()
    res=r.rule_explainable_3({"staged_score":0.9,"repeat_2y":3,"shell_score":0.8})
    assert "flag" in res and "reason" in res
