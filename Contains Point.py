def cPoint(x, y, rect_x, rect_y, rectWidth, rectHeight):
    """ This function checks whether if a point is within a rectangle"""
    if x in range(rect_x, (rect_x + rectWidth + 1)) and y in range(rect_y, (rect_y + rectHeight + 1)):
        return True
    else:
        return False

print(cPoint(100, 100, 100, 100, 20, 20))
