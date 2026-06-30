import functools

def hash(a, b):
    return a * ord(b)


def solution(input: List[str]):
    seen = dict()
    acc = []
    for s in input:
        x = functools.reduce(hash, s, 1)
        if x not in seen:
            seen[x] = len(acc)
            acc.append([])  # at index i
        i = seen[x]
        acc[i].append(s)
    return acc


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return solution(strs)