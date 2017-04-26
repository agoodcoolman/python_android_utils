
from cf.touch import startTouch
from cf.touch import moveTouch
from cf.touch import endTouch
from cf.click import click

def main() :
    startTouch(10, 10)
    for num in range(102):

        moveTouch(20, num *20)

        if num == 10:
            click(320, 480)

    endTouch()

if __name__ == '__main__':
    main()