while True:
    _number_count = int(input("숫자를 입력하세요 : "))
    if 1 < _number_count < 200:
        break
    else:
        print("1 < X < 200 범위 안에 정확한 숫자를 입력하세요.")

for _number_bLank in range(_number_count):
    _number_star = (_number_count * 2) - (_number_bLank * 2) - 1
    for i in range(_number_bLank):
        print(" ", end="")
    for j in range(_number_star):
        print("*", end="")
    print("")

for x in range(1, _number_count):
    _number_bLank = _number_count - x - 1
    _number_star = (_number_count * 2) - (_number_bLank * 2) - 1
    for i in range(_number_bLank):
        print(" ", end="")
    for j in range(_number_star):
        print("*", end="")
    print("")