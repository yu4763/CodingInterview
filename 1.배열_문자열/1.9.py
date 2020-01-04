def isSubString(sub, string):
    if sub in string:
        return True
    return False


if __name__ == "__main__":
    s1, s2 = input().split()
    s = s2+s2
    if isSubString(s1, s):
        print("true")
    else:
        print("false")