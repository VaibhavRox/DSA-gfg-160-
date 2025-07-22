
class Solution:
    def countTriplets(self, arr, target):
        # code heredef countTriplets(arr, target):
        n = len(arr)
        count = 0
    
        for i in range(n - 2):
            left = i + 1
            right = n - 1
    
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    # arr[left] == arr[right]
                    if arr[left] == arr[right]:
                        num_elements = right - left + 1
                        count += (num_elements * (num_elements - 1)) // 2
                        break
                    else:
                        # Count duplicates
                        l_count = 1
                        r_count = 1
                        while left + 1 < right and arr[left] == arr[left + 1]:
                            l_count += 1
                            left += 1
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            r_count += 1
                            right -= 1
                        count += l_count * r_count
                        left += 1
                        right -= 1
        return count