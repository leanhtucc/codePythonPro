def swap_even_and_odd_positions(arr):
    length = len(arr)
    if length % 2 == 0:
        end = length
    else:
        end = length - 1

    for i in range(0, end, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr

# Thử nghiệm chương trình
original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_array = swap_even_and_odd_positions(original_array)

print("Mảng ban đầu:", original_array)
print("Mảng sau khi hoán đổi:", result_array)
