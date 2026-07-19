# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 14:18:29

from itertools import combinations as comb

def solution(numbers):
    an_list = []
    for i, j in comb(numbers, 2):
        an_list.append(i*j)
        
    return max(an_list)