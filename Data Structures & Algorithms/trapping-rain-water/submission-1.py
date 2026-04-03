class Solution:
    def trap(self, height: List[int]) -> int:
        # - using 2 pointers at both side
        # - at both side cant contain water because of no 
        # wall so move immediately the shorter one to find more water
        # it can trap inside
        # - only need to know the shortest wall side to know how much water it 
        # can contain

        # inintilize 2 pointers and 2 maxSides
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        water_area = 0

        # the loop stop when 2 pointers meet
        while l < r:
            # - the farther the pointer the more it can contain water
            # so move inside the shorter side to find the higher wall so it 
            # can contain more water
            # - move maxLeft so when we calculate we know that
            # the side we just move is the shorter side
            # from that we can calculate immediately without checking
            if maxLeft < maxRight:
                l +=1
                maxLeft = max(maxLeft, height[l])
                water_area += maxLeft - height[l]
            else:
                r-=1 
                maxRight = max(maxRight, height[r])
                water_area += maxRight - height[r]
        
        return water_area

# Time: O(N)
# Space: O(1)




# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # using 2 pointers start next to each other
#         water_area = 0
#         i = 0
#         while i in range(len(height)):
#             if (height[i] == 0):
#                 continue
#             j = i + 1
#             temp = 0
#             # with this it evaluate left first and saw out of index 
#             # lesson: left always come first
#             while j < len(height) and height[i] > height[j]:
#                 # plus all the height in the middle
#                 temp += height[j]
#                 # increase to find the >= height
#                 j += 1
#                 continue

#             if (j == len(height)):
#                 i += 1
#                 continue

#             # calcualte water area when find height[i] <= height[j]
#             lower_pointer = min(height[i], height[j])
#             water_area += lower_pointer * (j-i-1) - temp
#             temp = 0
#             i = j

#         print(water_area)
#         return water_area    