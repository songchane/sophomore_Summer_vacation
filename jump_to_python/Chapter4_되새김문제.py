#01. 홀수, 짝수 판별하기
# 주어진 자연수가 홀수인지, 짝수인지 판별해 주는 함수 is_odd를 작성, 홀수이면 True, 짝수이면 False를 리턴
import fileinput

print("1번 문제")
def id_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(id_odd(6))

# print("람다 함수로 표현")
is_odd = lambda x: True if x % 2 == 1 else False

print("="*30)

# 02. 모든 입력의 평균값 구하기
# 입력으로 들어오는 모든 수의 평균값을 계산해주는 함수를 작성, 단, 입력으로 들어오는 수의 개수는 정해져 있지 않음
print("2번 문제")
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2,3,4,5))

print("="*30)

# 03.프로그램 오류 수정하기 1
# 다음은 2개의 숫자를 입력 받아 더한 후에 리턴하는 프로그램, 위 프로그램을 올바르게 수정
# input으로 받은 숫자는 String 타입임을 주의!!
print("3번 문제")
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다" %total)

print("="*30)

# 04. 출력 결과가 다른 것은?
# 다음 중 출력 결과가 다른 것은?
print("4번 문제")
print("3번")

print("="*30)

# 05. 프로그램 오류 수정하기 2
# 다음은 파일(test.txt)에 "Life is too short" 문자열로 저장 후 다시 그 파일을 읽어 출력하는 프로그램이다, 올바르게 수정해보자
print("5번 문제")

f1 = open("C:/Users/lcsdc/PycharmProjects/pythonProject/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

print("="*30)

# 06. 사용자 입력 저장하기
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램 작성, 프로그램을 다시 실행하더라고 기존 작성 내용을 유지, 새로 입력한 내용 추가
print("6번 문제")
user_input = input("저장할 내용을 입력하세요:")
f = open("C:/Users/lcsdc/PycharmProjects/pythonProject/test.txt", 'a')
f.write("\n")
f.write(user_input)
f.close()

print("="*30)

# 07. 파일의 문자열 바꾸기
# 다음과 같은 내용을 지닌 test.txt가 있다. 이 파일의 내용 중 "java"를 "python"으로 바꾸어 저장해보자
print("7번 문제")
f = open("C:/Users/lcsdc/PycharmProjects/pythonProject/test.txt", 'r')
body = f.read()
f.close()
body = body.replace('java', 'python')
f = open("C:/Users/lcsdc/PycharmProjects/pythonProject/test.txt", 'w')
f.write(body)
f.close()

print("="*30)

# 08. 입력값을 모두 더해 출력하기
# 다음과 같이 실행할 때 입력값으 모두 더해 출력하는 스크립트 작성
print("cd doit => python myargv.py 1 2 3 4 5 6 7 8 9 10")



