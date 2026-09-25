from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        i = 0
        n = len(expression)

        def parse():
            nonlocal i

            result = set()
            current = {""}

            while i < n and expression[i] != "}":
                char = expression[i]

                if char == ",":
                    result.update(current)
                    current = {""}
                    i += 1
                    continue

                if char == "{":
                    i += 1       # Skip opening brace
                    choices = parse()
                    i += 1       # Skip closing brace
                else:
                    choices = {char}
                    i += 1

                current = {
                    prefix + suffix
                    for prefix in current
                    for suffix in choices
                }

            result.update(current)
            return result

        return sorted(parse())