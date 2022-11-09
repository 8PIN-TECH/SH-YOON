def kinship():
    people = int(input("전체 사람의 수를 입력하세요 : "))
    while True:
        a, b = input("비교 대상을 입력하세요 : ").split()
        if 1 <= a <= people and 1 <= b <= people:
            break
        print("정확히 입력하세요.")
    count = int(input("관계의 수를 입력하세요 : "))
    for _ in range(count):
        x, y = input("관계를 입력하세요 : ").split()




if __name__ == '__main__':
    kinship()