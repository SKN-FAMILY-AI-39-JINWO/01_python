
# 변수(variable)
# - 값을 저장하는 메모리 공간
# - 변수 선언과 동시에 값(literal)을 할당할 수 있다.

# 변수 선언과 동시에 대입
a = 10 # a변수에 10을 저장(대입)한다. 
b = "홍길동" 

num = a # num 변수에 a(10) 대입

print('a: ', a)
print('b: ', b)
print('num: ', num)


# 대소문자 구분 확인
name = "이순신"
NAME = "홍길동"
print(name, NAME)


#변수명은 snake casing을 사용한다.
show_me_the_money = 10000
print('show me the money: ', show_me_the_money)


#한글 변수명을 지정할 수 있다.(하지만 사용하지 않는다.)
우리반 = "SKN_AI_39"
print(우리반)


#언더바(_)를 제외한 특수문자를 사용할 수 없고, 숫자로 시작할 수 없다.
#1st_user = "김개똥"
_1st_user = "김개똥"
print(_1st_user)

#second! = '김철수'
#print(second!) 


#파이썬 예약어(if, elif, else, for, while, …)를 사용할 수 없다.
import keyword
print(keyword.kwlist)

#False=100

#직관적인 변수명을 사용한다.
a = 100
num1 = 100
name = "이름"





