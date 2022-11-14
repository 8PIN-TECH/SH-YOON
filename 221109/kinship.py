people = 0
a = 0
b = 0
count = 0
result = []

def kinship():
    people = int(input("전체 사람의 수를 입력하세요 : "))
    while True:
        a, b = int(input("비교 대상을 입력하세요 : ").split())
        if 1 <= a <= people and 1 <= b <= people:
            break
        print("정확히 입력하세요.")
    count = int(input("관계의 수를 입력하세요 : "))
    for _ in range(count):
        while True:
            x, y = input("관계를 입력하세요 : ").split()
            if 1 <= x <= people and 1 <= y <= people and x != y:
                break
            print("정확히 입력하세요.")
        kinship[x].append(y)
        kinship[y].append(x)
    search(a, 0)
    if len(result) == 0:
        print(-1)
    else:
        print(result[0])

def search(a, cnt):
    cnt += 1
    if a == b:
        result[0] = cnt
    for i in kinship[a]:
        search(i, cnt)

if __name__ == '__main__':
    kinship()