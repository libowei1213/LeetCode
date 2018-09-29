class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit_str = bin(n)[2:].zfill(32)
        return int(bit_str[::-1],base=2)