# 두 수의 나눗셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120806
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 17. 13:48:02

def solution(num1, num2):
    if (0 < num1 <= 100) and (0 < num2 <= 100):
        return int(num1/num2*1000)