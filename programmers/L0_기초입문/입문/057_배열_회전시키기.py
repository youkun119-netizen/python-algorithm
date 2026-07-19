# 배열 회전시키기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 17:23:42

def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]