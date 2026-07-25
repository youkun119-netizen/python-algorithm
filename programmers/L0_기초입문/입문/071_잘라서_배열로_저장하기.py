# 잘라서 배열로 저장하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120913
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 26. 08:32:51

import textwrap
def solution(my_str, n):
    my_string = ""
    answer = textwrap.wrap(my_str, n)
    return answer