def maze():
    print("test")

if __name__ == '__main__':
    x, y = map(int, input("미로의 크기를 입력하세요. : ").split())
    road = []
    for _ in range(x):
        road.append(list(map(int,input())))
    print(road[2][2])
    maze()
