# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 25. 11:59:26

def solution(my_string):
    for char in my_string:
        if not char.isdigit():
            my_string = my_string.replace(char, ' ')
    return sum(int(num) for num in my_string.split())
