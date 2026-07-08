class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return False
        
        count = 0
        current_sum = 0

        # Inclusive left, inclusive right
        left = 0
        for right in range(len(arr)):
            #print(f"{left=}, {right=}")
            if right-left == k:
                current_sum -= arr[left]
                left += 1
            current_sum += arr[right]
            #print(f"{arr[left:right+1]=}, {current_sum=}, {left=}, {right=}, {count=}")
            if right-left+1 == k and threshold <= current_sum/k:
                count += 1
        
        #print(f"\n\nstart {arr[left:right+1]=}, {current_sum=}, {left=}, {right=}, {count=}")
        return count