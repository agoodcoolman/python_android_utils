import os
def main() :

    file = open("C:\Users\Administrator\Desktop\\touch1.txt", "r")
    readlines = file.readlines()
    wfile = open("C:\Users\Administrator\Desktop\\test1.txt", "w")
    count = 0;
    for line in readlines:
        split = line.replace(":", "").split(" ")
        split[1] = int("0x"+split[1], 16)
        split[2] = int("0x"+split[2], 16)
        split[3] = int("0x"+split[3], 16)

        line = "adb shell sendevent "+ split[0] + " " + str(split[1]) + " " + str(split[2]) + " " + str(split[3]) + "\r\n";
        readlines[count] = line
        count += 1;
        # os.system(line.replace("\r\n", ""))
        print line
    wfile.writelines(readlines)
    wfile.flush();
    wfile.close()
    # cmdfile = open("C:\Users\Administrator\Desktop\click.txt", "r")
    # cmdline = cmdfile.readlines()
    # for line in cmdline:
    #     os.system(line.replace("\r\n", ""))
if __name__ == '__main__':
    main()