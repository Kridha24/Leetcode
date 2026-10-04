class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, answer = 0, x, 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return  mid

            elif mid * mid < x:
                answer = mid    
                left = mid + 1

            else:
                right = mid - 1

        return answer    

 # this is solved by binary search and its time complexity is o(log n )
 # simply we devide it into mid then compare and compare until round off value and neares root valus isnot found .           