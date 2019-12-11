import itertools
from collections import Counter


def iter_rows(pixels, w):
    row = []
    for i, pixel in enumerate(pixels, 1):
        row.append(pixel)
        if i % w == 0:
            yield tuple(row)
            row = []


def iter_layers(pixels, w, h):
    layer = []
    for i, row in enumerate(iter_rows(pixels, w), 1):
        layer.append(row)
        if i % h == 0:
            yield layer
            layer = []


def part1():
    pixels = open('input.txt').read()
    data = []
    for layer in iter_layers(pixels, 25, 6):
        counter = Counter(itertools.chain(*layer))
        data.append((counter['0'], counter['1'], counter['2']))
    fewest_zeros, *_ = sorted(data)
    return fewest_zeros[1] * fewest_zeros[2]


def iter_pixels(layer):
    for pixel in itertools.chain(*layer):
        yield pixel


def calculate_final_pixels(pixels, w, h):
    _layers = list(iter_layers(pixels, w, h))
    layer_pixels = [iter_pixels(l) for l in _layers]

    pixels_in_image = []
    for row in range(w):
        pixels_in_row = []
        for col in range(h):
            for p in [next(l) for l in layer_pixels]:
                if p != '2': # first non-transparent pixel
                    break
            pixels_in_row.append(p)
        pixels_in_image.append(tuple(pixels_in_row))

    return pixels_in_image

def part2():
    pixels = open('input.txt').read()
    image = calculate_final_pixels(pixels, 6, 25)
    for row in image:
        print(''.join(row).replace('0', ' '))


if __name__ == '__main__':
    print(part1())
    print(part2())
