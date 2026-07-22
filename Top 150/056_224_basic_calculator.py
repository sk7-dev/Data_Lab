class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        res = 0 
        cur = 0 
        sign = 1 
        stack = [] 

        for c in s: 
            if c.isdigit(): 
                cur = cur * 10 + int(c)
            elif c == "+": 
                res += sign * cur 
                sign = 1 
                cur = 0 
            elif c == "-": 
                res += sign * cur 
                sign = -1 
                cur = 0 
            elif c == "(": 
                stack.append(res) 
                stack.append(sign)
                res = 0 

                cur = 0 
                
                sign = 1 
            elif c == ")": 
                res += sign * cur 
                cur = 0 
                res = res * stack.pop() 
                res += stack.pop()  

                sign = 1 
        
        return res + sign * cur 