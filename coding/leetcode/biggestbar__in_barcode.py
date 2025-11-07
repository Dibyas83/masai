
# find biggest rectangle in barcode
# if right side is bigger then left ponter can be extended,if less pop the curr height,and
# all the heights less than it and before it
# use stack to pop frm top ,heights = [2,1,5,6,2,3] = height * breadth
# 2*1,pop 2 1*2,5>2 pop 1 5*1,5*2,2*3 < 5*2,2*4< 5*2 ,so ans is 5*2
# make cols of index,height(min * breadth) and max area produced , recalcuate area if bigger upto that index height that has to be extended backward

class Solut:
    def largest_rec(self,heights: list[int]) -> int:
        maxArea = 0
        stack = [] #  in pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # stack not empty and top val of stack > curr_height in list.then we have to pop our stack and chech the max rectangle we can  create from that height by extending curr_height backwards
                index, height = stack.pop()
                maxArea = max( maxArea, height * (i - index)) # 9*1,8*2,7*3 gradually poping, after popping index of height = or smaller is known
                start = index # start is the index from back from where area is recalculated
                print(stack, maxArea)
            stack.append((start,h))

        print("-----------------------")
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            print(stack, maxArea)
        return maxArea

bars =[1,2,2,4,6,2,7,8,9,1,2,6]
j= Solut()
print(j.largest_rec(bars))


