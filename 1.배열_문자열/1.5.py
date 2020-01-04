if __name__ == "__main__":
    ss1, ss2 = input().split(", ")
    possible = True
    answer = True

    n1 = len(ss1)
    n2 = len(ss2)
    n = n1 if n1 > n2 else n2
    s1 = ss1 if n1 > n2 else ss2
    s2 = ss2 if n1 > n2 else ss1

    if abs(n1 - n2) > 1:
        print("false")

    elif abs(n1 - n2) == 1:
        k = 0
        for i in range(n):
            if k == n - 1:
                if not possible:
                    answer = False
                break

            if s1[i] != s2[k]:
                if possible:
                    possible = False
                else:
                    answer = False
                    break
            else:
                k += 1

    else:
        for i in range(n):
            if s1[i] != s2[i]:
                if possible:
                    possible = False
                else:
                    answer = False
                    break

    if answer:
        print("true")
    else:
        print("false")



#if len(str1) < len(str2):
 #   str1, str2 = str2, str1