# 01. 조건문의 참과 거짓
# 다음 코드의 결괏값은?
print("1번 문제")
a = "Life is too short, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

print("결괏값: shirt")

print("="*30)


# 02. 3의 배수의 합 구하기
# while문을 사용해 1부터 1000까지 자연수 중 3의 배수 합을 구해라
print("2번 문제")

last = 0
i = 1
while i <= 1000:
    if i%3 == 0:
        last += i
    i += 1
print(last)

print("="*30)

# 03. 졀 표시하기
# while문을 사용하여 다음과 같이 별을 표시하는 프로그램을 작성
print("3번 문제")
i = 0
while True:
    i += 1
    if i > 5:
        break
    print("*" * i)

print("="*30)

# 04. 1부터 10까지 출력하기
# for문 이용
print("4번 문제")

for i in range(1,11):
    print(i)

print("="*30)

# 05. 평균 점수 구라기
# A학급에 총 10명의 학생이 있다. 학생들의 중간고사 점수는 [70,60,55,75,95,90,80,80,85,100] for문을 이용해 평균 점수 구하기
print("5번 문제")
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

print("="*30)

# 06. 리스트 컴프레헨션 사용하기
# 다음 소스 코드는 리스트의 요소 중에서 홀수만 골라 2를 곱한 값은 result 리스트에 담는 예제 위 코드를 컴프리헨션을 사용해 표현
print("6번 문제")
numbers = [1, 2, 3, 4, 5]
last = []
for n in numbers:
    if n % 2 == 1:
        last.append(n * 2)
print(last)

print("컴프리헨션 사용 코드")
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)

print("="*30)



