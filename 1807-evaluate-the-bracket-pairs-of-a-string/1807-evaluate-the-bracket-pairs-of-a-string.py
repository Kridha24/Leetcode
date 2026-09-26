class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        lookup = dict(knowledge)
        result = []
        start = -1

        for i, char in enumerate(s):
            if char == '(':
                start = i + 1

            elif char == ')':
                key = s[start:i]
                result.append(lookup.get(key, "?"))
                start = -1

            elif start == -1:
                result.append(char)

        return "".join(result)