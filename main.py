# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Watersort:
    def __init__(self,beaker_size, beakers):
        """
        :param size: max size of the beaker
        :param beakers:
            2 dim array representing each beaker. No need to write zeros for empty 'cells'
        """
        self.beaker_size = beaker_size
        self.beakers = beakers

    def move(self,an, bn):
        """
        :param an: beaker to move from
        :param bn: beaker to move to
        :return: True if success, false otherwise == move disallowed
        """
        if len(self.beakers[an]) != 0 and len(self.beakers[bn]) != self.beaker_size:
            # test color
            if len(self.beakers[bn]) == 0:
                #TODO move
                self.beakers[bn].append(self.beakers[an].pop(-1))
                return True

            elif self.beakers[an][-1] == self.beakers[bn][-1]:
                self.beakers[bn].append(self.beakers[an].pop(-1))
                return True

        print('Move not allowed')
        return False

    def __repr__(self):
        return '\n'.join(list(map(str,self.beakers)))



if __name__ == '__main__':
    b = [ [1] , [2,1,2], [2,1] ]
    w = Watersort(3, b)
    print(w)
    w.move(0,2)
    print(w)
    w.move(1,2)

