from tkinter import *

class Paddle:
    #Paddle init
    def __init__(self, canvas, color, height, player, w):
        self.canvas = canvas
        self.height = height
        self.w = w
        self.id = canvas.create_rectangle(0,0, 100, 15, fill=color)
        self.canvas.move(self.id, (self.w/2)-50, height)
        self.xspeed = 0
        self.player=player
        if player==1:
            self.canvas.bind_all('<KeyPress-Left>', self.move_left)
            self.canvas.bind_all('<KeyPress-Right>', self.move_right)
            self.canvas.bind_all('<KeyPress-Down>', self.stop)
           
        elif player==2:
            self.canvas.bind_all('<KeyPress-q>', self.move_left)
            self.canvas.bind_all('<KeyPress-d>', self.move_right)
            self.canvas.bind_all('<KeyPress-s>', self.stop)
            
    #Paddle movement
    def draw(self):
        self.canvas.move(self.id, self.xspeed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.xspeed = 0
        if pos[2] >= self.w:
            self.xspeed = 0

    def move_left(self, evt):
        self.xspeed = -5
    def move_right(self, evt):
        self.xspeed = 5
    def stop(self, evt):
        self.xspeed = 0