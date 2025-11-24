# https://www.acmicpc.net/problem/4779

# 칸토어 집합은 0 과 1 사이의 실수로 이루어진 집합으로,
# 구간 [0, 1] 에서 시작해서 각 구간을 3등분하여
# 가운데 구간을 반복적으로 제외하는 방식으로 만든다

# - 가 3^N 개 있는 문자열에서 시작하여
# 모든 선의 길이가 1 이면 멈추는 프로그램
# 0 <= N <= 12 정수

import sys


def cantor(n):
    if n == 0:
        return "-"
    prev = cantor(n - 1)
    # Prev 사이에 가운데 구간 3^(N-1) 길이만큼 공백 넣어주기
    return prev + (" " * (3 ** (n - 1))) + prev


if __name__ == "__main__":

    for line in sys.stdin:  # 한 줄씩 읽기
        line = line.strip()
        if not line:  # 빈 줄 건너뛰기
            continue
        n = int(line)
        print(cantor(n))
