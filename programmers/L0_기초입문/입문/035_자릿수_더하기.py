# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 17:39:20

def solution(n):
    return sum(int(digit) for digit in str(n))