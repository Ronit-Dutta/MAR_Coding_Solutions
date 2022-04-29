def checkSuperASCII(s):
    b = [0 for i in range(26)]

    for i in range(len(s)):
        index = ord(s[i]) - 97 + 1
        b[index - 1] += 1

    for i in range(len(s)):
        index = ord(s[i]) - 97 + 1

        if (b[index - 1] != index):
            print("No")
            return

    print("Yes")
if __name__ == '__main__':
    s = input("Enter the string")
    checkSuperASCII(s)
