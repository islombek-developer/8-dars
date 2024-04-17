def kvadrat(x):
    print(x**2)

if __name__ == "__main__":
    kvadrat()

def ayrish(x):
    print(x-2)

if __name__ == "__main__":
    ayrish()

def bolish(x):
    print(x//2)

if __name__ == "__main__":
    bolish()
# 
# 
# 
# 
# # def xay_diff(a, b):
#     return [x for x in a if x not in b]
# print(xay_diff([1,2,2,2,3], [2]))  

# xay_diff = lambda a, b: [x for x in a if x not in b]
# print(xay_diff([1,2,2,2,3], [2]))

# def f(t,d):
#     s=''
#     if len(t) > len(d):
#         s+=t[len(d):]
#     elif len(t) < len(d):
#         s+=d[len(t):]
#     return s
# print(f('abcde' ,'abcd'))

# def quicksort(x):
#     if len(x) <= 1:
#         return x
#     else:
#         a = x[0]
#         lesser = [x for x in x[1:] if x <= a]
#         greater = [x for x in x[1:] if x > a]
#         return quicksort(lesser) + [a] + quicksort(greater)

# x = [3, 6, 8, 10, 1, 2, 1]
# sorted_x = quicksort(x)
# print(sorted_x)

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# number=[13, 27, 50, 58, 58, 86, 87, 101, 107, 107, 116, 117, 121, 145, 146, 149, 
#         159, 170, 184, 189, 197, 199, 226, 234, 235, 236, 237, 240, 252, 265, 
#         276, 289, 301, 322, 338, 358, 383, 385, 398, 406, 413, 414, 420, 423, 425, 
#         426, 428, 431, 436, 472, 475, 482, 487, 492, 494, 513, 523, 529, 566, 568, 
#         576, 576, 599, 599, 600, 609, 617, 624, 633, 644, 646, 654, 661, 698, 712, 
#         719, 728, 728, 762, 783, 799, 826, 828, 832, 847, 849, 880, 880, 890, 893, 
#         906, 911, 923, 924, 934, 943, 973, 974, 984]
# def f(target,sorted_list):
#     start=0
#     end=len(sorted_list)-1
#     while start<=end:
#         mid = (start+end)//2
#         mid_value=sorted_list[mid]
#         if mid_value==target:
#             return mid
#         elif mid_value<target:
#             start = mid + 1
#         elif  mid_value>target:
#             end = mid-1

# print(f(184,number))

# number=[3,5,2,6,9,8,7,4,1]
# def f(sorted_list):
#     n=len(sorted_list)
#     for i in range(n):
#         for j in range(0,n-1):
#             if sorted_list[j]>sorted_list[j+1]:
#                 sorted_list[j],sorted_list[j+1]=sorted_list[j+1],sorted_list[j]

#     return sorted_list

# print(f(number))










