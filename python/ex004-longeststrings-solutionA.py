# 09.15.20 sjg - solution A
#Exercise 4
#Given an array of strings, return another array containing 
#all of its longest strings.

#Input: ["aba", "aa", "ad", "vcd", "aba"]
#Output: ["aba", "vcd", "aba"]

def lengthOfValue(x):
	
	return len(x)


def longestStringsInArray(listInput):


	listInput.sort(key=lengthOfValue)

	
	length_LastElement = len(listInput[-1])


	longestStrings = [] 


	for element in listInput:

		if len(element) == length_LastElement:

			longestStrings.append(element)
	

	return longestStrings


print(longestStringsInArray(["aba", "aa", "ad", "vcd", "aba"]))