class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            # Sum the days of the preceding months, then add the current day
            return sum(days_in_month[:month - 1]) + day
        
        start_a = date_to_day_of_year(arriveAlice)
        end_a = date_to_day_of_year(leaveAlice)
        start_b = date_to_day_of_year(arriveBob)
        end_b = date_to_day_of_year(leaveBob)
        
        overlap_start = max(start_a, start_b)
        overlap_end = min(end_a, end_b)
        
        return max(0, overlap_end - overlap_start + 1)