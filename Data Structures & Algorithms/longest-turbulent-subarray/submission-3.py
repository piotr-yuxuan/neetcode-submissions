from itertools import pairwise


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)

        max_length = 1
        previous_sign = None

        def sign(a, b) -> int:
            value = 0
            if a < b:
                value = -1
            elif b < a:
                value = 1
            return value

        # Inclusive both ends.
        left = 0
        for right in range(len(arr)):
            if 1 == right - left + 1:
                continue
            if previous_sign is None:
                previous_sign = sign(arr[right - 2], arr[right - 1])
            current_sign = sign(arr[right - 1], arr[right])
            if 0 == current_sign:
                left = right
                continue
            elif previous_sign == current_sign:
                left = right - 1
                continue
            previous_sign = current_sign
            max_length = max(max_length, right - left + 1)

        return max_length
