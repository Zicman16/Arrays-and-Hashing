Contained within is the explanation of the problem, my thought process on solving the problem, and my final solution.

   **Contains Duplicate**

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1: 

nput: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.


Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


My Code: 

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        Record = set()
        for i in nums:
            if i in Record:
                return True

            else:
                Record.add(i)

        return False


Explanation: A set called Record is used to as a set to store each element as the nums list is iterated through. As we go through the list, each num is checked to see if it is in the record set. If so, a duplicate is detected, and we immediately return true, since a duplicate has been detected. Finally, if the entire list has been integrated through with a hit, no duplicates are present. In this case, we return false.



    **Valid Anagram**
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

My Code: 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # checks to see if each string is the same length.
        # if not, automatically return false
        if len(s) != len(t):
            return False

        # Creates a dictionary to store character frequencies
        Freq_Dict = {}
        for i in s:
            if i in Freq_Dict:
                Freq_Dict[i] += 1
            else:
                Freq_Dict[i] = 1

        # Check the second string to verify if it has the same 
        # Char freqency as the first string.

        for Key, Val in Freq_Dict.items():
            Freq_Val = 0

            for char in t:
                if char == Key:
                    Freq_Val += 1

            # if a miss match is found, then the 2 strings
            # cannot be anagrams.
            if Freq_Val != Val:
                return False

        return True


Explanation: First, we take the first string and find the frequencies of each character in it. This is done using a dictionary. Once done, we then need to compare the frequency of each character in the second string to that in the first string. This is done by iterating through our dictionary. For each key and value pair, we find the frequency of the key in the second string. We then compare the found frequency to the value of the key in the dictionary. If the two values match, then we currently have a valid anagram. If we find a key in the dictionary that fails to have the same frequency in the second string, we can determine that the two strings are not anagrams.




    **Top K Frequent Elements**


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]


Example 2: 

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]


My Code: 

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


Explanation: To start, a default dict is used to store the frequencies of each of the integers within the list. Afterward, the dictionary is sorted in descending order, and stored as a list. Once done, the final list is spliced using the value k. Since the list is in descending order, the values with the greatest occurrence are at the front of the list, making it easy to splice them.

