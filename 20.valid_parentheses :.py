# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
    
            if ch in ')]}':
                if not stack: return False
                
                last_p = stack.pop()
                if (ch == ')' and last_p != '(') or \
                    (ch == ']' and last_p != '[') or \
                    (ch == '}' and last_p != '{'):
                    return False
                
        return False if stack else True  
