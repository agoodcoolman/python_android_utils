#C:\Users\Administrator\Desktop\newFile\android-ndk

import os


def main() :
    dir = r"C:\Users\Administrator\Desktop\newFile\android-ndk";
    if os.path.exists(dir):
        os.removedirs(dir)

if __name__ == '__main__':
    main()