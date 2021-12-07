import pickle

seq_test = "ACGACTACAGACAT"
sa_test = [14, 6, 10, 0, 3, 8, 12, 7, 11, 1, 4, 9, 2, 13, 5]
bwt_test = ['T', 'T', 'G', '$', 'G', 'C', 'C', 'A', 'A', 'A', 'A', 'A', 'C', 'A', 'C']
rank_test = [0, 1, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4, 2, 5, 3]
occ_test = {'$': 1, 'A': 6, 'C': 4, 'G': 2, 'T': 2}


with open("seq.pickle", "rb") as fin:
    seq = pickle.load(fin)
with open("sa_seq.pickle", "rb") as fin:
    sa_seq = pickle.load(fin)
with open("bwt_seq.pickle", "rb") as fin:
    bwt_seq = pickle.load(fin)
with open("rank_seq.pickle", "rb") as fin:
    rank_seq = pickle.load(fin)
with open("occ_seq.pickle", "rb") as fin:
    occ_seq = pickle.load(fin)

seq_queries = [
 "CAAAACATTCCCACCAACAG",
 "TCGGGCACGTAGTGTAGCTA",
 "GGCTCAATGTGTCCAGTTAC",
 "GGGAAATTGTTAAATTTATC",
 "AAAACAAGATGATAAGAAAA",
 "TTTAGCTTAGTTGCAGAGTG",
 "TCTTAGCCTACTGTAATAAG",
 "TTTGAACTTGATGAAAGGAT",
 "CCAGGTAACAAACCAACCAA",
 "TGCAGGAATCTTTTGTTGCA",
 "AAGACATGTACGTGCATGGA"
]

perfect_queries = [
 "CAAAACATTCCCACCAACAG",
 "GCGGGCACGTAGTGTAGCTA",
 "GGCTCAATGTGTCCAGTTAC",
 "GGGAAATTGTTAAATTTATC",
 "AAAACAAGATGATAAGAAAA",
 "TTTGGCTTAGTTGCAGAGTG",
 "TCTTAGCCTACTGTAATAAG",
 "TTTGAACTTGATGAAAGGAT",
 "CCAGGTAACAAACCAACCAA",
 "TGCAGCAATCTTTTGTTGCA",
 "AAGACATGTACGTGCATGGA"
]
