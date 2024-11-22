import utime
import machine
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses

print("Loading train turntable 1.0")

step_pin = machine.Pin(15, machine.Pin.OUT)
dir_pin = machine.Pin(14, machine.Pin.OUT)

#ir= machine.Pin(13,machine.Pin.IN)
Buzzer_Pin = 21

# Set up the Buzzer pin as PWM
buzzer = machine.PWM(machine.Pin(Buzzer_Pin)) # Set the buzzer to PWM mode

Signal_Pin = 13
ir_pin = machine.Pin(Signal_Pin,machine.Pin.IN)

hallEffect = machine.Pin(27, machine.Pin.IN)
sleepPin = machine.Pin(26, machine.Pin.OUT, machine.Pin.PULL_UP)

maxSteps = 200

### guitar notes for the music player....
A = 440
As = 466
Bf = 466
B = 494  #frequency (493.88 Hz)
Bs = 510
C = 523
Cs = 554
D = 587
Ds = 622
E = 659
F = 698
Fs = 740
Gf = 784
G = 830
Gs = 880

E4 = 329  # E4 note frequency (329.63 Hz)
G4 = 392  # G4 note frequency (392 Hz)
A4 = 440  # A4 note frequency (440 Hz)
B4 = 493  # B4 note frequency (493.88 Hz)
F4 = 349  # F4 note frequency (349.23 Hz)
D4 = 293  # D4 note frequency (293.66 Hz)
C4 = 261  # C4 note frequency (261.63 Hz)
B3 = 246  # B3 note frequency (246.94 Hz)
A3 = 220  # A3 note frequency (220 Hz)


G4 = 392  # G4 note frequency (392 Hz)
C5 = 523  # C5 note frequency (523.25 Hz)
G3 = 196  # G3 note frequency (196 Hz)
A3 = 220  # A3 note frequency (220 Hz)
F3 = 174  # F3 note frequency (174.61 Hz)
E4 = 329  # E4 note frequency (329.63 Hz)



# Create volume variable (Duty cycle)
volume = 32768

##
currentCommand = ""

## 
positionMap = {}

currentPosition= 0
lastMoveCommand = ''
isZeroed = False



# Create our function with arguments
def playtone(note,vol,noteLength,delayAfterNote):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    utime.sleep(noteLength)
    buzzer.duty_u16(0)
    utime.sleep(delayAfterNote)
    
def play_thomas_theme_buzzer():
    notes = [
        (Gf, 300,0.1), (G, 200,0.1),
        (Bf, 200,0.1), (B, 300,0.4),
        (Bs, 200,0.1), (E, 200,0.1),
        (G, 1000,0.4),(Gs,200,0.2),
        (D,200,0.4),(Gf,200,0.1),(G,600,0.3),
        (Gf,200,0.1),(G,200,0.1),(Gs,300,0.1),
        (G,200,0.1),(G,200,0.1),(Gs,200,0.1),(G,200,0.1),
        
        (Gf,200,0.1),(G,200,0.1),(Gf,200,0.1),(G,200,0.1),(Gf,200,0.1),(G,200,0.1),(G,200,0.4),   (Gf,200,0.1),(G,200,0.1),(Gf,200,0.1),(G,200,0.1),(Gs,200,0.1),(Gs,200,0.1),
        
        (D,200,0.1),(D,200,0.1),(Gf,200,0.1),(G,200,0.3),(Gs,200,0.3),    (G,200,0.1),(Gs,200,0.5),         (Gs,200,0.1),(G,200,0.1),(Gf,200,0.1),  (Ds,200,0.1),(Ds,200,0.1), (G,200,0.1),(Gs,200,0.1), (B,200,0.1),(B,200,0.5), (E,200,0.1),
        
        (D,200,0.1),(D,200,0.1),(G,200,0.1),(G,200,0.1),(B,200,0.1),(B,200,0.1),(Bs,200,0.4),       (As,200,0.1),(As,200,0.1),(D,200,0.1),(D,200,0.1),(G,200,0.1),(G,200,0.1),(B,200,0.1),
        
        (Bs,200,0.1),(Bs,200,0.3),   (Bf,200,0.1),(B,200,0.1),(Bs,200,0.2),(G,200,0.1)

    ]

    for note, duration, gap, in notes:
        playtone(note,volume, duration / 1000,gap)
    
def play_ymca_chorus_buzzer():
    notes = [
        (G, 400,200),(G, 400,800),
        (E, 1000,200),(E, 1000,800),
        (C, 1000,200),(C, 1000,800),
        (D, 400,500),(C, 400,500),(D, 400,500),(C, 400,500),(G, 400,500),(D, 400,500)
    ]

    for note, duration,delay in notes:
        playtone(note,volume, duration / 1000,0.1)
    

    


def play_eye_of_the_tiger():
    notes = [
        (E4, 400), (E4, 400), (F4, 200), (G4, 200),
        (E4, 400), (E4, 400), (F4, 200), (G4, 200),
        (E4, 400), (E4, 400), (F4, 200), (G4, 200),
        (C5, 800), (G4, 400), (F4, 200), (E4, 200),
        (C5, 800), (G4, 400), (F4, 200), (E4, 200),
        (D4, 800), (D4, 400), (E4, 200), (F4, 200),
        (G4, 800), (F4, 400), (E4, 200), (F4, 200),
        (D4, 800), (D4, 400), (E4, 200), (F4, 200),
        (G4, 800), (F4, 400), (E4, 200), (F4, 200),
        (C5, 1600), (G4, 400), (F4, 200), (E4, 200),
        (C5, 1600), (G4, 400), (F4, 200), (E4, 200),
        (D4, 800), (D4, 400), (E4, 200), (F4, 200),
        (G4, 800), (F4, 400), (E4, 200), (F4, 200),
    ]

    for note, duration in notes:
        playtone(note, volume, duration / 1000, 0.1)
        utime.sleep(0.05)

def play_a_team_theme():
    notes = [
        (A3, 2000), (A3, 200), (D4, 400),
        (C4, 200), (A3, 200), (E4, 400),
        (D4, 200), (A3, 200), (G3, 400),
        (F3, 200), (A3, 200), (E4, 400),
        (D4, 200), (A3, 200), (A4, 800),
        (A3, 200), (A4, 400), (A3, 200), (G3, 200),
        (A3, 400), (F3, 200), (A3, 200), (A3, 800),
        (A3, 200), (A4, 400), (A3, 200), (G3, 200),
        (A3, 400), (F3, 200), (A3, 200), (A3, 800),
    ]

    for note, duration in notes:
        playtone(note, volume, duration / 1000, 0.1)
        utime.sleep(0.05)

def play_rocky_theme():
    notes = [
        (E4, 400), (G4, 400), (A4, 400), (B4, 400), (A4, 200), (G4, 200), (E4, 400),
        (G4, 400), (A4, 400), (B4, 400), (A4, 200), (G4, 200), (E4, 400),
        (E4, 400), (E4, 200), (G4, 200), (A4, 400), (G4, 200), (F4, 200), (E4, 400),
        (E4, 400), (E4, 200), (G4, 200), (A4, 400), (G4, 200), (F4, 200), (E4, 400),
        (D4, 400), (F4, 400), (G4, 400), (A4, 400), (G4, 200), (F4, 200), (D4, 400),
        (F4, 400), (G4, 400), (A4, 400), (G4, 200), (F4, 200), (D4, 400),
        (C4, 400), (E4, 400), (F4, 400), (G4, 400), (F4, 200), (E4, 200), (C4, 400),
        (E4, 400), (F4, 400), (G4, 400), (F4, 200), (E4, 200), (C4, 400),
        (B3, 400), (D4, 400), (E4, 400), (F4, 400), (E4, 200), (D4, 200), (B3, 400),
        (D4, 400), (E4, 400), (F4, 400), (E4, 200), (D4, 200), (B3, 400),
        (A3, 400), (C4, 400), (D4, 400), (E4, 400), (D4, 200), (C4, 200), (A3, 400),
        (C4, 400), (D4, 400), (E4, 400), (D4, 200), (C4, 200), (A3, 400),
    ]

    for note, duration in notes:
        playtone(note, volume, duration / 1000, 0.1)
        utime.sleep(0.05)

def playJingleBells():
    # Play the tune
    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.5) #Longer second delay

    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.5) #Longer second delay

    playtone(E,volume,0.1,0.2)
    playtone(G,volume,0.1,0.2)
    playtone(C,volume,0.1,0.2)
    playtone(D,volume,0.1,0.2)
    playtone(E,volume,0.1,0.6)

    playtone(F,volume,0.1,0.2) #oh
    playtone(F,volume,0.1,0.2) #what
    playtone(F,volume,0.1,0.2) #fun
    playtone(F,volume,0.1,0.2) #it
    playtone(F,volume,0.1,0.2) #is
    playtone(E,volume,0.1,0.2) #to
    playtone(E,volume,0.1,0.2) #ride
    playtone(E,volume,0.0,0.0) #in
    playtone(E,volume,0.0,0.2) # a

    playtone(E,volume,0.1,0.2) #one
    playtone(D,volume,0.1,0.2) #horse
    playtone(D,volume,0.1,0.3) #op
    playtone(E,volume,0.1,0.2) #en
    playtone(D,volume,0.1,0.2) #sleug
    playtone(G,volume,0.1,0.6) #sleug

    #second verse

    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.5) #Longer second delay

    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.2)
    playtone(E,volume,0.1,0.5) #Longer second delay

    playtone(E,volume,0.1,0.2)
    playtone(G,volume,0.1,0.2)
    playtone(C,volume,0.1,0.2)
    playtone(D,volume,0.1,0.2)
    playtone(E,volume,0.1,0.6)

    playtone(F,volume,0.1,0.2) #oh
    playtone(F,volume,0.1,0.2) #what
    playtone(F,volume,0.1,0.2) #fun
    playtone(F,volume,0.1,0.2) #it
    playtone(F,volume,0.1,0.2) #is
    playtone(E,volume,0.1,0.2) #to
    playtone(E,volume,0.1,0.2) #ride
    playtone(E,volume,0.0,0.0) #in
    playtone(E,volume,0.0,0.2) # a

    playtone(G,volume,0.1,0.2) #one
    playtone(G,volume,0.1,0.2) #horse
    playtone(F,volume,0.2,0.3) #op
    playtone(D,volume,0.1,0.2) #en
    playtone(C,volume,0.1,0.2) #sleigh

def readPositionData():
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
    

def beep(high):
    f =1000
    duty = 10000
    t=0.1
    
    if high:
        f=5000
    
    # Set PWM frequency to 1000
    buzzer.freq(f)
    # Set PWM duty
    buzzer.duty_u16(duty)
    utime.sleep(t) # Wait 1 second
    # Duty to 0 to turn the buzzer off
    buzzer.duty_u16(0)
    
def failTone():
    notes = [
    (Gf, 300,0.1), (G, 300,0.1),
    (Bf, 600,0.1)
    ]

    for note, duration, gap, in notes:
        playtone(note,volume, duration / 1000,gap)
    



#for i in range(2):
#    print("loop:",i)
#    utime.sleep(1)
#    if led_state == True:
#        led_external.value(1)
#        led_state = False
#    else:
#        led_external.value(0)
#        led_state = True
        
#file = open("test.txt", "w")
#file.write("Hello, File!")
#file.close()

#file2 = open("test.txt", "w")
#data = file2.read()
#file2.close()

#print("data"+data)

#set direction
#dir_pin.value(0)

#for i in range(100):
#     print("loop:",i)
#     step_pin.value(1)
#     utime.sleep(0.01)
#     step_pin.value(0)
#     utime.sleep(0.01)
     
#dir_pin.value(1)
#i=0

#for i in range(100):
#     print("loop:",i)
#     step_pin.value(1)
#     utime.sleep(0.01)
#     step_pin.value(0)
#     utime.sleep(0.01)

#IR detection
#while True:
#    try:
#        if ir.value()==0:
#             print("Detected")
#             step_pin.value(1)
#             utime.sleep(0.01)
#             step_pin.value(0)

#        utime.sleep_ms(50)
#    except KeyboardInterrupt:
#        break

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
    sleepPin.value(1)
    
    dir_pin.value(direction)

    for i in range(steps):
         #print("loop:",i)
         step_pin.value(1)
         utime.sleep(0.01)
         step_pin.value(0)
         utime.sleep(0.01)
         
    #back to sleep
    sleepPin.value(0)

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
        
        
def zeroMotor():
    
    global isZeroed
    global currentPosition
    currentPosition = 0
    
    count = 0
    isZeroed = False
    numStepsToMove = 1
    hallEffectVal = 0
    
    while isZeroed == False:
        moveStepper(0,numStepsToMove)
        
        hallEffectVal = hallEffect.value()
        print('hall value:' + str(hallEffectVal))
        
        if hallEffectVal == 0:
            print('found zero')
            isZeroed = True
            beep(False)
        
        count = count + 1
        
        if count > 300:
            isZeroed = True
            print('could not find zero spot')
            failTone()
            #beep(False)
           # beep(False)
           
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
        diff = currentPosition - newPosition
        print('moving positive ' + str(diff))
        moveStepper(0,diff)
    else:
        diff = newPosition - currentPosition
        print('moving negative ' + str(diff))
        moveStepper(1,diff)

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

def callback(data, addr, ctrl):
    global currentCommand
    global lastMoveCommand
    
    if data < 0:  # NEC protocol sends repeat codes.
        print('Repeat code.')
        print('last move:'+lastMoveCommand)
        if lastMoveCommand == 'right':
            moveRight(5)
        elif lastMoveCommand == 'left':
            moveLeft(5)
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

    
readPositionData()

print("data read")

sleepPin.value(0)

print("driver in sleep mode")

beep(True)
beep(False)
beep(True)

ir = NEC_8(ir_pin, callback)

while True:
    utime.sleep_ms(500)

print("Turntable finished")











    


