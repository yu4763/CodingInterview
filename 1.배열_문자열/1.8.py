def make0 (k, arr, m):
    for i in range(m):
        arr[i][k] = 0



if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    arr = []
    for i in range(m):
        arr.append(list(input().split()))

    loc = []
    for k in range(n):
        for i in range(m):
            if arr[i][k] == '0':
                make0(k, arr, m)
                loc.append(i)
                break

    for i in loc:
        arr[i] = [0]*n


    print(arr)
