# 두 수의 곱 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120804
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 17. 14:09:06

def solution(num1, num2):
    i = 0
    answer = 0
    while i < num2:
        answer += num1
        i += 1
    return answer
