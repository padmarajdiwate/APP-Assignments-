def longest_common_subsequence(first: str, second: str):
    rows, cols = len(first), len(second)
    table = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if first[i - 1] == second[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    result = []
    i, j = rows, cols

    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            result.append(first[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return table[rows][cols], "".join(reversed(result))


length, subsequence = longest_common_subsequence("STONE", "LONGEST")

print(f"Length: {length}, Subsequence: {subsequence}")