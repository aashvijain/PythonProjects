# background
Rect (0,0,400,400,fill = 'paleGreen',opacity = 40)

# hang drawing
Line(80, 220, 160, 220)
Line(118, 220, 118, 40)
Line(118, 40, 260, 40)
Line(260, 40, 260, 60)

Label("Name of the hardware unit that carries out instructions for the computer?", 200, 20, visible=True)

# global variables
s = 'CPU'
word = ['c','p','u']
word2 = ['c','p','u']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
repeat = []
drawing = []
    
# label for repeated letter
l = Label("Pick a new letter!", 60, 100, visible= False)
    
#drawing keyboard
keys = []
cx = 35
cy = 290
for i in range(26):
    if (cx > 380):
        cx = 35
        cy += 25
            
    keys.append(Rect(cx-10,cy-10,30,20,fill='gainsboro'))
    Label(alphabet[i],cx,cy)
    cx += 45
    
# hangman list
drawing.append(Line(260, 104, 285, 120))
drawing.append(Line(260, 104, 232, 120))
drawing.append(Line(260, 160, 302, 200))
drawing.append(Line(260, 160, 214, 200))
drawing.append(Line(260, 104, 260, 160))
drawing.append(Circle(260, 82, 22, fill=None, border="black"))
    
for i in drawing:
    i.visible = False

# show blanks for word
for index in range(len(word)):
    Line(140+index*40, 260, 170+index*40, 260)

# show letters on word
def showLetter(letter):
    r = False
    for index, value in enumerate(word):
        if letter == value:
            r = True
            Label(letter, 155+index*40, 250)
            
            # remove letter once placed
            while value in word2:
                word2.remove(value)
        
    return r
    
# check if game is over
def checkhangman():
    if len(drawing) == 0:
        Label("GAME OVER", 50, 50)
        Label("Word is " + s, 50, 80)
        return False
    if len(word2) == 0:
        Label("YOU WON", 50, 50)
        return False
    return True
    
q = Label("Good Job!!", 60, 100, visible=False)

#guessing letters
def onMousePress (mouseX,mouseY):
    if checkhangman():
        for k, key in enumerate(keys):
            if key.hits(mouseX, mouseY):
                if alphabet[k] in repeat:
                    l.visible = True
                else:
                    if showLetter(alphabet[k]) == False:
                        q.visible = False
                        hangman_part = drawing.pop()
                        hangman_part.visible = True
                    if showLetter(alphabet[k]) == True:
                        q.visible = True
                    l.visible = False
                repeat.append(alphabet[k])
    checkhangman()
