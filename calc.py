from Myro import *
from Graphics import *
win = Window("Calc")

#TITLE
Title = Text((150,20), "Calculator")
Title.fontSize = 20
Title.fill = Color("Black")
Title.draw(win)

#SCREEN
Screen = Rectangle((10, 35), (290, 80))
Screen.fill = Color("lightGray")
Screen.outline = Color("Black")
Screen.draw(win)


#ADDITION BUTTON
SubtractionRectangle = Rectangle((85,95), (115,125))
SubtractionRectangle.fill = Color("lightGray")
SubtractionRectangle.outline = Color("Black")
SubtractionRectangle.draw(win)
VerticalPlus = Line((100,100), (100,120))
VerticalPlus.fill = Color("Black")
VerticalPlus.draw(win)
HorizontalPlus = Line((90, 110), (110, 110))
HorizontalPlus.fill = Color("Black")
HorizontalPlus.draw(win)

#SUBTRACTION BUTTON
AdditionRectangle = Rectangle((185,95), (215,125))
AdditionRectangle.fill = Color("lightGray")
AdditionRectangle.outline = Color("Black")
AdditionRectangle.draw(win)
VerticalHorizontal = Line((190, 110), (210, 110))
VerticalHorizontal.fill = Color("Black")
VerticalHorizontal.draw(win)

listcalc = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(listcalc)):
    for j in range(len(listcalc)):
        print(listcalc[i][j])

#FIRST ROW NUMBER BUTTONS
for x in range(0,3):
    NumberButton = Rectangle((55 + (x * 80),145), (85 + (x * 80),175))
    NumberButton.fill = Color("lightGray")
    NumberButton.outline = Color("Black")
    NumberButton.draw(win)
for x in range(0,3):
    Numbers = Text((70 + (x*80), 160), "1")
    Numbers.fill = Color("black")
    Numbers.draw(win)

#SECOND ROW NUMBER BUTTONS
for x in range(0,3):
    NumberButton = Rectangle((55 + (x*80),195), (85 + (x * 80),225))
    NumberButton.fill = Color("lightGray")
    NumberButton.outline = Color("Black")
    NumberButton.draw(win)
for x in range(0,3):
    Numbers = Text((70 + (x*80), 210), "1")
    Numbers.fill = Color("black")
    Numbers.draw(win)

#THIRD ROW NUMBER BUTTONS
for x in range(0,3):
    NumberButton = Rectangle((55 + (x * 80),245), (85 + (x * 80),275))
    NumberButton.fill = Color("lightGray")
    NumberButton.outline = Color("Black")
    NumberButton.draw(win)
for x in range(0,3):
    Numbers = Text((70 + (x*80), 260), "1")
    Numbers.fill = Color("black")
    Numbers.draw(win)
    
#EQUAL/ENTER BUTTON
EnterRectangle = Rectangle((230,40), (285,75))
EnterRectangle.fill = Color("lightGray")
EnterRectangle.outline = Color("red")
EnterRectangle.draw(win)
EnterText = Text((258, 55), "Enter")
EnterText.fill = Color("black")
EnterText.draw(win)
