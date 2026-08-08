# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 08. 17:27:59

def solution(s):
    stack = []
    for char in s.split():
        if char == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(char))
    return sum(stack)