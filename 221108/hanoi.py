def hanoi():
    """
    hanoi 함수
    """
    circle = inputcircle()
    movement(circle)
    printcircle(circle, 1, 3, 2)

def printcircle(circle, start, end, asis):
    """
    hanoi 실행시 원판의 이동 경로 출력
    :param circle   :원판갯수
    :param start    :시작지점
    :param end      :목표지점
    :param asis     :보조지점
    """
    if circle == 1: # 원판이 1개일 때 바로 목표지점에 놓는다
        print(start," > ",end)
        return
    printcircle(circle - 1, start, asis, end) # 원판이 1개 이상일 때 처음 원판을 보조지점에 놓는다
    print(start," > ",end)
    printcircle(circle - 1, asis, end, start) # 보조지점에 놓았던 원판을 목표지점에 놓는다

def inputcircle():
    """
    원판의 갯수 입력
    :return: 원판의 갯수
    """
    while True:
        circle = int(input("갯수를 입력하세요 : "))
        if 1 <= circle and circle < 100:
            return circle
        print("1 <= X < 100 범위 안에 정확한 갯수를 입력하세요.")

def movement(circle):
    """
    원판의 이동 횟수
    :param circle: 원판의 갯수
    """
    count = 2 ** circle - 1
    print(count,"번 이동하였습니다.")

if __name__ == '__main__':
    hanoi()