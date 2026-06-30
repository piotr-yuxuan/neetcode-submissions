class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for segment in path.split('/'):
            if segment in {'', '.'}:
                continue
            elif '..' == segment:
                if stack:
                    stack.pop()
            else:
                stack.append(segment)
        return '/' + '/'.join(stack)
            