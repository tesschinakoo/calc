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


#ADDITIONBUTTON
x1addition = 85
x2addition = 115
y1addition = 95
ButtonRectangle = Rectangle((85,95), (115,125))
ButtonRectangle.fill = Color("lightGray")
ButtonRectangle.outline = Color("Black")
ButtonRectangle.draw(win)
VerticalPlus = Line((100,100), (100,120))
VerticalPlus.fill = Color("Black")
VerticalPlus.draw(win)
HorizontalPlus = Line((90, 110), (110, 110))
HorizontalPlus.fill = Color("Black")
HorizontalPlus.draw(win)

#SUBTRACTIONBUTTON
AdditionRectangle = Rectangle((180,95), (210,125))
x1subtraction = 180
x2subtraction = 210
y1subtraction = 95
y2subtraction = 125
ButtonRectangle = Rectangle((180,95), (210,125))
ButtonRectangle.fill = Color("lightGray")
ButtonRectangle.outline = Color("Black")
ButtonRectangle.draw(win)
VerticalHorizontal = Line((185, 110), (205, 110))
VerticalHorizontal.fill = Color("Black")
VerticalHorizontal.draw(win)
