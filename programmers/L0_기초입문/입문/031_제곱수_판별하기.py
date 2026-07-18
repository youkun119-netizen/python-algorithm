# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 16:11:13

def solution(n):
    return 1 if (n**0.5).is_integer() else 2 