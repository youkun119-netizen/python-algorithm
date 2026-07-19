# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 15:31:16

def solution(array):
    return max(array), array.index(max(array))