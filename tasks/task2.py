# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input("").split())
    
    ac = 3
    bc = ac+2
    cc = bc+7

    print ((ac * a) + (bc * b) + (cc * c))
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()