from compute_borders import compute_borders

def morris_pratt (x: str, y: str, m: int, n: int):
    mp_next = compute_borders(x, m)
    i = 0
    j = 0
    while j < n:
        print("j = ", j, ", i = ", i)  # For Workshop 7, ex 2b
        while (i == m) or ((i >= 0) and (x[i] != y[j])):
            i = mp_next[i]
        i = i + 1
        j = j + 1
        if i == m:
            print(x, " occurs in ", y, " at position ", j - i)

print("Enter pattern x: ")
pattern = input()
print("Enter text y: ")
text = input()
morris_pratt(pattern, text, len(pattern), len(text))