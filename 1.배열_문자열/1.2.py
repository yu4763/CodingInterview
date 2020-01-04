from collections import Counter

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    if counter1-counter2:
        print("순열관계가 아님")
    else:
        print("순열관계")



#itertools, permutations 을 이용해 순열모두 만들어서 check도 가능
#list(map("".join, permutation(str1))
