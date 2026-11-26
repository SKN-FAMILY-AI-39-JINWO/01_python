""" list

- 컨테이너형(묶다) 자료형이자 시퀀스(순서) 자료형

- 여러 값(literal)을 묶어서 관리

- list에 값이 저장 된 순서(index)를 기억한다. 

- 같은 시퀀스 자료형으로 str, tuple이 있다.

"""

print("---list---")
lst = [10, 20, 30] # int 3개를 저장 한 list

print(f'lst: {lst} - {type(lst)}')
#lst: [10, 20, 30] - <class 'list'>

print(f'lst[0]: {lst[0]} - {type(lst[0])}')
# lst[0]: 10 - <class 'int'>

print("--- list 요소 추가/삭제  ---")
"""
- list는 값을 추가하거나 삭제할 수 있는 
  mutable 자료형이다.

- mutable 자료형: list, set, dict
- immutable 자료형: int, float, bool, str, tuple

"""

print("--- list mutable 확인 ---")
lst = [1, 2, 3, 4]

# id() 함수: 변수에 저장된 값(객체)의 식별코드 반환
print(id(lst)) # 2926031150656

before_id = id(lst)

# list.append(값)
# - 지정된 list 제일 끝에 값 추가
lst.append(5)

after_id = id(lst)

print(lst, id(lst)) # 5 추가 확인, id 유지 확인, [1, 2, 3, 4, 5] 2926031150656
print(before_id == after_id) # 이전, 현재 id 비교, True


print("--- list insert ---")
# 리스트 내부 원하는 위치(index)에 요소 삽입(추가)
lst.insert(0, 0.5)
print("insert 후 lst:", lst) # insert 후 lst: [0.5, 1, 2, 3, 4, 5]

lst.insert(3, 100)
print("insert 후 lst:", lst) # insert 후 lst: [0.5, 1, 2, 100, 3, 4, 5]

lst.insert(7, 777) # 제일 끝
print("insert 후 lst:", lst) # insert 후 lst: [0.5, 1, 2, 100, 3, 4, 5, 777]

lst.insert(10, 999) # 중간에 인덱스 건너 뛰고 삽입
print("insert 후 lst:", lst) # insert 후 lst: [0.5, 1, 2, 100, 3, 4, 5, 777, 999], 제일 끝에 삽입


#list 값 변경
print("=== list update ---")
lst2 = [100, 200, 300]

#1번 인덱스의 값을 2로 변경
lst2[1] = 2
print("변경 후 lst2:", lst2) # 변경 후 lst2: [100, 2, 300]


# 특정 인덱스 값 제거
print("--- list remove ---")
lst3 = ['aaa', 'bbb', 'ccc', 'ddd']

lst3.remove('bbb')
print('remove 후 lst: ', lst3) # remove 후 lst:  ['aaa', 'ccc', 'ddd']


print('--- list pop ---')
# list.pop(index)
# - 지정된 위치의 요소를 제거하고 반환
# - index를 생략하면 마지막 요소를 제거하고 반환
lst4 = [10, 20, 30, 40]
removed = lst4.pop(1)
print("pop 수행 후 lst4: ", lst4) # pop 수행 후 lst4:  [10, 30, 40]
print("removed: ", removed) # removed:  20


# 값 정렬
print('--- list sort ---')
lst5 = [20, 13, 40, 33, 21, 42]

lst5.sort() # 원본 리스트 자체를 정렬

print(lst5) # [13, 20, 21, 33, 40, 42]


lst5.reverse() # 역순으로 뒤집기, 오름차순->내림차순
print(lst5)


#-------------------------------------------------------------------------

""" 다차원 list(1차원 - 2차원 - 3차원, 점 - 선 - 면이 쌓이는 것처럼)
- list의 요소로 list가 존재하는 형태

* 2차원 list
- 1차원 list를 요소로 갖는 list
"""
lst6 = [1,2,3] #1차원
lst7 = [4,5,6] #1차원

lst_2d_1 = [lst6, lst7] #2차원 list

print("--- 2차원 list ---")
lst_2d_1 = [lst6, lst7] #2차원 list
print(lst_2d_1)
# [[1, 2, 3], [4, 5, 6]]

# 2차원 list에서 원하는 요소 얻어오기 
print('lst_2d_1[0][2]: ', lst_2d_1[0][2]) # lst_2d_1[0][2]:  3


# 2차원 리스트에 1차원 리스트[7,8,9] 추가하기
lst_2d_1.append([7,8,9])

print(lst_2d_1) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# 2차원 리스트 내부 1차원 리스트에 값(99) 추가하기
# [[1, 2, 3], [4, 5, 6, 99], [7, 8, 9]]
lst_2d_1[1].append(99)
print("1st_2d_1: ", lst_2d_1)


# 2차원 리스트에서 특정 값(7) 제거
# [[1, 2, 3], [4, 5, 6, 99], [8, 9]]
lst_2d_1[2].pop(0)
print("lst_2d_1: ", lst_2d_1)



students = [
    ['홍길동', 20],
    ['신사임당', 22, '여'],
    ['이순신', 48, '전남', '여수시']
]

print("---student에 저장된 모든 학생 이름만 꺼내기---")

print(students[0][0])
print(students[1][0])
print(students[2][0])


# csv(Comma Separated Value): 콤마로 구분된 값 (문자열 형식)


# str.split(구분자)
# - 문자열 내에서 지정된 구분자를 기준으로 나누어 list 반환
print("--- str.split(구분자) ---")
data = '이순신,48,전남,여수시'

split_data = data.split(',')
print("split 결과: ", split_data, type(split_data)) # split 결과:  ['이순신', '48', '전남', '여수시'] <class 'list'>


# ----------------------------------------------------------

print("--- list 연산 (+ , *) ---")

foods = ['🍗', '🍕', '🍔']
drinks = ['☕', '🥛', '🍶']

foods_drinks = foods + drinks
print('foods_drinks: ', foods_drinks) # foods_drinks:  ['🍗', '🍕', '🍔', '☕', '🥛', '🍶']
print('foods*2:', foods*2) # foods*2: ['🍗', '🍕', '🍔', '🍗', '🍕', '🍔']


# list slicing (문자열과 같은 방법)

print("--- list slicing ---")
texts = ['안녕하세요', 'hello', '곤니찌와', 'bye', '잘가']

print(texts[0:2]) # ['안녕하세요', 'hello']
print(texts[2:]) # ['곤니찌와', 'bye', '잘가']
print(texts[::2]) # ['안녕하세요', '곤니찌와', '잘가']


"""list 반복 순회 (iterable)

- iterable(순회) 가능한 타입: str, list, tuple, set, dict
- iterable(순회)란?
 -> 내부에 저장된 요소를 0번 인덱스 부터 끝까지
    하나씩 꺼낼 수 있게 하는 기술


"""

lst = [10, 20, 30, 40, 50]

# for 변수 in 순회 객체: 
# -> 순회객체에서 요소를 하나씩 꺼내 변수에 저장하여 사용
for e in lst: 
    print("요소:", e)


# 인덱스 순회(지금은 참고만)
for index, e in enumerate(lst):
    print(f"{index} 번째 요소: {e}")



# 자료구조: 데이터 저장 및 산출 순서, 저장 된 모양에 따라 구조에 따라 사용 순서가 달라진다. 
# 변수: 값 1개 저장 구조
# 1차원 list: 값(변수) 여러 개 저장 구조
# 2차원 list: 1차원 list 여러 개 저장 구조 
# stack / queue / deque / 


# list의 remove, pop / del 차이점
# remove, pop은 꺼내는 개념
# del은 아예 제거하는 개념




