class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        list = [""] * numRows

        max_row = 0
        max_col = 0

        str = s

        line = numRows

        if line == 0:
            return ""
        elif line == 1:
            return str

        for i, char in enumerate(str):

            x = i // (line + line - 2)
            y = i % (line + line - 2) + 1

            if y > line:
                col = x * (1 + line - 2) + 1 + y - line
                row = line - (y - line)
            else:
                col = x * (1 + line - 2) + 1
                row = y

            if max_col < col: max_col = col
            if max_row < row: max_row = row

            # dict[(row, col)] = char
            list[row - 1] += char

        result = ""

        # for l in list:
        #    result += "".join(l)
        return "".join(list)
