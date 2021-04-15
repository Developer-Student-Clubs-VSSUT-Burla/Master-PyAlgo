''' Find the largesr rectangular area possible in agiven histogram where thr largest rectangle 
    can be made of a number of contiguos bar. Assume that all bar have the same
    width i.e. 1 unit.

   There are various ways in which the question can be solved and we will be using
   STACK, in order to solve the problem.

   Sample Input
   Enter heights of the bar 6,2,5,4,5,1,6 '''

class Area (object):
    def largestRectangleArea(self,heights):

        #First we create an empty stack that will hold the value of the height in an increasing order
        s =[]
        i = 0       #initialisng index
        area = 0    # Area is being initialised by minimum

        while i < len(heights):  
            # If the height of present bar is more than the height of the last bar in the stack, then
            # push the bar in the stack
            if len(s)==0 or heights[s[-1]] <= heights [i]:
                s.append(i)
                i+=1
            
            # If this bar is lower than top of stack, then calculate area of rectangle with 
            # stack top as the smallest (or minimum height) bar.
            else:
                x = s[-1]
                s.pop()
                height = heights[x]
                # calculating area of histogram with the top of the stack as the smallest bar
                temp = height * (i - s[-1] -1) if len(s)!=0 else height * i
                area= max(area,temp)   # updating max area
                
        while len(s)>0:
            # Now pop the remaining bars from stack and calculate area with 
            # every popped bar as the smallest bar
            x = s[-1]
            height = heights[x]
            s.pop()
            temp = height * (len(heights) - s[-1] -1) if len(s)!=0 else height* len(heights)
            area = max(area,temp)
        
        return area  # returning maximum area

# Driver code of the given function : 

if __name__ == '__main__' :

    numbers = list(map(int,input("Enter heights of the bar: ").split(",")))

    solution= Area()
    print("Maximum Rectangle Area: ", solution.largestRectangleArea(numbers))

''' Sample Output
    Maximum Rectangle Area: 12 '''