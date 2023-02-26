import random

app.background = gradient('mediumSlateBlue', 'darkBlue', start='bottom')
app.stepsPerSecond = 30

Label('Barriers!', 330, 20, fill='white', size=30, bold=True)
Label('Score: ', 340, 45, fill='white', size=18, bold=True)
scoreLabel = Label(0, 380, 45, fill='white', size=18, bold=True)
Label('Move the mouse to avoid barriers', 20, 20, fill='white', align='left')

gameOverText = Group(
    Rect(200, 200, 300, 125, fill='aliceBlue', opacity=75, align='center'),
    Label('Game Over', 200, 175, fill='orangeRed', size=48, bold=True),
    Label('Press any key to restart', 200, 225, fill='orangeRed', size=20)
    )
gameOverText.visible = False

barrier = Group( 
    Rect(-400, 0, 425, 25, fill=gradient('orange', 'red', start='top')),
    Rect(100, 0, 400, 25, fill=gradient('orange', 'red', start='top'))
    )
barrier.dy = 6
barrier.maxDy = 12

player = RegularPolygon(200, 300, 25, 3, fill='white', border='mediumSlateBlue')

def nextBarrier():
    # Move the barrier to the top and position the gap randomly with an x
    # coordinate somewhere between 50 and 350 (inclusive).
    ### Place Your Code Here ###
    barrier.top = -25
    barrier.centerX = random.randint(50,350)
    player.points += 1
    # Then increase the number of points of the player.
    ### Place Your Code Here ###
    pass

def newGame():
    gameOverText.visible = False
    scoreLabel.value = 0
    nextBarrier()
    barrier.dy = 6
    player.points = 3

    app.paused = False

def moveBarrier():
    # Moves the barrier down with wraparound.
    barrier.top += barrier.dy
    if (barrier.top >= 400):
        scoreLabel.value += 1

        # If we wraparound, increases speed until we reach max speed.
        if (barrier.dy < barrier.maxDy):
            barrier.dy += 1
        nextBarrier()

def onMouseMove(mouseX, mouseY):
    # When the game is not over, set the player's center to the current mouse
    # position.
    ### Place Your Code Here ###
    if (gameOverText.visible == False):
        player.centerX = mouseX
        player.centerY = mouseY
    pass

def onKeyPress(key):
    if (gameOverText.visible == True):
        newGame()

def onStep():
    # If the game is not over, move the barrier.
    ### (HINT: The gameOverText is only visible when the game is over.)
    ### Place Your Code Here ###
    if (gameOverText.visible == False):
        moveBarrier()
        if (player.hitsShape (barrier)):
            gameOverText.visible = True
            app.paused = True
    # End the game if the player hits the barrier.
    ### (HINT: We can make the game pause by setting app.paused to True.)
    ### Place Your Code Here ###
    
    pass
