import os
global resutl
resutl = ""
def fa(file_dir):
    global resutl

    list = os.listdir(file_dir)
    for i in range(0, len(list)):
        path = os.path.join(file_dir, list[i])
        if os.path.isfile(path):
            djfeojo = path.replace("C:\\Users\\Administrator\\Desktop\\jiaojie\\asio-1.10.8\\include\\", "").replace("\\", "/")
            resutl += "src/main/cpp/" + djfeojo + " \r\n"
        else:
            fa(path)


def haode(rootdir):
    global resutl
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
                # resutl += (path.replace("E:\C_library\\boost_1_63_0\\boost", "src/main/cpp/boost") + "\r\n").replace("\\", "/")
                f = open(path, "r")
                readlines = f.readlines()
                count = 0;
                for line in readlines:
                    if ("#include" in line ) & ("asio" in line):
                        readlines[count] = line.replace("asio/", "/asio/")
                        # line = line.replace(">", "\"").replace("<", "\"").replace("boost/", "")
                        # line = line.replace("boost", "/boost")
                        # readlines[count] = ("#include \"" +line.split('/')[-1] + "\"").replace("\n", "").replace(">", "") + "\r\n"
                        # readlines[count] = line
                        # readlines[count] = line.replace("boost", "/boost")
                    count += 1

                write = open(path, "w")
                write.writelines(readlines)
                write.flush();
                write.close();
        else:
            haode(path)

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)
        print(dirs)

def main():
    global resutl
    # fa("E:\C_library\\boost_1_63_0\\boost\\asio")
    # haode("C:\Users\Administrator\Desktop\\newFile\NdkCamera\\app\src\main\cpp\\boost\\asio\\")
    # haode("C:\Users\Administrator\Desktop\\tps-550\\test\\")
    # fa("E:\C_library\boost_1_63_0\libs\\asio\\test")
    haode("C:\Users\Administrator\Desktop\jiaojie\\asio-1.10.8\include")
    print resutl

if __name__ == '__main__':
    main()