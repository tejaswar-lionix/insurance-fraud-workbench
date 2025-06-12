"""Tests for graph edge distinct"""

def test_graph_edge_0():
    from apps.graph.models import GraphEntity
    g=GraphEntity()
    graph=g.build_graph_0([{"id":"c1","claimant":"John","vehicle":"V1"}])
    assert "John" in graph or "c1" in graph

def test_graph_edge_1():
    from apps.graph.models import GraphEntity
    g=GraphEntity()
    graph=g.build_graph_1([{"id":"c1","claimant":"John","vehicle":"V1"}])
    assert "John" in graph or "c1" in graph

def test_graph_edge_2():
    from apps.graph.models import GraphEntity
    g=GraphEntity()
    graph=g.build_graph_2([{"id":"c1","claimant":"John","vehicle":"V1"}])
    assert "John" in graph or "c1" in graph

def test_graph_edge_3():
    from apps.graph.models import GraphEntity
    g=GraphEntity()
    graph=g.build_graph_3([{"id":"c1","claimant":"John","vehicle":"V1"}])
    assert "John" in graph or "c1" in graph
