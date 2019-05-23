# Given a time represented in the format "HH:MM", form the next closest time by
#  reusing the current 
# digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34",
#  "12:09" are all valid. 
# "1:34", "12:9" are all invalid.

# Example 1:

# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
#  which occurs 5 minutes
#  later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:

# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
#  It may be assumed that
#  the returned time is next day's time since it is smaller than the input 
# time numerically.
import itertools
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        num1, num2, num3, num4 = int(time[0]), int(time[1]), int(time[3]), int(time[4])
        curr = num1 * 10 * 60 + num2 * 60 + num3 * 10 + num4
        nextClosest = None
        for a, b, c, d in itertools.product([num1,num2,num3,num4], repeat=4):
            temp = a * 10 * 60 + b * 60 + c * 10 + d
            if temp > curr and temp < 24 * 60 and 10 * a + b < 24 and \
            c * 10 + d < 60:
                print a, b,c,d, temp, divmod(temp, 60)
                if nextClosest == None:
                    nextClosest = temp
                else:
                    nextClosest = min(nextClosest, temp)
        if nextClosest != None:
            hours,minutes = divmod(nextClosest,60)
            hoursStr = str(hours) if hours >= 10 else "0" + str(hours)
            minutesStr = str(minutes) if minutes >= 10 else "0" + str(minutes)
            return hoursStr + ":" + minutesStr
        else:
            minimum = min([num1, num2, num3, num4])
            return str(minimum) + str(minimum) + ":" + str(minimum) + str(minimum)

s = Solution()
print s.nextClosestTime("20:48")
