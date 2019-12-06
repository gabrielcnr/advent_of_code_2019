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
K)YOU
I)SAN
"""

from day06 import build_graph, count_orbits, count_transfers

def test_traverse():
    nodes = build_graph(text_input)
    C = nodes['C']
    assert ['B', 'COM'] == [o.name for o in C.traverse()]

    L = nodes['L']
    assert ['K', 'J', 'E', 'D', 'C', 'B', 'COM'] == [o.name for o in L.traverse()]

    assert 54 == count_orbits(nodes)





def test_count_transfers():
    nodes = build_graph(text_input)
    assert 4 == count_transfers(nodes, 'YOU', 'SAN')

    
