import os
def main() :
    file = open("C:\Users\Administrator\Desktop\\touch3.txt", "r")
    readlines = file.readlines()

    for line in readlines:
        os.system(line)


if __name__ == '__main__':
    main()