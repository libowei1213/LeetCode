from collections import defaultdict


class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        table = defaultdict(list)

        for a, b in dislikes:
            table[a].append(b)
            table[b].append(a)

        setA = set()
        setB = set()

        for key in table.keys():
            values = table[key]

            if not setA and not setB:
                setA.add(key)
                for value in values:
                    setB.add(value)

            if key in setA:
                for value in values:
                    if value in setA:
                        return False
                    if value not in setB:
                        setB.add(value)

            elif key in setB:
                for value in values:
                    if value in setB:
                        return False
                    if value not in setA:
                        setA.add(value)

        return True