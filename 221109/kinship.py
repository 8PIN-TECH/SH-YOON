result  = [0]
people = int(input("전체 사람의 수를 입력하세요 : "))
signal = [0] * (people + 1)
while True:
    a, b = map(int, input("비교 대상을 입력하세요 : ").split())
    if 1 <= a <= people and 1 <= b <= people:
        break
    print("정확히 입력하세요.")
count = int(input("관계의 수를 입력하세요 : "))
child = [[] for _ in range(people + 1)]
for _ in range(count):
    while True:
        x, y = map(int, input("관계를 입력하세요 : ").split())
        if 1 <= x <= people and 1 <= y <= people and x != y:
            child[x].append(y)
            child[y].append(x)
            break
        print("정확히 입력하세요.")

def kinship():
    search(a, 0)
    if len(result) == 0:
        print(-1)
    else:
        print(result[0] - 1)

def search(v, cnt):
    cnt += 1
    signal[v] = 1
    if v == b:
        result[0] = cnt
    for i in child[v]:
        if signal[i] != 1:
            search(i, cnt)

if __name__ == '__main__':
    kinship()