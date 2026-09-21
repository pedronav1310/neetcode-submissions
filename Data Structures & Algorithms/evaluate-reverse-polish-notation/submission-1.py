class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            elif token is "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a)+int(b))
            elif token is "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a)*int(b))
            elif token is "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)-int(a))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(int(b)/int(a)))
        return int(stack[-1])