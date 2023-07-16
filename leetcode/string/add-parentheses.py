class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def calc(left, right, operator):
            if operator == "+":
                return left + right
            elif operator == "-":
                return left - right
            elif operator == "*":
                return left * right

        def diffWaysToComputeHelper(expression):
            if expression.isdigit():
                return [int(expression)]

            outputList = []

            for i in range(len(expression)):
                if expression[i] in ["+", "-", "*"]:

                    leftResults = diffWaysToComputeHelper(expression[:i])
                    rightResults = diffWaysToComputeHelper(expression[i+1:])

                    for left in leftResults:
                        for right in rightResults:
                            outputList.append(calc(left, right, expression[i]))

            return outputList

        return diffWaysToComputeHelper(expression)