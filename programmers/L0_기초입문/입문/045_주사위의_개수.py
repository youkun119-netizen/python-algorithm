# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 13:26:49

def solution(box, n):
    x, y, z = box
    return (x//n)*(y//n)*(z//n)