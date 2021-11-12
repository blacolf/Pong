import threading
from tkinter import *
import time
import socket
from Ball import Ball
from Paddle import Paddle

class Main:
    def __init__(self):
        #Init
        self.tk = Tk()
        self.tk.title("PONG_Server")
        self.w=480
        self.h=640
        self.time = time
        self.canvas = Canvas(self.tk, width=self.w, height=self.h, bd=0, bg='black')
        self.canvas.pack()
        self.tk.update()
        
        self.paddle = Paddle(self.canvas, 'red', self.h-15, 1, self.w)
        self.paddle2= Paddle(self.canvas, 'White', 0, 2, self.w)
        ball = Ball(self.canvas, 'white', 25, self.paddle, self.paddle2, self.h, self.w)
        self.canvas.create_line(0,self.h/2+2,self.w,self.h/2+2,fill="white",width=4, dash=(2, 4))

        #Socket init
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = '127.0.0.1'
        self.port = 59001
        self.client = None
        self.adresse = None
        self.server.bind((self.ip, self.port))
        self.server.listen(1)
        #self.position_y = self.paddle2
        #self.paddle2.rect.y= int(self.position_y)

        #Appel la fonction thread
        self.create_thread(self.wait_connexion)


        #Scores init
        score=0 
        score2=0
        self.label = self.canvas.create_text(5, self.h/2-105, anchor=NW, text=score,fill="white", font=("Ani",50))
        self.label = self.canvas.create_text(5, self.h/2, anchor=NW, text=score2,fill="red",font=("Ani",50))

        while True:
            #Scores add
            while ball.hit_topbottom == False:
                
                ball.draw()
                self.paddle.draw()
                self.paddle2.draw()
                self.tk.update_idletasks()
                self.tk.update()
                self.time.sleep(0.01)
                if ball.hit_top==True:
                    score2=score2+1
                    ball.hit_topbottom == False
                    ball.hit_top==False
                elif ball.hit_bottom==True:
                    score=score+1
                    ball.hit_topbottom == False
                    ball.hit_bottom==False


            # Game Over
            if score==3:
                self.go_label = self.canvas.create_text(self.w/2,self.h/2,text="P1 WON",font=("Cantarell Ultra-Bold",40), fill="White")
                ball.hit_topbottom == True
                self.tk.update()
                time.sleep(10)
                self.tk.destroy  
                print ('OK1') 
                break

            elif score2==3:
                self.go_label = self.canvas.create_text(self.w/2,self.h/2,text="P2 WON",font=("Cantarell Ultra-Bold",40), fill="White")
                self.tk.update()
                time.sleep(10)
                self.tk.destroy
                print ('OK2')
                break

            else:
                self.go_label = self.canvas.create_text(self.w/2,self.h/2,text="GAME OVER",font=("Cantarell Ultra-Bold",40), fill="White")
                self.tk.update()
                time.sleep(2)
                ball.hit_topbottom=False
                self.tk.destroy()




    #Connexion client
    def wait_connexion(self):
        self.client, self.adresse = self.server.accept()
        print ('connection OK for ', self.adresse)
        self.reception()

    def reception(self):
        while True:
            self.position_y = self.client.recv(500).decode('utf-8')

    def create_thread(self,cible):
        thread = threading.Thread(target=cible)
        thread.daemon = True
        thread.start()



if __name__ == "__main__":
    Main()