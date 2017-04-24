# -*- coding:utf-8 -*-
import sys
import codecs
def is_chinese(s):
    if s.decode("gb2312") >= u'\u4e00' and s.decode("gb2312") <= u'\u9fa5':

        return True

    else:

        return False
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def main() :

    getdefaultencoding = sys.getdefaultencoding()
    codecs_open = codecs.open("C:\Users\Administrator\Desktop\log1.txt", "r", "utf-8-sig")
    # f = open("C:\Users\Administrator\Desktop\log1.txt", "r")
    write = codecs.open("C:\Users\Administrator\Desktop\log2.txt", 'w +')
    nationlist = range(200)
    readlines = codecs_open.readlines()
    # zu = "族".decode("utf-8").encode("gb2312")
    # print zu
    number = 0;
    for line in readlines:
       print line
       split = line.split(" ")
       # for i in range(len(split)):
       #     if split[i] == '':
       #         split.pop(i)

       for i in range(len(split)):
            if (split[i] != '') & (split[i] != "\r\n"):
                if is_number(split[i]) | split[i].startswith('0'.decode("utf-8").encode(getdefaultencoding)):   #number
                        number = i;
                        if split[i].startswith('0'.decode("utf-8").encode(getdefaultencoding)):
                            split[i] = split[i].replace('0', " ")
                else: # chinese
                    nationlist[int(split[number])] = split[i]
       print  nationlist
    print nationlist
    a  = ""
    for nation in range(len(nationlist)):
        if (nationlist[nation] != "") & (~(is_number(nationlist[nation]))) :
            # write.write("<item>"+ (str(nationlist[nation])).decode(getdefaultencoding).encode("utf-8")+ "</item>" + "\r\n")
                a += "<item>"+ nationlist[nation]+ "</item>" + "\r\n";

    print a


    # print nationlist.decode("utf-8").encode("gb2312")
           # if is_chinese(line):
       #     line = line.strip() + "|"
       #     find = line.find(zu)
       #     i = line.__len__()
       #     # line = line[:i - 2]
       #     write.write(line.decode("gb2312").encode("utf-8"))
       #     print line.decode("gb2312") , i , find
       # else:
       #     print "else"+line

    write.flush()
    write.close()
if __name__ == '__main__':
    main()