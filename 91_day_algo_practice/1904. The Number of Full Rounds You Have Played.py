class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        # Convert to minutes
        t0 = 60 * int(loginTime[:2]) + int(loginTime[3:])
        t1 = 60 * int(logoutTime[:2]) + int(logoutTime[3:])

        # If logoutTime is on the next day, add 1440 minutes (24 hours)
        if t1 < t0:
            t1 += 1440
        t1 = t1 // 15 * 15

        # Calculate the number of full rounds played
        return max(0, (t1 - t0)) // 15
