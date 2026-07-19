# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 15:54:09

def solution(num, k)->int:
    str_num = str(num)
    str_k = str(k)
    if str_k in str_num:
        return str_num.index(str_k) + 1
    else:
        return -1