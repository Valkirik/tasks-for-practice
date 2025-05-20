class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def point(self):
        return f"x = {self.x}, y = {self.y}"

    def move(self, string = ""):

        for i in string:
            if i.upper() == "U":
                self.y += 1
                if self.y < 0 or self.y > 20:
                    print("The robot can not move in this direction. Start from the beginning")
                    self.x = 0
                    self.y = 0
            elif i.upper() == "D":
                self.y -= 1
                if self.y < 0 or self.y > 20:
                    print("The robot can not move in this direction. Start from the beginning")
                    self.x = 0
                    self.y = 0
            elif i.upper() == "R":
                self.x += 1
                if self.x < 0 or self.x > 20:
                    print("The robot can not move in this direction. Start from the beginning")
                    self.x = 0
                    self.y = 0
            else:
                self.x -= 1
                if self.x < 0 or self.x > 20:
                    print("The robot can not move in this direction. Start from the beginning")
                    self.x = 0
                    self.y = 0

        return f"the robot's location: {Robot.point(self)}"




robot_1 = Robot()

print(robot_1.move("urll"))









