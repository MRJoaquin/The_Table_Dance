import sys

class SimulationState:
    def __init__(self, state):
        self.state = state

class Table:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Point:
    def __init__(self, x_position, y_position, direction):
        self.x_position = int(x_position)
        self.y_position = int(y_position)
        self.direction = direction
        
    def movePoint(self, command):
        
        for x in command:
        
            if (unvalidPosition(self.x_position, self.y_position, table.width, table.height)):
                return "failed"
                
            if (x == '0'):
                return "succeeded"
                break

            elif (x == '1'):

                if(self.direction == 'N'):
                    self.y_position -= 1
                elif (self.direction == 'S'):
                    self.y_position += 1
                elif (self.direction == 'E'):
                    self.x_position += 1
                elif (self.direction == 'W'):
                    self.x_position -= 1

            elif (x == '2'):

                if(self.direction == 'N'):
                    self.y_position += 1
                elif (self.direction == 'S'):
                    self.y_position -= 1
                elif (self.direction == 'E'):
                    self.x_position -= 1
                elif (self.direction == 'W'):
                    self.x_position += 1

            elif (x == '3'):

                if(self.direction == 'N'):
                    self.direction = 'E'
                elif (self.direction == 'E'):
                    self.direction = 'S'
                elif (self.direction == 'S'):
                    self.direction = 'W'
                elif (self.direction == 'W'):
                    self.direction = 'N'

            elif (x == '4'):

                if(self.direction == 'N'):
                    self.direction = 'W'
                elif (self.direction == 'W'):
                    self.direction = 'S'
                elif (self.direction == 'S'):
                    self.direction = 'E'
                elif (self.direction == 'E'):
                    self.direction = 'N'  

def unvalidPosition(x_pos, y_pos, width, height):
    if ((int(x_pos) > int(width)) or (int(y_pos) > int(height)) or (int(x_pos) < 0) or (int(y_pos) < 0)):
        simulationState.state = "failed"
        return True
    return False

def checkInput(input):
    # Simple input check
    # If the input value is not an int, it will return as a 0
    try:
        # Try to convert input into an integer
        val = int(input)
        # if it's an int, we return the value but first we check so it's not a negative value
        if (val < 0):
            return 0
        return input
    except ValueError:
        # else we check if its a float 
        try:
            # Try to convert input into a floating point number
            val = float(input)
            return 0
        except ValueError:
            # else it's a char or string
            return 0

def getHeader():
    
    # Here I'm assuming that the values of the header is separated by commas and ends with a newline character
    
    headerList = []
    
    #prompt the user and store input
    table_width, table_height, x_pos, y_pos = input("Enter comma separated header [width, height, x, y] ").split(",")
    table_width = checkInput(table_width)
    table_height = checkInput(table_height)
    x_pos = checkInput(x_pos)
    y_pos = checkInput(y_pos)
    
    headerList = [table_width, table_height, x_pos, y_pos]
    
    return headerList

def getIntStream():
    
    # Here I'm assuming that the values of the stream is separated by commas and ends with a newline character 
    
    command = input("Enter comma separated commands: ").split(",")
    
    return command

print("****Welcome to The Table Dance!****\n")

header = getHeader()

table = Table(header[0], header[1])
point = Point(header[2], header[3], 'N')
simulationState = SimulationState("initial state")

command = getIntStream()

simulationState.state = point.movePoint(command)

if (simulationState.state == "failed"):
    print("[-1,-1]")
elif (simulationState.state == "succeeded"):
    print('[' + str(point.x_position) + ", " + str(point.y_position) + ']')
else:
    print("something is wrong... really wrong...")
