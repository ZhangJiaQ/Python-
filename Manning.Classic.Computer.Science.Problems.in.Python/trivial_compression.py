# coding=utf-8
# @Time    : 2019-03-29 13:26
# @Author  : 张嘉麒
# @File    : trivial_compression.py

"""
通常在存储大量数据的时候
如果不压缩
会占用额外空间
所以我们需要压缩相应数据

"""

class CompressedGene:
    """
    一个将ACGT压缩成二位二进制数字的对象
    """
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene) -> int:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length()-1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self):
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = "TAGGGATTAACCGTTATATATATATTAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)  # compressed.__str__
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))