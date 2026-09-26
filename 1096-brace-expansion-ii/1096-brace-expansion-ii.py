class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0
        n = len(expression)

        def parse():
            nonlocal i
            union = set()
            product = {""}

            while i < n and expression[i] != "}":
                if expression[i] == ",":
                    union |= product
                    product = {""}
                    i += 1
                else:
                    if expression[i] == "{":
                        i += 1
                        factor = parse()
                        i += 1
                    else:
                        start = i
                        while i < n and expression[i].isalpha():
                            i += 1
                        factor = {expression[start:i]}

                    product = {left + right for left in product for right in factor}

            return union | product

        return sorted(parse())