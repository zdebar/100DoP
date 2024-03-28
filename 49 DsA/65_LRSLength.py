S1 = "ABCBDAB"
S2 = "BDCABA"

def LCSLength(S1, S2, lenS1, lenS2):
 
	# return if we have reached the end of either sequence
	if lenS1 == 0 or lenS2 == 0:
		return 0
 
	# if last character of S1 and S2 matches
	if S1[lenS1 - 1] == S2[lenS2 - 1]:
		return LCSLength(S1, S2, lenS1 - 1, lenS2 - 1) + 1
 
	# else if last character of S1 and S2 don't match
	return max(LCSLength(S1, S2, lenS1, lenS2 - 1), LCSLength(S1, S2, lenS1 - 1, lenS2))
 
print(LCSLength(S1, S2, len(S1), len(S2)))