n = 8
solution = []
def Place(k, i):
    for j in range(0, k):
        if solution[j] == i or abs(solution[j] - i) == abs(j - k):
            return False
    return True

def NQueens(k):
    if k == n:
        return solution.copy()
    for i in range(0, n):
        if Place(k, i):
            solution.append(i)
            result = NQueens(k + 1)
            if result:
                return result
            solution.pop()

result = NQueens(0)
print(result)