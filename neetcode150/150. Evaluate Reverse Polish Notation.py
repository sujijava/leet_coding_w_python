'''Summary: (int(float(b)/a))'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []

        for t in tokens:
            if t == "+":
                plus = number_stack.pop() + number_stack.pop()
                number_stack.append(plus)
            elif t == "-":
                a, b = number_stack.pop(), number_stack.pop()
                number_stack(b - a)
            elif t == "*":
                multi = number_stack.pop() * number_stack.pop()
                number_stack.append(multi)
            elif t == "/":
                a, b = number_stack.pop(), number_stack.pop()
                number_stack.append(int(float(b)/a))
            else:
                number_stack.append(int(t))

        return number_stack[-1]
