class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_length = max_length = 0
        current = set()

        # Inclusive both ends.
        left = 0
        for right in range(len(s)):
            #print(f"{left=}, {right=}, {s[right]}, {current_length=}, {current=}")
            while s[right] in current:
                #print("s[right] in current")
                current.remove(s[left])
                current_length -= 1
                left += 1
            current.add(s[right])
            current_length += 1
            max_length = max(max_length, current_length)

        return max_length
