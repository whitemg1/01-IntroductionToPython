"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Matthew White.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################


import rosegraphics as rg

window = rg.TurtleWindow()
matt = rg.SimpleTurtle()

matt.pen = rg.Pen('yellow', 100)
matt.speed = 10

matt.pen_up()
matt.right(90)
matt.forward(-80)
matt.left(90)
matt.pen_down()

matt.draw_circle(50)


grass = rg.SimpleTurtle()

grass.pen = rg.Pen('green',100)
grass.speed = 10


grass.forward(400)
grass.backward(800)



window.close_on_mouse_click()