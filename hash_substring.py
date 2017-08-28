# python3

_multiplier = 263
_prime = 1000000007


def read_input():
    return (input().rstrip(), input().rstrip())


def precomputeHash(patternlength, text):
    h = [None]*(len(text)-patternlength + 1)
    s = text[len(text)-patternlength:len(text)]
    h[len(text)-patternlength] = _hash_func(s)
    y = 1
    for i in range(1, patternlength + 1):
        y = y*_multiplier % _prime
    for i in range(len(text) - patternlength - 1, -1, -1):
        h[i] = ((_multiplier*h[i+1] + ord(text[i]) - y*ord(text[i+patternlength])) % _prime)
    return h


def _hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    pHash = _hash_func(pattern)
    list = []
    hashTable = precomputeHash(len(pattern), text)
    for i in range(len(text) - len(pattern) + 1):
        if hashTable[i] == pHash:
            if text[i:i + len(pattern)] == pattern:
                list.append(i)
    return list

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

