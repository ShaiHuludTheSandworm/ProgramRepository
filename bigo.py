"""
On my/our honor, Shasa Lloyd Kolar and Ethan Gomez, this 
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: SLK2633
UT EID 2: EGB664
"""


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n3(s):
	"""
	Finds the length of the longest substring without repeating characters
	using a brute force approach (O(N^3)).

	pre: s is a string of arbitrary length, possibly empty.
	post: Returns an integer >= 0 representing the length of the longest substring
		  in s that contains no repeating characters.
	"""
	max_length = 0
	characters = {}
	for beginning in range(len(s)):
		middle = 0
		length = 0
		while middle < len(s):
			if beginning > middle:

			elif middle > beginning:
			
			else:


			if > max_length:
				max_length = 
			middle += 1


	


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n2(s):
	"""
	Finds the length of the longest substring without repeating characters
	using a frequency list approach (O(N^2)), converting each character to
	their corresponding numeric representation in ASCII as the index into the
	frequency list.

	pre: s is a string of arbitrary length, possibly empty.
	post: Returns an integer >= 0 representing the length of the longest substring
		  in s that contains no repeating characters.
	"""
	#This function works, just not 100% sure if this is O(N^2)
	max_length = 0

	for start in range(len(s)):
		freq_list = [0] * 256

		for end in range(len(s)):
			char_index = ord(s[end])
			freq_list[char_index] += 1

			if freq_list[char_index] > 1:
				break
			max_length = max(max_length, end - start + 1)
	return max_length


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n(s):
	"""
	Letters are added to a set, if the set does not increase when added to then it has found a duplicate
	A separate variable keeps track of set size before new letter is added
	If a letter is added to set, but the set size does not increase it goes back by the length of the set and checks
	that letter against the current location in the for loop, 
	if that letter is the duplicate then the length of the substring goes down by 1, 
	if that letter is not the duplicate that letter is removed from the set and the substring length goes down by 1, 
	once the duplicate is reached and the substring went down by 1
	the set does not have that letter removed since we are already at it again
	"""
	#This code is based off the google doc instructions, my bad.
	#Couldn't figure out the other way

	#Keeps track of char using frequency list
	freq_list = [0] * 256
	max_length = 0
	start = 0

	#convert s[end] to ASCII & adds it to frequency list
	for end in range(len(s)):
		char_index = ord(s[end])
		freq_list[char_index] += 1

		#moves start pointer to the right by one & removes duplicate char from list
		while freq_list[char_index] > 1:
			freq_list[ord(s[start])] -= 1
			start += 1

		#Tracks max ss length
		max_length = max(max_length, end - start + 1)
	
	return max_length
	
