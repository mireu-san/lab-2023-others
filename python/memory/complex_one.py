# use of algorithm: longest increasing subsequence
# To figure this out, it is considered
# need to use range, zip, len, max, all


def increasing_subsequence(seq):
    n = len(seq)

    # generate all subsequences
    subsequences = [[] for _ in range(1 << n)]
    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j):
                subsequences[i].append(seq[j])

    # to check whether each subsequence is increasing & find the longest one.
    max_len = 0
    for subseq in subsequences:
        if all(x < y for x, y in zip(subseq, subseq[1:])):
            max_len = max(max_len, len(subseq))

    return max_len


seq = [11, 25, 3, 83, 31, 55, 40, 60, 80]
print(increasing_subsequence(seq))
