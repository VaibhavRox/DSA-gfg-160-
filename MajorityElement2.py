from collections import Counter
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        freq=Counter(arr)
        n=len(arr)
        threshold=n//3
        result=[num for num,count in freq.items() if count>threshold]
        return sorted(result)