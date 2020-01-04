from collections import Counter

if __name__ == "__main__":

    string = input()
    string = string.replace(" ", '')
    string = string.lower()

    counter = Counter(string)
    possible = True
    palindrome = True
    for c in counter:
        if counter[c] % 2 != 0:
            if possible:
                possible = False
            else:
                palindrome = False
                break

    if palindrome:
        print("palindrome")
    else:
        print("not palindrome")



from itertools import permutations

def solution(string):
    string = string.lower().replace(' ', '')
    perm = list(map(''.join, permutations(string)))
    for i in perm:
        if i == i[::-1]: return True
    return False

print(solution('Tact Coa'))