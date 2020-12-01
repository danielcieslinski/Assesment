DEBUG = True

class Watersort:
    def __init__(self,beaker_size, beakers):
        """
        :param size: max size of the beaker
        :param beakers:
            2 dim array representing each beaker. No need to write zeros for empty 'cells'
        """
        self.beaker_size = beaker_size
        self.beakers = beakers

    def __move(self,an, bn):
        self.beakers[bn].append(self.beakers[an].pop(-1))
        return True

    def move(self,an, bn):
        """
        :param an: beaker to move from
        :param bn: beaker to move to
        :return: True if success, false otherwise == move disallowed
        """
        if any((an,bn)) > len(self.beakers) or any((an,bn)) < 0:
            if DEBUG:
                print('Wrong index')
            return False

        if len(self.beakers[an]) != 0 and len(self.beakers[bn]) != self.beaker_size:
            # test if the destination in empty
            if len(self.beakers[bn]) == 0:
                return self.__move(an,bn)

            # test color
            elif self.beakers[an][-1] == self.beakers[bn][-1]:
                return self.__move(an,bn)

        if DEBUG:
            print('Move not allowed')
        return False

    def __repr__(self):
        return '\n'.join(list(map(str,self.beakers)))



if __name__ == '__main__':
    b = [ [1] , [2,1,2], [2,1] ]
    w = Watersort(3, b)
    # print(w)
    # w.move(,1)
    # assert (w.move(1,2))

    print(w)

