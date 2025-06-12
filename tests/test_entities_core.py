"""Tests for entities core distinct"""

def test_entities_core_0():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_0("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1

def test_entities_core_1():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_1("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1

def test_entities_core_2():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_2("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1

def test_entities_core_3():
    from apps.entities.models import EntitiesEntity
    e=EntitiesEntity()
    score=e.resolve_3("John Smith","J. Smith","1990-01-01","1990-01-01")
    assert 0 <= score <= 1
