import random

"""
### [목표]

플레이어는 지도 상에서 보물을 찾아야 합니다. 지도는 그리드로 구성되며, 플레이어는 매 턴마다 이동하여 보물의 위치를 찾아야 합니다. 보물의 위치는 무작위로 설정됩니다.

### [게임 설명]

1. 게임 시작 시, 프로그램은 N x N 크기의 그리드를 생성하고, 그리드 내에 무작위 위치에 보물을 배치합니다.
2. 플레이어는 그리드 내의 특정 위치에서 시작합니다. 초기 위치도 무작위로 결정됩니다.
3. 플레이어는 북(N), 남(S), 동(E), 서(W) 중 하나의 방향으로 한 칸 이동할 수 있습니다.
4. 이동 후, 플레이어는 보물까지의 대략적인 거리를 알 수 있습니다. 정확한 위치는 알 수 없습니다.
5. 플레이어가 보물 위치에 도달하면 게임이 종료되고, 이동 횟수가 공개됩니다.

### [기능 요구 사항]

- **그리드 생성**: N x N 크기의 게임 보드를 생성합니다.
- **보물 및 플레이어 위치 초기화**: 보물과 플레이어의 위치를 무작위로 설정합니다.
- **이동 명령 수행**: 플레이어로부터 이동 명령을 입력받아 수행합니다.
- **거리 힌트 제공**: 플레이어에게 현재 위치에서 보물까지의 거리에 대한 힌트를 제공합니다.
- **게임 종료 조건 확인**: 플레이어가 보물을 찾으면 게임을 종료합니다.

### [개발 단계]

1. **게임 환경 설정**: 필요한 변수(보드 크기, 위치 정보 등)와 게임 보드를 초기화합니다.
2. **플레이어 입력 처리**: 플레이어로부터 이동 명령을 입력받고, 입력에 따라 플레이어의 위치를 업데이트합니다.
3. **거리 계산 및 힌트 제공**: 현재 플레이어 위치에서 보물까지의 거리를 계산하고, 이를 기반으로 힌트를 제공합니다.
4. **게임 종료 및 결과 출력**: 플레이어가 보물 위치에 도달하면 게임을 종료하고, 플레이어의 이동 횟수를 출력합니다.
"""
# 게임 초기화
def initialize_game():
    n = int(input('보드 사이즈를 입력해주세요'))
    board_size = n * n
    treasure_position = random.randint(0, board_size - 1)
    player_position = random.randint(0, board_size - 1)

    # 플레이어와 보물 위치가 같으면 새 위치 설정
    while player_position == treasure_position:
        player_position = random.randint(0, board_size - 1)

    # 1차원 인덱스를 2차원 좌표로 변환
    treasure_pos = (treasure_position // n, treasure_position % n)
    player_pos = (player_position // n, player_position % n)

    return n, treasure_pos, player_pos

# 거리 계산
def calculate_distance(treasure_pos, player_pos):
    treasure_x, treasure_y = treasure_pos
    player_x, player_y = player_pos
    # 맨해튼 거리 계산
    distance = abs(treasure_x - player_x) + abs(treasure_y - player_y)
    if distance == 1:
        print('탐지기가 시끄럽게 울립니다!\n보물의 위치가 매우 가깝습니다!!')
    elif distance < 4:
        print('탐지기가 반응을 보입니다!')
    elif distance >= 4:
        print('탐지기에 반응이 없습니다...')

# 보드 그리드 생성
def draw_grid(n, player_pos, treasure_pos):
    horizontal_line = "+---" * n + "+"  # 각 행의 상단 경계를 만듭니다.
    vertical_line = "|   " * n + "|"   # 각 행의 셀 경계를 만듭니다.
    
    grid = ""
    for y in range(n):
        vertical_line = ""
        for x in range(n):
            if (x, y) == player_pos:
                vertical_line += "| P "  # 플레이어 위치5
            elif(x, y) == treasure_pos:
                vertical_line += "| O "  # 보물 위치(실제 게임 플레이시 주석처리 하기)
            else:
                vertical_line += "|   "  # 빈 셀
        vertical_line += "|"  # 마지막 셀 마무리
        grid += horizontal_line + "\n"  # 상단 경계 추가
        grid += vertical_line + "\n"   # 셀 내부 추가
    grid += horizontal_line  # 마지막 행의 하단 경계 추가
    return grid

# 플레이어 이동
def move_player(player_pos, n):
    player_x, player_y = player_pos
    move = input('이동 할 위치를 적어주세요(동: E, 서: W, 남: S, 북: N)')
    if move == "E" and player_x < n - 1:
        player_x += 1
    elif move == "W" and player_x > 0:
        player_x -= 1
    elif move == "S" and player_y < n - 1:
        player_y += 1
    elif move == "N" and player_y > 0:
        player_y -= 1
    else:
        print("잘못된 이동이거나 보드 경계를 벗어났습니다!")
        
    return (player_x, player_y)

# 게임 실행
def play_game():
    n, treasure_pos, player_pos = initialize_game() # 다른 함수에 쓸 값 받아오기
    play_count = 0

    # 보물을 찾을 때까지 무한 반복
    while player_pos != treasure_pos:
        print(draw_grid(n, player_pos, treasure_pos))
        calculate_distance(treasure_pos, player_pos)
        player_pos = move_player(player_pos, n)
        play_count += 1

    # 보물을 찾았을 때 최종 위치 알려주기
    print(draw_grid(n, player_pos, treasure_pos))
    print(f"축하합니다! 보물을 찾았습니다! 총 이동 횟수: {play_count}번")

# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    play_game()