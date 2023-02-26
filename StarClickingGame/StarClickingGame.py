app.background = gradient('mediumOrchid', 'indigo', start='bottom')
app.stepsPerSecond = 20

star = Star(200, 220, 50, 5, fill='cornflowerBlue')
ring = Star(200, 220, 5, 5, fill=None, border=gradient('white', 'yellow'),
            borderWidth=8)

score = Label(0, 350, 40, fill=None, border='white', size=50, bold=True)

gameOverLabel = Label('Game over', 200, 200, fill='navy', size=30, bold=True)
gameOverGroup = Group(
    Rect(200, 210, 200, 60, fill='aliceBlue', align='center'),
    gameOverLabel,
    Label('Press any key to play again', 200, 225, fill='navy')
    )
gameOverGroup.visible = False

def gameOver(message):
    gameOverLabel.value = message
    gameOverGroup.visible = True
    ring.visible = False

def restartGame():
    ring.radius = 5
    star.radius = 50
    score.value = 0
    gameOverGroup.visible = False
    ring.visible = True

def onKeyPress(key):
    # When a key is pressed while the game is over, restart.
    if (gameOverGroup.visible == True):
        restartGame()
    else:
        # If the ring was not close enough to the star, end the game.
        if (star.fill != 'mediumSeaGreen'):
            star.fill = 'orangeRed'
            gameOver('Oh No!!!')

        # Otherwise move on to the next round.
        else:
            ring.radius = 5
            star.radius += 10
            score.value += 1
            if (score.value == 15):
                gameOver('You Win!!!')

def onStep():
    # When game is in-play, increase the radius of the ring by the score + 1.
    # Depending on the size of the ring, set the color of star and end the
    # game if needed.
    ### (HINT: The player loses if the ring becomes larger than
    #          star.radius + 25.)
    ### (HINT: Use test cases to determine when the colors change.)
    ### Place Your Code Here ###
    if gameOverGroup.visible == False:
        ring.radius += score.value + 1
        if ring.radius + 25 >= star.radius:
            star.fill = 'mediumSeaGreen'
        else:
            star.fill = 'cornflowerBlue'
        if star.radius + 25 < ring.radius:
            gameOver ("Oh No!!!")
            star.fill = 'orangeRed'
    pass
