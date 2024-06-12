# approach #1: brute force, nested for loop starting at each character and going as far as you can
# runtime: O(n^2)

# can this be run in linear time... ? 

# approach #2: 2 pointer, O(n) runtime
# convert each array to ord values
# subtract the two
# loop through, find section where you can sum most numbers < maxCost

# this last part is a bit tricky, 
# two pointers, i, j
# i starts at the beginning, then j goes as far as it can until maxCount is reached, keep track the diff between j and i
# next, throw i away from sum, move it up keeping j, now you can increase j to the end

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        ordS = [ord(ss) for ss in list(s)]
        ordT = [ord(tt) for tt in list(t)]
        subs = [abs(j - ordT[i]) for i, j in enumerate(ordS)]

        i, j, l, li, lj = 0, 0, -1, -1, -1
        while j < len(s) and i <= j:
            if sum(subs[i:j]) <= maxCost:
                if (j - i) > l:
                    l, li, lj = (j - i), i, j
                j += 1
            else:
                i += 1
                if j < i:
                    j = i
        print("li is {0} lj is {1}".format(li, lj))
        print("substring is: " + s[li:lj])

sol, s, t, maxCost = Solution(), "dwediwe", "bcdefge", 5
sol.equalSubstring(s, t, maxCost)
