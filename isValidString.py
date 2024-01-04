# Mock project 2
# Read a file in your local computer and given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid
# An input string is valid if:
# 1.Open brackets must be closed by the same type of brackets
# 2.Open brackets must be closed in the correct order

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'

# Example 1:
# Input: s = "()"
# Output: valid

# Example 2:
# Input: s = "()[]{}"
# Output: valid

# Example 3:
# Input: s = "(]"
# Output: invalid

# Example 4:
# Input: s = "([)]"
# Output: invalid

# Example 5:
# Input: s = "{[]}"
# Output: valid

# Mock project 3:
# Write unit test by Pytest module for project 2 and try to use Exception in that project.

# Mock project 4:
# Upload Mock project 2 and 3 to a git repo.
# Create a Jenkins job to run Pytest for project 3.
# Analysis test result.

# create custom Exception
class QueueIsOutOfRange(IndexError):
    """Exception raised when variable 'queue' has }/)/] at the first index."""

def isValidString(s: str) -> str:
    if len(s) > 104 or len(s) < 1:
        return "invalid"
    queue = []
    try: 
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(' :
                queue.append(s[i])
            elif s[i] == ']' and queue[-1] == '[':
                queue.pop(-1)
            elif s[i] == '}' and queue[-1] == '{':
                queue.pop(-1)
            elif s[i] == ')' and queue[-1] == '(':
                queue.pop(-1)
    except IndexError:
        # raise IndexError
        raise QueueIsOutOfRange("Out of range")
    
    if  queue == []:
        return "valid"
    return "invalid"
