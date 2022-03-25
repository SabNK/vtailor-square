# Windows
# install python https://youtu.be/i-MuSAwgwCU
# from the folder run cmd
# run the following code in cmd: pip install Pillow
# run from windows: idle
# open this file in idle
# change setup and run

from PIL import Image


class SquareMismatch(Exception):
    pass


class Square:
    def __init__(self, square_size, square_color,
                 square_offset=0, square_id=0):
        self.size = square_size
        self.color = square_color
        self.id = square_id
        self.offset = square_offset
        self.img = Image.new('RGB', (self.size, self.size), color=self.color)

    def square_paste(self, square, position=0):
        if not isinstance(square, Square) and square.size > self.size - self.offset:
            raise SquareMismatch('Inner square is too big to paste')
        if 0 <= position <= 3:
            x = divmod(position, int('10', base=2))[1] * (self.offset + square.size)
            y = divmod(position, int('10', base=2))[0] * (self.offset + square.size)
            self.img.paste(square.img, (x, y))
        else:
            raise SquareMismatch('Position is not correct')


class TestSquare:
    def __init__(self):
        self.sq = Square(200, 'red', 10)

    def test_init(self):
        self.sq.img.save('test_sq.png')

    def test_square_paste(self):
        inner = Square(70, 'green', 10)
        self.sq.square_paste(inner, 3)
        self.sq.img.save('test_sq_pasted.png')

# SetUp
offsets = [5, 10, 20, 25, 30, 35, 40, 45, 50,]# 55, 60, 65 , 70] #lenth of offsets should correspond with iterations
iterations = len(offsets)
min_square_size = 10
colors = [(255, 0, 0), '#ffff00', 'green', 'blue'] #colors might be https://stackoverflow.com/questions/54165439/what-are-the-exact-color-names-available-in-pils-imagedraw
filename = 'square.png'

# code
size = min_square_size
sq = Square(size, colors[0])
inners = [Square(size, colors[j]) for j in range(4)]

for i in range(iterations):
    size = inners[0].size * 2 + offsets[i]
    outers = [Square(size, colors[j], offsets[i]) for j in range(4)]
    [sq.square_paste(inners[j], j) for sq in outers for j in range(4)]
    inners = [sq for sq in outers]
offset = offsets[-1] + 5
size = inners[0].size * 2 + offset
sq = Square(size, colors[0], offset)
[sq.square_paste(inners[j], j) for j in range(4)]
sq.img.save(filename)

'''
if __name__== '__main__':
    TestSquare().test_init()
    TestSquare().test_square_paste()
'''