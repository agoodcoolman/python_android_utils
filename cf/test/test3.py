
from cf.touch import startTouch
from cf.touch import moveTouch
from cf.touch import endTouch


def main() :
    startTouch(10, 10)
    for num in range(102):
        moveTouch(20, num *20)
    endTouch()

if __name__ == '__main__':
    main()