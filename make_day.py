import sys
import os

if __name__ == '__main__':
    day = int(sys.argv[1])
    dirname = 'day%02d' % day
    os.mkdir(dirname)
    open(os.path.join(dirname, 'input.txt'), 'w')
    open(os.path.join(dirname, f'{dirname}.py'), 'w')
    open(os.path.join(dirname, f'test_{dirname}.py'), 'w')
