# 가위 바위 보
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 21:33:47

def solution(rsp):
    i = {'0':'5', '2':'0', '5':'2'}
    return ''.join(i[char] for char in rsp)
        
        