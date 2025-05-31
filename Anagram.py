#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
       #code here
       charcount={}
       for i in s1:   #count occurences of each character and store in dictionary
           charcount[i]=charcount.get(i,0)+1
          
       for i in s2:     #reduce count of each character if seen in s2
           charcount[i]=charcount.get(i,0)-1
           
       for val in charcount.values(): #check if all counts of characters are 0
           if val!=0:
               return False
               
        #if all values are 0, then anagram
       return True 
        