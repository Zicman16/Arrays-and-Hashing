from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Freq_Dict = defaultdict(int)

        # records the frequency of each integer
        for i in nums:
            if i in Freq_Dict:
                Freq_Dict[i] += 1
            else:
                Freq_Dict[i] = 1
        
        # Sorts the array based on the value of each key. The sort is done in descending order (most frequent to least frequent.)
        # With the array sorted, we can easily retrieved the values based upon k. 
        Freq_Dict = [key for key, value in sorted(Freq_Dict.items(), key = lambda item: item[1] , reverse = True)]
        return Freq_Dict[:k]

Sol = Solution()

# Test Cases
# Arr = [1,1,1,2,2,3]
# Arr2 = [3,2,2,1,1,1]
Arr3 = [5,5,5,6,6,7]
K_Val = 2

x = Sol.topKFrequent(Arr3, K_Val)
print(x)
