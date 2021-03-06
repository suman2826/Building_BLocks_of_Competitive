class Solution:
	def countBits(self,num):
		if num == 0:
			return [0]
		dp = [0,1] + [0]*(num-1)
		for i in range(2,num+1):
			if i % 2 == 0:
				dp[i] = dp[i//2]
			else:
				dp[i] = dp[i//2]+1
		return dp

