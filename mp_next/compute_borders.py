def compute_borders(x: str, m: int):
    border = [0] * (m + 1)
    border[0] = -1
    for i in range(m):
        j = border[i]
        while (j >= 0) and (x[i] != x[j]):
            j = border[j]
        border[i + 1] = j + 1
    return border

print("Enter the string to compute borders for: ")
input_string = input()
result = compute_borders(input_string, len(input_string))
print("Values for NP_next table are: ", result)
    