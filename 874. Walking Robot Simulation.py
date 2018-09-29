from collections import defaultdict


class Solution:

    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        obstacle_dict = defaultdict(int)
        for obstacle in obstacles:
            obstacle_dict[(obstacle[0],obstacle[1])] += 1

        position = [0, 0]
        faces = [0, 1], [1, 0], [0, -1], [-1, 0]
        face_index = 0
        distance = 0

        for c in commands:
            if c == -1:
                face_index += 1
                face_index %= 4
            elif c == -2:
                face_index -= 1
                face_index %= 4
            else:
                # move
                dest = [position[0] + faces[face_index][0] * c, position[1] + faces[face_index][1] * c]

                while position != dest:
                    temp = [position[0] + faces[face_index][0], position[1] + faces[face_index][1]]
                    if obstacle_dict[(temp[0],temp[1])]:
                        break
                    position = temp

                temp = position[0] * position[0] + position[1] * position[1]
                if temp > distance:
                    distance = temp

        return distance


if __name__ == '__main__':
    r = Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]])
    print(r)
