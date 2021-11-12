from tkinter import *

class Ball:
    #Ball init 
    def __init__(self, canvas, color, size, paddle, paddle2, h, w):
        self.canvas = canvas
        self.h = h
        self.w = w
        self.id = canvas.create_rectangle(10, 10, size, size, fill=color)
        self.canvas.move(self.id, 360, self.w/2)
        self.xspeed = 0
        self.yspeed = 0
        self.paddle = paddle
        self.paddle2 = paddle2
        self.hit_topbottom = False
        self.hit_bottom = False
        self.hit_top = False
        
        #game start
        if self.yspeed == 0:
            self.canvas.bind_all('<KeyPress-space>', self.gamestart)

    def gamestart(self, evt):
        self.yspeed = 3
        self.xspeed = 3

    #Ball movement
    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.hit_topbottom = True
            self.hit_top=True
        if pos[3] >= self.h:
            self.hit_topbottom = True
            self.hit_bottom = True
        if pos[0] <= 0:
            self.xspeed = 3
        if pos[2] >= self.w:
            self.xspeed = -3
        if pos[1]>self.h/2-250 and self.hit_paddle(pos,self.paddle) == True:
            self.yspeed = -3
        if pos[1]<self.h/2+250 and self.hit_paddle2(pos,self.paddle2) == True:
                self.yspeed = 3

    #Touche paddles
    def hit_paddle(self, pos, paddle):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def hit_paddle2(self, pos, paddle2):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[1] >= paddle2_pos[1] and pos[1] <= paddle2_pos[3]:
                return True
        return False