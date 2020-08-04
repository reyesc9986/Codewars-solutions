# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# Example:

# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
# Note

# consecutive strings : follow one after another without an interruption

def longest_consec(strarr, k):
    # need to deal with invalid input and return "", so if statements
    #this task wants me to concatinate strings via k, the second parameter.
    #Then it wants me to return the string that has the largest length of the concatinations.
    #want to iterate through the input.
    #need to find the index of the current element then combine it with the consecutive element.
    ans = ''
    stringcheck = ''
    point = 0
    limit = 0
    i = 1
    #Check if we have a list of valid length, if not, return desired output.
    if len(strarr) <= 0:
        return ""
    else:#Otherwise, the output should be fine, begin performing operations.
        for string in strarr:
            point = strarr.index(string)
            limit = strarr.index(strarr[-1]) #limit/length = position of the last character.
            ans = string 
            if k > limit+1: 
                return ""
            elif k <= 0:
                return ""
            #limit +2 because limit is the position of the last character. I want this to include the last character.
            #Need the +2 because it's 0 index, and I need to make sure that the bounds are up to and including the last character
            #anything over that throws an error, so I need to make sure it's below the index that doesn't exist.
            elif point + k < limit+2:
                i = 1
                while i < k:             #want to keep looping until I hit k.
                    ans += strarr[point+i]
                    i += 1
            #Compare the strings using len to see which is bigger.
                if len(ans) > len(stringcheck):
                    stringcheck = ans

        return stringcheck
                    
        