from collections import Counter

if __name__ == '__main__':
    s = input()
    counter = Counter(s)
    repeat = False
    for c in counter:
        if counter[c] > 1:
            repeat = True
            break

    if repeat:
        print("중복 존재")
    else:
        print("중복 존재 안함")


#dictionary로도 풀 수 있을 듯
#key로 존재하면 중복