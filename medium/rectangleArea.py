'''



'''
class Rectangle:
    def __init__(self, left, right, top, bottom):
        self.bottomLeftCorner = (left, bottom)
        self.bottomRightCorner = (right, bottom)
        self.topLeftCorner = (left, top)
        self.topRightCorner = (right, top)

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1 = Rectangle(ax1, ax2, ay1, ay2)
        rect2 = Rectangle(bx1, bx2, by1, by2)
       
        print(rect1.topLeftCorner)
        print(rect1.bottomRightCorner)
        print(rect2.topLeftCorner)
        print(rect2.bottomRightCorner)

        intersectionArea = self.calcIntersection(rect1, rect2)
        
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        
    def calcIntersection(self, rect1, rect2):
        topLeftX, topLeftY, bottomRightX, bottomRightY, leftMost, topMost, rightMost, bottomMost = 0, 0, 0, 0, None, None, None, None
        if rect1.topLeftCorner[0] <= rect2.topLeftCorner[0]: # find leftMost triangle...
            leftMost, rightMost = rect1, rect2
        else:
            leftMost, rightMost = rect2, rect1
        if rect1.topLeftCorner[1] >= rect2.topRightCorner[1]: # find rightMost triangle...
            topMost, bottomMost = rect1, rect2
        else:
            topMost, bottomMost = rect2, rect1
            
        if leftMost == topMost: # these are the two positions you can have...
            print('here')
            if rightMost.topLeftCorner[0] >= leftMost.topLeftCorner[0] and rightMost.topLeftCorner[0] <= leftMost.topRightCorner[0]:
                topLeftX, topLeftY = rightMost.topLeftCorner[0], rightMost.topLeftCorner[1]
                bottomRightX, bottomRightY = min(rightMost.topRightCorner[0], leftMost.topRightCorner[0]), max(rightMost.topRightCorner[1], leftMost.topRightCorner[1])
        else:
            if rightMost.bottomLeftCorner[0] >= leftMost.bottomLeftCorner[0] and rightMost.bottomLeftCorner[0] <= leftMost.bottomRightCorner[0]:
                topLeftX, topLeftY = rightMost.bottomLeftCorner[0], min(leftMost.topRightCorner[1],
                rightMost.topRightCorner[1])
                print('hello')
                bottomRightX, bottomRightY = min(rightMost.bottomRightCorner[0], leftMost.bottomRightCorner[0]), rightMost.bottomRightCorner[1]
                print('hello')
        print("topLeftX {} topLeftY {} bottomRightX {} bottomRightY {}".format(topLeftX, topLeftY, bottomRightX, bottomRightY))

def main():
    sol = Solution()
    sol.computeArea(1, 5, 5, 1, 3, 8, 9, 3)

if __name__ == "__main__":
    main()
