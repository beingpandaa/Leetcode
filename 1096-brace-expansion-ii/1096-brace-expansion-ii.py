class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        union = set()
        product = {""}

        for char in expression:
            if char == "{":
                stack.append((union, product))
                union = set()
                product = {""}
            elif char == ",":
                union |= product
                product = {""}
            elif char == "}":
                factor = union | product
                union, left = stack.pop()
                product = {a + b for a in left for b in factor}
            else:
                product = {word + char for word in product}

        return sorted(union | product)