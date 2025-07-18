class Solution:
    def subarrayXor(self, arr, k):
        # code here
        from collections import defaultdict
        count=0
        pref_xor=0
        freq=defaultdict(int)
        for num in arr:
            pref_xor^=num
            if pref_xor==k:
                count+=1
            if pref_xor^k in freq:
                count+=freq[pref_xor^k]
            freq[pref_xor]+=1
        return count