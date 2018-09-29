class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()

        boats = 0

        while len(people) >= 2:
            total = people[0] + people[-1]
            if total <= limit:
                people.pop(0)
                people.pop(-1)
            else:
                people.pop(-1)
            boats += 1

        if people:
            boats += 1

        return boats