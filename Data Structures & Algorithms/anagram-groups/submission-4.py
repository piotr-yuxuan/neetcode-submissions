from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def make_key(counter):
            a = ord('a')
            result = [0 for i in range(a, ord('z')+1)]
            for k, v in counter.items():
                result[ord(k)-a] = v
            return '|'.join(map(str, result))
            

        groups = defaultdict(list)
        for s in strs:
            k = make_key(Counter(s))
            groups[k].append(s)
        
        return list(groups.values())