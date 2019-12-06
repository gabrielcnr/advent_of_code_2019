text_input = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

from day06 import build_graph, count_orbits

def test_traverse():
    nodes = build_graph(text_input)
    C = nodes['C']
    assert ['B', 'COM'] == [o.name for o in C.traverse()]

    L = nodes['L']
    assert ['K', 'J', 'E', 'D', 'C', 'B', 'COM'] == [o.name for o in L.traverse()]

    assert 42 == count_orbits(nodes)
    
