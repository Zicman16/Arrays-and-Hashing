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


Sol = Solution()

### Test Cases
# s = "anagram"
# t = "nagaram"

s = "rat"
t = "car"

res = Sol.isAnagram(s, t)
print(res)