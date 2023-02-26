import random
# Fill me in!
app.background = "papayaWhip"
app.steps = 30
shadow = Oval (140,280,200,50,fill = 'gainsboro')
ball1 = Group (
    Circle (200,170,120),
    Circle (215,155,75,fill = 'white'),
    Label ('8',235,145,font = 'monospace',size = 115,bold = True)
    )
ball1.rotateAngle = -10
ball2 = Group (
    Circle (200,200,120),
    Circle (200,200,85,fill = 'navy',opacity = 70))
ball2.visible = False
    
button1 = Group(
    Rect(85,320,240,40,fill = 'black'),
    Label ("Ask a Question",205,340,font = 'monospace',size = 20, bold = True,fill = 'white'))
reshake = Group(
    Rect(85,30,240,30,fill = 'indigo'),
    Label ("Reshake",205,45,font = 'monospace',size = 25, bold = True,fill = 'yellow'))
exit = Group(
    Rect(105,360,200,30, fill = 'indigo'),
    Label ("Exit",205,375,font = 'monospace',size = 25, bold = True,fill = 'yellow'))
reshake.visible = False
exit.visible = False
    
answers = ["Yes","No","Maybe","Definitely","Not Sure", "Probably"]

welcomeScreen = Group (
    Rect (0,0,400,400,fill = 'papayaWhip'),
    Label ("Welcome to Magic 8 Ball!",200,100,font = 'monospace',size = 18, bold = True),
    Label ("To ask a question,",200,150,font = 'monospace',size = 18, bold = True),
    Label ("Click the 'ask question button'",200,170,font = 'monospace',size = 18, bold = True),
    Label ("To ask another question,",200,220,font = 'monospace',size = 18, bold = True),
    Label ("click 'reshake'",200,250,font = 'monospace',size = 18, bold = True),
    Label ("To exit, press 'exit'",200,300,font = 'monospace',size = 18, bold = True),
    Label ("Press 'a' to begin",200,350,font = 'monospace',size = 18, bold = True))
def shakeBall (question):
    num = random.randint (0,len(answers)-1)
    for i in range (3):
        ball1.centerY -= 25
        sleep (0.1)
        ball1.centerY += 25
        sleep (0.1)
        ball2.centerY -= 10
        sleep (0.1)
        ball2.centerY += 10
        sleep (0.1)
    button1.visible = False
    reshake.visible = True
    exit.visible = True
    app.background = 'indigo'
    ball1.visible = False
    ball2.visible = True
    createStars()
    value = False
    for i in range(len(question)):
        if question[i] == '?':
            value = True
    if (value == True):
        word = Label (answers[num],200,205,size = 30,fill = 'royalBlue',bold = True)
        sleep (5)
        word.visible = False
    else:
        word = Label ("That is not",200,190,size = 27,fill = 'royalBlue',bold = True)
        word2 = Label ("a question",200,220,size = 27,fill = 'royalBlue',bold = True)
        sleep (5)
        word.visible = False
        word2.visible = False
    button1.toBack()
        
    
    
      
stars = Group()         
def createStars():
    stars.clear()
    shadow.visible = False
    x = 20
    y = 20
    app.background = 'indigo'
    number = random.randint (150,200)
    for i in range (number):
        size = random.randint (5,10)
        points = random.randint (5,10)
        createdStar = Star (x,y,size,points,fill = 'white',opacity = 70)
        for j in stars.children:
            if (j.hitsShape (createdStar)):
                createdStar.visible = False
        if (createdStar.hitsShape (ball2)==True) or (createdStar.hitsShape (reshake) == True) or (createdStar.hitsShape(exit)==True):
            createdStar.visible = False
            i = i - 1
        if (createdStar.visible == True):
            stars.add (createdStar)
        x += 40
        if (x >400):
            x = 20
            y += 30
            
def removeStars ():
    for i in stars.children:
        i.visible = False
        
def responses (value):
    if (value == 1):
        response = app.getTextInput ("Ask me a question")
        shakeBall(response)
    elif (value == 2):
        response2 = app.getTextInput ("Ask me a new question")
        shakeBall (response2)
    elif (value == 3):   
        ball2.visible = False
        app.background = 'papayaWhip'
        shadow.visible = True
        removeStars()
        ball1.visible = True
        exit.visible = False
        reshake.visible = False
        Label ("Thank you for playing!",205,340,font = 'monospace',size = 20, bold = True,fill = 'black')

def onMousePress (mouseX,mouseY):
    if (button1.hits(mouseX,mouseY)):
        responses(1)
    elif (reshake.hits(mouseX,mouseY)):
        responses (2)
    elif (exit.hits (mouseX,mouseY)):
        responses(3)
    
def onKeyPress (key):
    if (key == 'a'):
        welcomeScreen.visible = False
        
         
    
    
    

