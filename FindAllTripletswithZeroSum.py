#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        map = {}
        ans = []
        # Check for all pairs i, j
        for j in range(len(arr)):
            for k in range(j + 1, len(arr)):
                
                # Value of third index should be 
                val = -1 * (arr[j] + arr[k])
                
                # If such indices exist
                if val in map:
                    
                    # Append the i, j, k
                    for i in map[val]:
                        ans.append([i, j, k])
            
            # After j'th index is traversed
            # We can use it as i.
            if arr[j] not in map:
                map[arr[j]] = []
            map[arr[j]].append(j)
        
        return ans