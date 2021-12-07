import random
import time

def naive_matching(pattern: str, text: str) -> bool:
    for i in range(len(text)-len(pattern)+1):
        j = 0
        for j in range(len(pattern)):
            if pattern[j] != text[i+j]:
                break
            j += 1
        if j == len(pattern):
            return True
    return False

def pretty_tsv(rows: list) -> None:
    cmax = [0]*len(rows[0])
    for row in rows:
        for i, c in enumerate(row):
            cmax[i] = max(len(c), cmax[i])
    ls = []
    pad = lambda x, y: x.ljust(y)
    for row in rows:
        s = ''
        for i, c in enumerate(row):
            s += pad(c, cmax[i]) + '  '
        ls.append(s)
    return ls

def print_table(s, sa, bwt, rank):
    if bwt == None: bwt = [""] * len(sa)
    if rank == None: rank = [""] * len(sa)

    rows = []
    rows.append(["i", "SA[i]", "S[SA[i]:]", "F", "L", "Rank"])
    for i in range(len(s)):
        l = list(map(str, [i, sa[i], s[sa[i]:], s[sa[i]], bwt[i], rank[i]]))
        rows.append(l)
    pretty_rows = pretty_tsv(rows)
    [print(l) for l in pretty_rows]

def timeit(func, *args) -> None:
    t0 = time.perf_counter()
    func(*args)
    t1 = time.perf_counter()
    print(f'{t1-t0} seconds')


def random_seq(size: int) -> str:
    return "".join([random.choice("ACGT") for _ in range(size)])
