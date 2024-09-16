# N X N 인 체스판 위에 퀸 N 개를 서로 공격할 수 없게 놓는 문제
# 경우의 수 count

# n * n 의 n 입력 받기
n = int(input())

# 1 <= n < 15 조건 추가 
if n >= 15:
    print("15 미만으로 입력하세요")
# 15 미만인 경우에만 queen() 진행      
else:
    count = 0 # 경우의 수를 저장할 변수 
    pos = [0] * n # 각 열에 배치된 퀸의 행을 저장하는 배열 
    flag_a = [False] * n # 각 행에 퀸을 배치했는지 체크하는 배열 
    flag_b = [False] * (2*n-1) # ↙↗ 대각선 방향에 퀸을 배치했는지 체크하는 배열
    flag_c = [False] * (2*n-1) # ↘↖ 대각선 방향에 퀸을 배치했는지 체크하는 배열

    def queen(i: int) -> None:
        global count # 경우의 수를 전역 변수로 사용한다고 명시 
                    # count 가 함수 내부에서 값이 변경되기 때문에 global 선언이 필요함 

        # i 열의 가능한 모든 행에 퀸 배치 시도 
        for j in range(n):
            # j 행에 퀸이 배치되지 않았고
            # 대각선 방향에도 퀸이 배치되지 않았다면
            if(      not flag_a[j]
                and not flag_b[i+j]
                and not flag_c[i-j+(n-1)]):
                
                # i 열 j 행에 퀸 배치 
                pos[i] = j

                # 모든 열에 퀸을 배치한 경우 count++
                if i == n-1:
                        count += 1
                else:
                        # 현재 열과 행에 퀸을 배치한 상태로 표시 
                        flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = True
                        # 다음 열에 퀸 배치 
                        queen(i+1)
                        # 현재 상태를 복원하여 다음 시도에 방해되지 않도록 False 로 변경 
                        flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = False

    # 첫번째 열부터 퀸 배치 시ㅡ작!
    queen(0)
    print(count)