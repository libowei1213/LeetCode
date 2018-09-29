class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        occur = []

        for id, char in enumerate(S):
            if char == C:
                occur.append(id)

        return [min([abs(o - id) for o in occur]) for id in range(len(S))]