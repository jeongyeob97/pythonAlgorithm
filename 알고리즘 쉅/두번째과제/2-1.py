import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
k = int(input())

start, end = 0, n-1

#이진탐색 함수
def binary_search(start, end, num):
    left = start
    right = end

    #left가 right보다 커질 때까지 반복
    while left <= right:
        #중간값 설정
        mid = (left + right) // 2
        temp_num = list1[mid]

        #중간 값이 찾고자 하는 값보다 클 때 right변수 mid-1로 갱신
        if (temp_num > num):
            right = mid - 1
        # 중간 값이 찾고자 하는 값보다 작을 때 left변수 mid+1로 갱신
        else:
            left = mid + 1
    return left, right

left, right = binary_search(start,end,k)

#left가 list1의 길이보다 크면 list1[right] 출력
if left >= len(list1):
    print(list1[right])
elif right >= 0:
    # 가장 가까운 값을 얻는 것이기 때문에 절대값을 이용해 절대값이 가장 작은 수를 출력한
    if abs(k-list1[right]) <= abs(k-list1[left]):
        print(list1[right])
    else:
        print(list1[left])다
#right가 음수이면 원하는 값을 못 얻기 때문에 list1[left] 출력
else:
    print(list1[left])