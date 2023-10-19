# def linearsearch():
#     nums = []
#     idx = 0
#     
#     limit = int(input("How many numbers in the list"))
#     for x in range(limit):
#         nums.append(int(input("Input number")))
#         x += 1
#     search = int(input("Input the number you are looking for"))
#     
#     for x in nums:
#         if x == search:
#             print(idx)
#         else:
#             idx += 1
# linearsearch()

# def sortlist(unsortlist):
#     sortedlist = []
#     
#     while len(unsortlist) != 0:
#         smallest = 9999999
#         for x in unsortlist:
#             if x<smallest:
#                 smallest = x
#         sortedlist.append(smallest)
#         unsortlist.remove(smallest)
#     return sortedlist

# def binarysearch():
#     nums = []
#     limit = int(input("How many numbers in the list"))
#     for x in range(limit):
#         nums.append(int(input("Input number")))
#         x += 1
#     search = int(input("Input the number you are looking for"))
#     low = 0
#     high = limit-1
#     mid = (low+high)//2
#     sortedlist = sortlist(nums)
#     while sortedlist[mid] != search:
#         if sortedlist[mid] < search:
#             low = mid + 1
#         else:
#             high = mid - 1
#         mid = (low+high)//2
#     print(sortedlist[mid])
# binarysearch()


# def linearsearchrec(idx,nums,search):
#     if idx == 0:
#         nums = []
#         limit = int(input("How many numbers in the list"))
#         for x in range(limit):
#             nums.append(int(input("Input number")))
#             x += 1
#         search = int(input("Input the number you are looking for"))
#     if idx == len(nums):
#         return -1
#     elif nums[idx] == search:
#         return idx
#     else:
#         return linearsearchrec(idx+1,nums,search)
# print(linearsearchrec(0,[],0))

# def binarysearchrec(mid,low,high,counter,sortedlist,search):
#     if counter == 0:
#         nums = []
#         limit = int(input("How many numbers in the list"))
#         for x in range(limit):
#             nums.append(int(input("Input number")))
#             x += 1
#         search = int(input("Input the number you are looking for"))
#         low = 0
#         high = limit-1
#         mid = (low+high)//2
#         sortedlist = sortlist(nums)
#     if sortedlist[mid] == search:
#         return sortedlist[mid]
#     elif sortedlist[mid] < search: 
#         low = mid + 1
#         mid = (low+high)//2
#         return binarysearchrec(mid,low,high,counter+1,sortedlist,search)
#     else:
#         high = mid - 1
#         mid = (low+high)//2
#         return binarysearchrec(mid,low,high,counter+1,sortedlist,search)
# print(binarysearchrec(0,0,0,0,[],0))



















