import itertools


def lb(arr):
    cs = list(cumsum(arr))
    for idx1, idx2 in itertools.combinations(range(len(arr)), 2):
        idx1, idx2 = sorted([idx1, idx2])
        try:
            sum_1 = cs[idx1 - 1]
            sum_2 = cs[idx2] - cs[idx1 + 1]
            sum_3 = cs[-1] - cs[idx2]
        except IndexError:
            continue
        if sum_1 == sum_2 == sum_3:
            return idx1, idx2


def cumsum(arr):
    sum = 0
    for number in arr:
        sum += number
        yield sum


def test_lb():
    in_ = [1, 3, 4, 2, 2, 2, 1, 1, 2]
    assert (2, 5) == lb(in_)
