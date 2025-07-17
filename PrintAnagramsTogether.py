#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        anagram={}
        for s in arr:
            key=''.join(sorted(s))
            if key not in anagram:
                anagram[key]=[]
            anagram[key].append(s)
        return list(anagram.values())