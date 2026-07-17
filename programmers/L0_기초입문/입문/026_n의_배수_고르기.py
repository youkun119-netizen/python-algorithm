# n의 배수 고르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 17. 20:58:21

def solution(n, numlist):
    return list(filter(lambda x: x % n == 0, numlist))