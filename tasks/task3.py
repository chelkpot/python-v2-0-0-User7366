# tasks/task3.py

def solve():
    a, b = map(int, input().split())

    n = a + b - 1

    print(n - a, n - b)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()