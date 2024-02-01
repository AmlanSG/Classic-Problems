n = 8
solutions = []

def Place(k, i):
    for j in range(0, k):
        if solution[j] == i or abs(solution[j] - i) == abs(j - k):
            return False
    return True

def NQueens(k):
    if k == n:
        solutions.append(solution.copy())
        return
    for i in range(0, n):
        if Place(k, i):
            solution.append(i)
            NQueens(k + 1)
            solution.pop()


solution = []
NQueens(0)

print("All possible solutions:")
for idx, sol in enumerate(solutions):
    print(f"Solution {idx + 1}: {sol}")
