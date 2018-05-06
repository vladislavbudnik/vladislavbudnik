

def readImg(path):
    try:
        with open(path, "rb") as r:
            byte = r.read(1)
            k = 0
            while byte:
                print(byte, end="")
                try:
                    byte = r.read(1).decode("utf-8")
                except:
                    continue
                k += 1
    except FileNotFoundError:
        print("\n[x] File: '" + str(path) + "' is not defined!")
        raise SystemExit
    else:
        print("\n[+] Number of bytes in the '" + str(path) + "': " + str(k))
    pass


def writeImg(path, text):
    try:
        with open(path, 'ab') as file:
            file.write(text.encode("utf-8"))
    except FileNotFoundError:
        print("[x] File: '" + str(path) + "' is not defined!")
        raise SystemExit
    else:
        print("[+] File: " + str(path) + " successfully overwritten!")
    pass


def zipImg(path, zpath):
    try:
        with open(path, 'rb') as file1:
            read1 = file1.read()
    except FileNotFoundError:
        print("[x] File: '" + str(path) + "' is not defined!")
        raise SystemExit
    try:
        with open(zpath, 'rb') as file2:
            read2 = file2.read()
    except FileNotFoundError:
        print("[x] File: '" + str(zpath) + "' is not defined!")
        raise SystemExit
    with open(path, 'wb') as file3:
        file3.write(read1)
        file3.write(read2)
        print("[+] File: " + str(path) + " successfully overwritten!")
    pass


def main():
    while True:
        mode = input("Select mode [r - read, w - write, z - zip write, q - quit] (default 'r'):\n")
        if mode == 'w':
            path = input("Enter path to image:\n")
            text = input("Write the text:\n")
            writeImg(path, text)
        elif mode == 'z':
            path = input("Enter path to image:\n")
            zpath = input("Enter path to zip:\n")
            zipImg(path, zpath)
        elif mode == 'q':
            break
        else:
            path = input("Enter path to image:\n")
            readImg(path)
    print("Program ended.")
    pass


if __name__ == "__main__":
    main()

