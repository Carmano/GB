def main():
    path = "C:\\Users\\tuvan\\Desktop\\MyProject\\GB.exe"
    file = ''
    resolution = ''
    absolute_url = ''
    flag1 = flag2 = 0

    for c in path[::-1]:
        if c == "\\":
            flag1 = 1
        if flag1:
            absolute_url = c + absolute_url
        else:
            if c == '.':
                flag2 = 1
            if flag2:
                if c == '.':
                    continue
                file = c + file
            else:
                resolution = c + resolution

    print(absolute_url)
    print(file)
    print(resolution)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
