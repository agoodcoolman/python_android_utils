# -*- coding:utf-8 -*-
import sys


def main():
    getfilesystemencoding = sys.getfilesystemencoding()
    f = open("C:\Users\Administrator\Desktop\log.txt")
    write = open("C:\Users\Administrator\Desktop\log1.txt", 'w +')

    a1 = ""
    find_ = ""
    try:
        readlines = f.readlines()
        for line in readlines:
            find = line.find("[")
            print find
            if find > 0:
                print a1.decode("utf-8").encode(getfilesystemencoding)

                print "结果=" + find_.decode("gb2312").encode(getfilesystemencoding)

                for x in a1:
                    if  ((x != " ") & (a1 != " ")) :
                        print "结果" + a1.decode("gb2312").encode(getfilesystemencoding)
                        write.write("<item>" + find_ + x +"</item> \n")
                        a1 = ""
                        write.flush()

                find_ = line[find + 1: find + 3]

            else:
                a1 += " ".join([x for x in line if x.isalpha()])
                print "结果" + a1.decode("gb2312").encode(getfilesystemencoding)

        for x in a1:
            if  ((x != " ") & (a1 != " ")) :
                print "结果" + a1.decode("gb2312").encode(getfilesystemencoding)
                write.write("<item>" + find_ + x +"</item> \n")
                a1 = ""
                write.flush()
    finally:
        f.close()
        write.close()

if __name__ == '__main__':
    main()