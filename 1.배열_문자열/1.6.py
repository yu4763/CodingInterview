
if __name__ == "__main__":
    ss = input()
    n = len(ss)

    cnt = 1
    ans = ""
    for i in range(1, n):
        if ss[i] == ss[i-1]:
            cnt += 1
        else:
            ans += ss[i-1] + str(cnt)
            cnt = 1

    ans += ss[n-1] + str(cnt)

    if len(ans) <= n:
        print(ans)
    else:
        print(ss)

