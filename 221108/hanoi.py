def hanoi(circle, start, end, asis):
    """
    hanoi 함수
    :param circle   :원판갯수
    :param start    :시작지점
    :param end      :목표지점
    :param asis     :보조지점
    :return:
    """
    if circle == 1:
        """
        원판이 1개일 때 바로 목표지점에 놓는다
        """
        print(start," > ",end)
        return

    hanoi(circle - 1, start, asis, end)
    """
    원판이 1개 이상일 때 처음 원판을 보조지점에 놓는다
    """
    print(start," > ",end)
    hanoi(circle - 1, asis, end, start)
    """
    보조지점에 놓았던 원판을 목표지점에 놓는다
    """

circle = int(input("갯수를 입력하세요 > "))
hanoi(circle, 1, 3, 2)

count = 1
for _ in range(circle):
    """
    원판의 이동 횟수는 2의 n승 - 1
    """
    count = count * 2
print(count - 1,"번 이동하였습니다.")