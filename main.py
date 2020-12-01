DEBUG = False
from itertools import groupby, product


def all_element_eq(l):
    if len(l) == 0: return True #Just for the convenience
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
            x = self.is_game_finished()
            if x: print(x); return
            print('BOARD:')
            print(self)
            print('-------')
            print('Available moves are:', self.available_moves())
            a, b = map(int,input('Enter valid move: ').split())
            self.move(a,b)
            # if not self.moved: print('You must have entered invalid move')
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
            if DEBUG:
                print('Trying to pour from empty')
            return False

        chunk = [list(g) for k, g in groupby(orig[::-1])][0]
        # print('Chunk', chunk)

        #assert(all_element_eq(chunk))
        dl = dest[-1] if len(dest) > 0 else -1

        if dl != chunk[0]:
            # print('colors are different')
            if free_space(dest) < len(chunk):
                if DEBUG:
                    print('Disallowed')
                return

            for _ in range(len(chunk)):
                self.__move(an, bn)

        # test color
        elif orig[-1] == dest[-1]:
            n = free_space(dest) if (free_space(dest) - len(chunk) < 0) else len(chunk)
            for _ in range(n):
                self.__move(an,bn)

    def is_game_finished(self):
        """
        :return: str, when true
        """
        if all(list(map(all_element_eq, self.beakers))):
            return "Won. All either empty or contain only one type"
        return False

    def simulate_move(self, a, b):
        cpi = self.__copy__()
        cpi.move(a,b)
        moved = cpi.moved
        del cpi
        return moved

    def available_moves(self):
        ava = []
        s = range(len(self.beakers))
        for x,y in product(s,s):
            if self.simulate_move(x,y):
                ava.append([x,y])
        return ava

    def __copy__(self):
        # It does not cover making the copy during the move
        # i.e the self.moved, but doing this on purpose now
        return Watersort(self.beaker_size, self.beakers.copy())

    def __repr__(self):
        return '\n'.join(list(map(str,self.beakers)))

def test0(w):
    # print(w)
    w.move(1,2)
    w.move(1,2)

def test1(w):
    w.move(1,2)
    w.move(2,0)

def test_bigger():
    b = [ [1] , [2,1,2], [2,1], [], [] ]
    w = Watersort(6, b, game_mode=False)
    w.move(1,2)
    w.move(0,0)
    w.is_game_finished()
    # print(w)
    # print(w.available_moves())


if __name__ == '__main__':
    b = [ [1] , [2,1,2], [2,1] ]
    w = Watersort(3, b, game_mode=True)
    # test0(w)
    # test_bigger()
    # assert (w.move(1,2))


