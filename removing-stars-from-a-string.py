class Solution(object):
    def removeStars(self, s: str) -> str:
        s_stack = []
        for i in s:
            if i != '*':
                s_stack.append(i)
            else:
                s_stack.pop()
        return''.join(s_stack)
