# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:15:54 2018

@author: mike
"""

# =============================================================================
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# >
# > Find the largest palindrome made from the product of two 3-digit numbers.
# =============================================================================
num1, num2 = 999, 999

def palindrome_num(num1, num2):
    product = num1 * num2
   
    def isPalindrome(product):
        s = str(product)
        return s
    
    def toChars(s):
        """reduces a string to lower case letters;
        eliminates non alpha-numeric characters"""
        s = s.lower()
        ans = "" #holder for return value
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz0123456789': #validates alpha-numeric
                ans += c #string s as lower case alpha-numeric
        return ans
    
    def isPal(s):
        """validates string is the same frontwards and backwards"""
        if len(s) <= 1: #Base Case; has to be a Palindrome if len is 0 or 1
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) #validates the first and last character are equal
                                                    #AND
                                                    #reduces the string s by eliminating the first and last char
    return isPal(toChars(s))