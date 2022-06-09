def binary_search(value,arr):
    
    arr.sort()
    split_char = round((len(arr) -1) / 2)
    upper_limit = len(arr) -1
    lower_limit = 0
    
    if value < arr[lower_limit] or value > arr[upper_limit]:
        return -1

    while arr[int(split_char)] != value:
        split_char = round(int(upper_limit + lower_limit) /2)
        if value > arr[int(split_char)]:
            lower_limit = split_char + 1
        elif value < arr[int(split_char)]:
            upper_limit = split_char -1
        else:
            return split_char


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=--=-=-=
# orignal test code

# def binary_search(value,arr):
#     arr.sort()
#     split_char = round((len(arr) -1) / 2)
#     upper_limit = len(arr) -1
#     lower_limit = 0
    
#     if value < arr[lower_limit] or value > arr[upper_limit]:
#         return -1

#     while arr[int(split_char)] != value:
#         split_char = round(int(upper_limit + lower_limit) /2)
#         if value > arr[int(split_char)]:
#             lower_limit = split_char + 1
#         elif value < arr[int(split_char)]:
#             upper_limit = split_char -1
#         else:
#             if value > lower_limit and value < upper_limit:
#                 return -1
#             else:
#                 return split_char
            
#     return split_char

# --=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-