# class Iterator:
#     def __init__(self, start,end):
#         self.current=start
#         self.end=end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current<=self.end:
#             result=self.current
#             self.current+=1
#             return result
#         else:
#             raise StopIteration
# number=Iterator(1,5)
# for num in number:
#     print(num)
# class Iterator:
#     def __init__(self,listofnumbers):
#         self.current=0
#         self.end=len(listofnumbers)-1
#         self.listofnumbers=listofnumbers

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current<=self.end:
#             result=self.listofnumbers[self.current]
#             self.current+=1
#             return result
#         else:
#             raise StopIteration
# my_numbers=Iterator([1,2,4,5,8,69,63,4,5])
# s=[]
# for i in my_numbers:
#     s.append(i)
# print(s)
class CustomRange:
    def __init__(self,start,end,step=None):
        self.current=start
        self.end=end
        self.step=step
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.end:
            result=self.current
            if self.step is None:
                self.current+=1
            else :
                self.current+=self.step
            return result
        else:
            raise StopIteration
my_numbers=CustomRange(4,10)
for i in my_numbers:
    print(i)

