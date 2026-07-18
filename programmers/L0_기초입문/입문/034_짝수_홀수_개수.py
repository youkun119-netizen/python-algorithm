# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 17:16:25

def solution(num_list)->int:
    even_count = len([x for x in num_list if x % 2 == 0])
    odd_count = len([x for x in num_list if x % 2 == 1])
    return [even_count, odd_count]