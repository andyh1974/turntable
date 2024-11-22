import machine
import utime

Buzzer_Pin = 21

# Set up the Buzzer pin as PWM
buzzer = machine.PWM(machine.Pin(Buzzer_Pin)) # Set the buzzer to PWM mode

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
