from collections import Counter

def solution(word):
    counter = Counter(word)
    odds = sum(1 for count in counter.values() if count % 2)
    return odds


def test_():
    assert 1 == solution('acbcbba')
    assert 2 == solution('axxaxa')
    assert 0 == solution('aaaa')
