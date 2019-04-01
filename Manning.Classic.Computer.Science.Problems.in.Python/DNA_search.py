# coding=utf-8
# @Time    : 2019-04-01 14:37
# @Author  : 张嘉麒
# @File    : DNA_search.py


from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Nucleotide]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) > len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if key_codon == codon:
            return True
    return False


def binary_contains(gene: Gene, key_codon: Codon) ->bool:
    pass


if __name__ == "__main__":
    pass
