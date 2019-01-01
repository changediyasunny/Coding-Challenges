"""
681. Next closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid.

"1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time
is next day's time since it is smaller than the input time numerically.

"""
class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        nums = sorted(set(hour+minute))
        allowed = [a+b for a in nums for b in nums]

        # check for next avail minute
        i = allowed.index(minute)
        if i+1 < len(allowed) and allowed[i+1] < '60':
            return hour +":"+ allowed[i+1]

        # check for hour
        i = allowed.index(hour)
        if i+1 < len(allowed) and allowed[i+1] < '24':
            return allowed[i+1] + ":" + allowed[0]

        # return earliest time
        return allowed[0]+":"+allowed[0]
