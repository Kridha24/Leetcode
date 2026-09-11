class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        for digit in digits:
            count[digit] += 1

        answer = 0

        for number in range(100, 1000, 2):
            required = [0] * 10
            value = number

            while value:
                required[value % 10] += 1
                value //= 10

            if all(required[digit] <= count[digit] for digit in range(10)):
                answer += 1

        return answer