class Solution:
    def intersect(self, a, b):
        # code here
        a=set(a)
        b=set(b)
        return list(a&b)
