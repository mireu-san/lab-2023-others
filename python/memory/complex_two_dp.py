# note: DP in algorithm seems complex. Take this as a mid-term problem.


def longest_increasing_subsequence(seq):
    if not seq:
        return 0

    dp = [1] * len(seq)  # dp[i] is the length of the LIS ending at seq[i]

    for i in range(len(seq)):
        for j in range(i):
            if seq[i] > seq[j]:  # say if it increases
                dp[i] = max(dp[i], dp[j] + 1)  # to compare the value of the current LIS
                # and the previous LIS plus 1 and select the larger value
                # note: previous LIS indicates 'dp[j]'
                # to say; this j is always less than i.
                # so, j refers to i(previous position in sequence)
                # that + 1 accounts for including seq[i] in this subsequence.

    return max(dp)  # max value of dp is the length of LIS


# Example usage
seq = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(seq))
