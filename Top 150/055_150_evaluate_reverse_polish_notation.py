class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(v1 + v2)
            elif token == "*":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(v1 * v2)
            elif token == "/":
                v1, v2 = stack.pop(), stack.pop()
                sign = (v1 >= 0) ^ (v2 >= 0)
                stack.append(abs(v2) // abs(v1) * (-1 if sign else 1))
            elif token == "-":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(v2 - v1)
            else:
                stack.append(int(token))
        return stack[0]