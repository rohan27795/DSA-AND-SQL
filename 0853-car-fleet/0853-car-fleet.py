class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        times = [float(target - position) / speed for position, speed in cars]
        stack = []
        for time in times:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)




        


        

        

        
    


        