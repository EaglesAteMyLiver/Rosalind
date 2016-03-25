#!/usr/bin/env python3
# Rosalind PERM - eaml

def all_permutations(items):
    result = []
    for item in items:
        other = [i for i in items if i is not item]
        permutations = all_permutations(other)
        for permutation in permutations:
            result.append([item] + permutation)
        if not permutations:
            result.append([item])
    return result

if __name__ == "__main__":
    n = int(input("> "))
    permutations = all_permutations(range(1, n+1))
    print(len(permutations))
    for permutation in permutations:
        print(" ".join(map(str, permutation)))
