"""
입력받은 숫자에따라 별을 출력하는 모듈입니다.
"""


def answer():
    """
    정답을 출력하기 위한 함수입니다.
    """
    number_count = inputdata()

    for number_blank in range(number_count):
        printstar(number_blank, number_count)
        print("")

    for number_blank in range(number_count - 2, 0, -1):
        printstar(number_blank, number_count)
        print("")


def inputdata():
    """
    데이터를 입력받는 함수입니다.
    :return: 입력받은 값을 리턴합니다.
    """
    while True:
        number_count = int(input("숫자를 입력하세요 : "))

        if 1 < number_count < 200:
            return number_count

        print("1 < X < 200 범위 안에 정확한 숫자를 입력하세요.")


def printstar(number_blank, number_count):
    """
    별을 출력하기 위한 함수입니다.
    :number_blank 공백 숫자
    :number_count 입력받은 값
    """
    number_star = (number_count * 2) - (number_blank * 2) - 1

    for _ in range(number_blank):
        print(" ", end="")
    for _ in range(number_star):
        print("*", end="")


if __name__ == '__main__':
    answer()
