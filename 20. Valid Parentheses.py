class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        if len(s) % 2 != 0:
            return False

        for index, char in enumerate(s):

            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if stack == []:
                    return False
                c = stack.pop()
                if c != '(':
                    return False
            elif char == '}':
                if stack == []:
                    return False
                c = stack.pop()
                if c != '{':
                    return False
            elif char == ']':
                if stack == []:
                    return False
                c = stack.pop()
                if c != '[':
                    return False
        if stack != []:
            return False

        return True
