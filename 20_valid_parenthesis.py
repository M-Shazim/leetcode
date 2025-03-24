class Solution(object):
    def isValid(self, s):
        if len(s) ==1:
            return False
        stack = []
    
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for item in s:
            if item in brackets:
                stack.append(item)             
            else:
                if not stack:
                    return False

                stack_item = stack.pop()

                if item != brackets[stack_item]:
                    return False

        if not stack:
            return True
        else:
            return False

        
    
