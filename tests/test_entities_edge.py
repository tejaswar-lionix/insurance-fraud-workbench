"""Tests for entities edge distinct"""

def test_entities_edge_0():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_0("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1

def test_entities_edge_1():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_1("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1

def test_entities_edge_2():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_2("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1

def test_entities_edge_3():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_3("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1
