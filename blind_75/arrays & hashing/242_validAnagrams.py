'''
242. Valid Anagram
Solved
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            count[char] = count.get(char, 0) - 1

        for char in count:
            if count.get(char, 0) != 0:
                return False
        return True

'''
NOTES:

initial thought: 

create a set that reads through s
create a set that reads through t
compare the set
and then compare the num of words

(but set removes duplicates, that will mess with the number of alphabest so it won't work)


working solution:

first check length, if doesn't match then instantly false.

add each letter to a dictionary with for loop on s; then remove all of then with for loop on t.

if we get null dictionary, then True, or false.

'''