# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 16:38:18

def solution(my_string):
    answer = ''
    for i in my_string: 
        if i not in ["a", "e", "i", "o", "u"]:
            answer += i
    return answer