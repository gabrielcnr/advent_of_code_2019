class N:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name

    __repr__ = __str__

    def traverse(self):
        o = self
        while o.name != 'COM':
            o = o.parent
            yield o


def build_graph(text_input):
    text_input = text_input.strip()
    nodes = {'COM': N('COM', None)}
    for line in text_input.splitlines():
        line = line.strip()
        left, right = line.split(')')

        if left not in nodes:
            left = N(left, None)
            nodes[left.name] = left
        else:
            left = nodes[left]

        if right in nodes:
            right = nodes[right]
            right.parent = nodes[left.name]
        else:
            right = N(right, left)  # the right orbits the left
            nodes[right.name] = right
    
    return nodes


def count_orbits(nodes):
    return sum(len(list(o.traverse())) for o in nodes.values())


def count_transfers(nodes, origin, dest):
    origin = nodes[origin]
    dest = nodes[dest]
    p1 = origin.parent
    p2 = dest.parent
    p1_path = list(p1.traverse())
    p2_path = list(p2.traverse())

    for node in p1_path:
        if node in p2_path:
            break
    join_node = node

    steps_from_p1 = p1_path.index(node) + 1
    steps_from_p2 = p2_path.index(node) + 1
    return steps_from_p1 + steps_from_p2
    

def part1():
    text_input = open('input.txt').read()
    nodes = build_graph(text_input)
    return count_orbits(nodes)

def part2():
    text_input = open('input.txt').read()
    nodes = build_graph(text_input)
    return count_transfers(nodes, 'YOU', 'SAN')



if __name__ == '__main__':
    print(part1())
    print(part2())