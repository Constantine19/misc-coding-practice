

def two_sum_n(num_list, target):
    compliments = {}
    for i in range(len(num_list)):
        compliment = target - num_list[i]
        if compliment in compliments:
            return i, compliments[compliment]
        else:
            compliments[num_list[i]] = i

    return -1


def two_sum_squared(num_list, target):
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            value = num_list[i] + num_list[j]
            if value == target and num_list[i] != num_list[j]:
                return i, j
            else:
                continue
    return -1


def two_sum_nlogn(num_list, target):
    num_list_sorted = sorted(num_list)
    left = 0
    right = len(num_list)-1

    while left <= right:
        if num_list_sorted[left] + num_list_sorted[right] > target:
            right -= 1
        elif num_list_sorted[left] + num_list_sorted[right] < target:
            left += 1

        elif num_list_sorted[left] + num_list_sorted[right] == target:
            return num_list.index(num_list_sorted[left]), num_list.index(num_list_sorted[right])

        else:
            return -1


num_list = [0, 0, 3, 4]
target = 0


print two_sum_n(num_list, target)
print two_sum_squared(num_list, target)
print two_sum_nlogn(num_list, target)