def min_scoring_sequence(n):
    scores = [8, 7, 6, 3, 2]

    # minimum number of scores needed to make i
    dp = [float('inf')] * (n + 1)

    # choice
    choice = [0] * (n + 1)

    dp[0] = 0

    #dynamic table
    for i in range(1, n + 1):
        for score in scores:
            if i >= score:
                if dp[i - score] + 1 < dp[i]:
                    dp[i] = dp[i - score] + 1
                    choice[i] = score

    #scoring sequence
    sequence = []
    current = n

    while current > 0:
        score = choice[current]
        sequence.append(score)
        current -= score

    return sequence


def main():
    n = int(input("Enter an integer n > 1: "))

    if n <= 1:
        print("Input must be greater than 1.")
        return

    sequence = min_scoring_sequence(n)

    print("Minimum scoring sequence:")
    print("+".join(map(str, sequence)))
    print("Length of the output is", len(sequence))


main()