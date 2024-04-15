# def xay_diff(a, b):
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
