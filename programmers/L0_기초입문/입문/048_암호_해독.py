# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 14:27:26

def solution(cipher, code):
    return cipher[code -1:: code]