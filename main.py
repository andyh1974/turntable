import utime
import machine
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses
import music
from music import playtone, play_thomas_theme_buzzer, play_ymca_chorus_buzzer,play_eye_of_the_tiger,play_a_team_theme, play_rocky_theme,playJingleBells,beep,failTone

print("Loading train turntable 1.0")

step_pin = machine.Pin(15, machine.Pin.OUT)
dir_pin = machine.Pin(14, machine.Pin.OUT)

#ir= machine.Pin(13,machine.Pin.IN)


Signal_Pin = 13
ir_pin = machine.Pin(Signal_Pin,machine.Pin.IN)

hallEffect = machine.Pin(27, machine.Pin.IN)
sleepPin = machine.Pin(26, machine.Pin.OUT, machine.Pin.PULL_UP)

#represents the number of steps to do a full rotation
#is saved to steps.txt file and can be calculated by command #02
maxSteps = 200

lastAction = 0;
sleepAfter = 20000;
elapsedMills = 0;

##
currentCommand = ""

## 
positionMap = {}

currentPosition= 0
lastMoveCommand = ''
isZeroed = False

isMoving = False;

def loadData():
    stepsFile = open("steps.txt", "r")
    stepsData = stepsFile.read()
    stepsFile.close()
    
    if stepsData != "":
        maxSteps = int(stepsData)
    
    positionfile = open("positions.txt", "r")
    positionData = positionfile.read()
    positionfile.close()

    if positionData != "":
        print('loading positions:' + positionData)
        positionList = positionData.split("~")

        for p in positionList:
            print('parsing:'+p)
            if p != '':
                pData = p.split(",")
                positionMap[pData[0]] = pData[1]
                print('position:' + str(pData[0]) + ":"+ str(pData[1]))
    else:
        print('no position data')
    

def getCharacter(data):
    if data == '45':
        return '1'
    elif data == '46':
        return '2'
    elif data == '47':
        return '3'
    elif data == '44':
        return '4'
    elif data == '40':
        return '5'
    elif data == '43':
        return '6'
    elif data == '07':
        return '7'
    elif data == '15':
        return '8'
    elif data == '09':
        return '9'
    elif data == '19':
        return '0'
    elif data == '18':
        return 'up'
    elif data == '52':
        return 'down'
    elif data == '08':
        return 'left'
    elif data == '5a':
        return 'right'
    elif data == '1c':
        return 'ok'
    elif data == '16':
        return 'star'
    elif data == '0d':
        return 'hash'
    else:
        return data
        
            
def moveStepper(direction, steps):
    #take out of sleep
    #sleepPin.value(1)
    
    dir_pin.value(direction)

    for i in range(steps):
         #print("loop:",i)
         step_pin.value(1)
         utime.sleep_us(950)
         step_pin.value(0)
         utime.sleep_us(950)
   
   #we sleep to give the stepper time to move before we set it to sleep
    #utime.sleep_ms(1500)
    #back to sleep 
   # sleepPin.value(0)
   
def moveStepperUntillStopFlag(direction):
    isMoving = true
    
    dir_pin.value(direction)

    while isMoving:
         #print("loop:",i)
         step_pin.value(1)
         utime.sleep_us(950)
         step_pin.value(0)
         utime.sleep_us(950)
         
         if direction == 1:
             currentPosition = currentPosition + 1
         elif direction == 0:
             currentPosition = currentPosition - 1
             
         if currentPosition > maxSteps:
            currentPosition = 0
         elif currentPosition < 0:
            currentPosition = maxSteps
        
            


def runCommand(command):
    if str(command).isdigit():
        print('position command')
        moveToPosition(command)
    elif str(command).startswith('star'):
        command = str(command).replace('star','')
        print('program command')
        runProgramCommand(command)
    elif str(command).startswith('hash'):
        command = str(command).replace('hash','')
        print('easter egg command: ' + command)
        runEasterEgg(command)


def runProgramCommand(command):
    global currentPosition
    global positionMap
    
    positionMap[command] = currentPosition
    
    positionfile = open("positions.txt", "w")
    
    for c in positionMap:
        print(str(c)+":"+str(positionMap[c]))
        positionfile.write(str(c) + "," + str(positionMap[c]) + "~")    
        
    positionfile.close()
    print('data saved')


def runEasterEgg(command):
    if command == '1':
        print('playing thomas')
        play_thomas_theme_buzzer()
    if command == '2':
        print('playing jingle')
        playJingleBells()
    if command == '3':
        print('playing ymca')
        play_ymca_chorus_buzzer()
    if command == '4':
        print('playing eye of the tiger')
        play_eye_of_the_tiger()
    if command == '5':
        print('playing a team')
        play_a_team_theme()
    if command == '6':
        print('playing rocky')
        play_rocky_theme()
    if command == '0':
        zeroMotor()
    if command == '01':
        setZeroPosition()
    if command == '02':
        countTurnTableSteps()
        
def setZeroPosition():
    currentPosition = 0

def countTurnTableSteps():
    zeroMotor()
    numberOfSteps =  zeroMotor()
    stepsFile = open("steps.txt", "w")
    stepsfile.write(str(numberOfSteps))

def zeroMotor():
    
    global isZeroed
    global currentPosition
    currentPosition = 0
    isMoving = True
    
    count = 0
    isZeroed = False
    numStepsToMove = 1
    hallEffectVal = 0
    
    while isZeroed == False and isMoving == True:
        moveStepper(0,numStepsToMove)
        
        hallEffectVal = hallEffect.value()
        #print('hall value:' + str(hallEffectVal))
        
        if hallEffectVal == 0:
            #print('found zero')
            isZeroed = True
            beep(False)
        
        count = count + 1
    
    return count
        
       # if count > 20000:
          #  isZeroed = True
          #  print('could not find zero spot')
          #  failTone()
           
def moveToPosition(code):
    print('moving to position:' + code)
    global currentPosition
    global positionMap

    if str(code) not in positionMap:
        print('position not in map stopping')
        return
    
    newPosition = int(positionMap[code])
    
    print('current position:' + str(currentPosition) + ' new position'+ str(newPosition))
    
    if int(currentPosition) > newPosition:
        antiClockwise = currentPosition - newPosition
        clockWise = newPosition + (maxSteps - currentPosition)
        
        if antiClockwise < clockWise:
            print('moving anti clockwise ' + str(antiClockwise))
            moveStepper(0,antiClockwise)
        else:
            print('moving clockwise ' + str(clockWise))
            moveStepper(0,clockWise)

    else: #np > cp
        clockWise = newPosition -currentPosition
        antiClockwise = currentPosition + (maxSteps - newPosition)
        
        if antiClockwise < clockWise:
            print('moving anti clockwise ' + str(antiClockwise))
            moveStepper(0,antiClockwise)
        else:
            print('moving clockwise ' + str(clockWise))
            moveStepper(0,clockWise)

    currentPosition = newPosition
    print('current postion:'+str(currentPosition))
    
        
def moveRight(steps):
    global lastMoveCommand
    global currentPosition
    global maxSteps
    lastMoveCommand = 'right'
    moveStepper(1,steps)
    currentPosition = currentPosition+steps
    
    if currentPosition > maxSteps:
       currentPosition = 0
    
    print('postion:'+str(currentPosition))
    
    
def moveLeft(steps):
    global lastMoveCommand
    global currentPosition
    global maxSteps
    lastMoveCommand = 'left'
    moveStepper(0,steps)
    currentPosition = currentPosition-steps
    
    if currentPosition < 0:
       currentPosition = maxSteps
    
    print('postion:'+str(currentPosition))

#call back executed when an infa red character is received
#if there is no data we assume its a repeat, if the last command was move left or right we then go left or right in big steps
#if the current command is left or right we move that direction in 1 small increment
#if the command is the 'ok' button we execute the current command string
#otherwise we add the char onto the current command string. So if you are trying to move to position 10, first char '1' is added to command string, second char '0'
#is added to command string, then you press ok, and we call runCommand passing it the command string '10', this will check the first character
#as its a digit it will try to move you to position '10' 
def callback(data, addr, ctrl):
    elapsedMills = 0
    #take out of sleep
    sleepPin.value(1)
    
    global currentCommand
    global lastMoveCommand
    
    
    
    if data < 0:  # NEC protocol sends repeat codes.
        print('Repeat code.')
        print('last move:'+lastMoveCommand)
        if lastMoveCommand == 'right':
            #moveRight(30)
            moveStepperUntillStopFlag(1)
        elif lastMoveCommand == 'left':
            #moveLeft(30)
            moveStepperUntillStopFlag(0)
        else:
            beep(False)
    else:
        lastMoveCommand = ''
        beep(True)
        code = '{:02x}'.format(data)
        
        print('code' + code)
        
        translatedCode = getCharacter(code)
        print('translated code:',translatedCode)
        
        if translatedCode == 'ok':
            isMoving = False
            print('the command is:', currentCommand)
            runCommand(currentCommand)
            currentCommand = ''
        elif translatedCode == 'left':
            print('moving left- zero')
            lastMoveCommand = 'left'
            moveLeft(1)
        elif translatedCode == 'right':
            print('moving right - one')
            moveRight(1)
        else:
            currentCommand = currentCommand + translatedCode

    
loadData()
print("data read")

sleepPin.value(1)
print("driver awake")

#play tune to say we loaded
beep(True)
beep(False)
beep(True)

ir = NEC_8(ir_pin, callback)

while True:
    utime.sleep_ms(500)
    elapsedMills += 500
    
    if elapsedMills >  sleepAfter:
        sleepPin.value(0)
        elapsedMills = 0
        print("sleeping driver")



print("Turntable finished")











    



