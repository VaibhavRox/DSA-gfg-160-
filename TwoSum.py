class Solution:
	def twoSum(self, arr, target):
		arr.sort()
		l, r = 0, len(arr) - 1
		while l < r:
			sum = arr[l] + arr[r]
			if sum == target:
				return True
			elif sum < target:
				l += 1
			else:
				r -= 1
		return False
		