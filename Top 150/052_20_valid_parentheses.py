class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        check = []
        for char in s:
            if char in "([{":
                check.append(char)
            else:
                if char in ")]}":
                    if not check: return False
                    top = check[-1]
                    if pairs[char] == top:
                        check.pop()
                    else: return False
        if not check: return True
        else: return False