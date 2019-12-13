from aoc19.day09.day09 import IntCode, read_input_program

class ArcadeGame:
    def run(self, program):
        L = []
        program = IntCode(program,
                          output=L.append)
        program.run()
        return L

    def build_tiles(self, output):
        assert len(output) % 3 == 0

        def iter_tiles(output):
            it = iter(output)
            while True:
                try:
                    x = next(it)
                    y = next(it)
                    tile_id = next(it)
                    yield((x, y, tile_id))
                except StopIteration:
                    break

        tiles = {(x, y): tile_id for x, y, tile_id in iter_tiles(output)}
        return tiles


def part1():
    from collections import Counter
    program = read_input_program()
    game = ArcadeGame()
    output = game.run(program)
    tiles = game.build_tiles(output)
    counter = Counter(tiles.values())
    return counter[2]


if __name__ == '__main__':
    print(part1())