def select_non_overlapping_segments(n, segments):
    # 선분을 끝점을 기준으로 정렬
    segments.sort(key=lambda x: x[1])

    # 선택된 선분의 끝점 초기화
    end_point = -1
    # 겹치지 않게 선택된 선분의 수 초기화
    count = 0

    for segment in segments:
        start, end = segment
        # 이전에 선택한 선분의 끝점보다 현재 선분의 시작점이 크거나 같으면 선택
        if start >= end_point:
            end_point = end
            count += 1

    return count

# 입력 받기
n = int(input())
segments = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

# 결과 출력
result = select_non_overlapping_segments(n, segments)
print(result)