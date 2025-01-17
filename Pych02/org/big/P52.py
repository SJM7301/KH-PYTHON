'''
Created on 2024. 12. 2.

@author: user
'''
import turtle;
'''
turtle.shape('turtle');

turtle.forward(200);
turtle.right(90);
turtle.forward(200);
turtle.right(90);
turtle.forward(200);
turtle.right(90);
turtle.forward(200);
'''

myT = None;

myT = turtle.Turtle();
myT.shape("turtle");

for i in range(0, 4):
    myT.forward(200);
    myT.right(90);
print(i);

turtle.done();
