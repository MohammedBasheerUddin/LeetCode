class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # idea is to use x and y axis to keep track of robot position, initially both x and y axis = 0 
        # if robot has moved Up or Right increment y and x axis respectively
        # if robot has moved Down or Left decrement y and x axixs respectively
        # if robot goes to same position as from origin return true
        # so if x and y again == 0 after moving in given direction return true else false
        x = 0                
        y = 0
        for i in moves:
            if i == 'U':
                y += 1
            elif i == 'R':
                x += 1
            elif i == 'D':
                y-= 1
            elif i == 'L':
                x -= 1
                
        return x == 0 and y == 0