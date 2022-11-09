def hanoi():
    """
    hanoi 함수
    """
    circle = inputcircle()
    movement(circle)
    signal = 1
    stack = [circle, 1, 2, 3]
    while stack:
        """
        원판이 소진될 때까지 반복하며, 원판이 1이 될 때까지 순서를 저장한다
        """
        end = stack.pop()
        asis = stack.pop()
        start = stack.pop()
        circle = stack.pop()
        if circle == 1: # 원판1을 목표지점으로 움직인다.
            print(start, '>', end)
            signal = 0
            continue
        if signal == 0: # 원판1을 움직이고 다음 차례
            print(start, '>', end)
            signal = 1
            stack.append(circle - 1)
            stack.append(asis)
            stack.append(start)
            stack.append(end)
            continue
        stack.append(circle)
        stack.append(start)
        stack.append(asis)
        stack.append(end)
        if signal != 0: # 원판 갯수가 짝수일 경우 보조지점부터 첫 원판을 빼줘야 함, 이후 순서를 섞는 과정
            stack.append(circle - 1)
            stack.append(start)
            stack.append(end)
            stack.append(asis)

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