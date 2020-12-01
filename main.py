DEBUG = True
from itertools import groupby


def all_element_eq(l):
    return all(x == l[0] for x in l)

class Watersort:
    def __init__(self,beaker_size, beakers, game_mode=False):
        """
        :param size: max size of the beaker
        :param beakers:
            2 dim array representing each beaker. No need to write zeros for empty 'cells'
        """
        self.beaker_size = beaker_size
        self.beakers = beakers
        self.moved = False

        if game_mode: self.game()

    def game(self):
        while True:
            print('BOARD:')
            print(self)
            print('-------')
            a, b = map(int,input('Enter valid move: ').split())
            self.move(a,b)
            if not self.moved: print('You must have entered invalid move')
            print('-------')

    def __move(self,an, bn):
        self.beakers[bn].append(self.beakers[an].pop(-1))
        self.moved = True

    def move(self,an, bn):
        """
        :param an: beaker to move from
        :param bn: beaker to move to
        :return: True if success, false otherwise == move disallowed
        """
        self.moved = False

        # Check index
        if any((an, bn)) > len(self.beakers) or any((an, bn)) < 0:
            if DEBUG:
                print('Wrong index')
            return False

        dest = self.beakers[bn]
        orig = self.beakers[an]

        free_space = lambda x: self.beaker_size - len(x)

        #Check if origin not empty
        if len(orig) == 0:
            print('Trying to pour from empty')
            return False

        chunk = [list(g) for k, g in groupby(orig[::-1])][0]
        # print('Chunk', chunk)

        #assert(all_element_eq(chunk))
        dl = dest[-1] if len(dest) > 0 else -1

        if dl != chunk[0]:
            # print('colors are different')
            if free_space(dest) < len(chunk):
                print('Disallowed')
                return

            for _ in range(len(chunk)):
                self.__move(an, bn)

        # test color
        elif orig[-1] == dest[-1]:
            n = free_space(dest) if (free_space(dest) - len(chunk)) else len(chunk)
            for _ in range(n):
                self.__move(an,bn)

    def __repr__(self):
        return '\n'.join(list(map(str,self.beakers)))

def test0(w):
    # print(w)
    w.move(1,2)
    w.move(1,2)

def test1(w):
    w.move(1,2)
    w.move(2,0)

if __name__ == '__main__':
    b = [ [1] , [2,1,2], [2,1] ]
    w = Watersort(3, b, game_mode=True)
    test0(w)
    print(w)
    # assert (w.move(1,2))


