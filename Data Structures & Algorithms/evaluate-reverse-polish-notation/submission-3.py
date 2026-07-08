class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for k in tokens:
            if k == "+":
                stack.append(stack.pop() + stack.pop())
            elif k == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif k == "*":
                stack.append(stack.pop() * stack.pop())
            elif k == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(k))
        return stack[0]