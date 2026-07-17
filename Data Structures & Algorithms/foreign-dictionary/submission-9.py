from collections import defaultdict, deque, OrderedDict
import itertools

class TreeNode:
    def __init__(self):
        self.children = OrderedDict()
        self.word = False

    def add(self, word) -> bool:
        current = self
        for l in word:
            current.children[l] = current.children.get(l, TreeNode())
            current = current.children[l]
        
        if current.children:
            return False
        current.word = True
        return True

class Solution:
    def _foreignDictionary(self, words: List[str]) -> str:
        prefix_tree = TreeNode()
        indegree = defaultdict(int)
        for w in words:
            if not prefix_tree.add(w):
                return ''
            for l in w:
                indegree[l] = 0
        
        adjacency = defaultdict(set)
        def dfs(node):
            if node is None:
                return
            keys = node.children.keys()
            for n1, n2 in itertools.pairwise(keys):
                adjacency[n1].add(n2)
            for k in keys:
                dfs(node.children[k])
        dfs(prefix_tree)
    
        for parent, children in adjacency.items():
            for c in children:
                indegree[c] += 1
        print(dict(adjacency))
        print(dict(indegree))


    def foreignDictionary(self, words: List[str]) -> str:
        adjacency = defaultdict(set)
        indegree = dict()

        for word in words:
            for c in word:
                indegree.setdefault(c, 0)

        for w1, w2 in pairwise(words):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adjacency[c1]:
                        adjacency[c1].add(c2)
                        indegree[c2] += 1
                    break

        q = deque()
        for k, v in indegree.items():
            if 0 == v:
                q.append(k)

        ret = []
        while q:
            node = q.popleft()
            print(f"{node=}")
            print(f"indegree={dict(indegree)}")
            ret.append(node)
            for child in adjacency[node]:
                indegree[child] -= 1
                if 0 == indegree[child]:
                    q.append(child)

        print(len(ret), len(indegree), ret)
        return ''.join(ret) if len(ret) == len(indegree) else ''
