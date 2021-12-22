from turtle import *
from random import *
from tkinter import *
from PIL import Image
import turtle
import time
import random
import array as arr 



def Racing(set, bg, dt):
	WIDTH, HEIGHT = dt, 600

	def countdown(t): 
		turtlex=turtle.Turtle()
		turtlex.hideturtle()
		turtlex.up() 
		turtlex.color('white')
		turtlex.setposition(-400,250)
		t=5
		while t>0 : 
			turtlex.write(t, font = ("Arial", 40, "normal"))
			turtlex.forward(20)
			turtlex.write(".......", font = ("Arial", 40, "normal"))
			turtlex.forward(100)
			time.sleep(1)
			t-=1
		turtlex.write("START!!!", font = ("Arial", 40, "bold"))

	def accelerate(turtle):
		turtle.forward(randint(25,30))

	def slow(turtle,i):
		n = randint(1,3)
		if turtle.xcor() - n > -WIDTH // 2 + 20:
			turtle.forward(n)
		else: turtle.setx(-WIDTH // 2 + 20)
		if i < 30:
			return i+1
		else: 
			return 0

	def restart(turtle): 
		turtle.clear()
		turtle.hideturtle()
		turtle.setx(-WIDTH // 2 + 20)
		turtle.showturtle()

	def reverse(turtle,i):
		if i == 15: turtle.right(180)
		if i == 14: turtle.right(180)
		n = randint(5,10)
		if turtle.xcor() - n > -WIDTH // 2 + 20:
			turtle.forward(n)
		else:
			turtle.setx(-WIDTH // 2 + 20)
		if i == 15: 
			return 0
		else: 
			return i+1

	def finish(turtle):
		turtle.setx(WIDTH // 2 - 20)

	def stop(turtle,i):
		turtle.forward(0)
		if i < 30:
			return i+1
		else:
			return 0

	def teleport(turtle):
		turtle.ht()
		turtle.setx(turtle.xcor()+35)
		turtle.st()

	def chonbua(turtle):
		n=randint(1,17)
		if n>=1 and n<=7:
			teleport(turtle)

		if n>=8 and n<=14:
			accelerate(turtle)

		if n>=15 and n<=16:
			restart(turtle)
	
		if n == 17:
			finish(turtle)
	

	def race(set): #hàm chạy+ tính tg,tìm người thắng+xếp hạng
		create_finish_line()
		T = create_turtles(set)
		line = WIDTH // 2 - 50
		x = 0
		countdown(t)
		start=time.time()
		i0 = 30
		l0 = 30
		g0 = 15
		i1 = 30
		l1 = 30
		g1 = 15
		i2 = 30
		l2 = 30
		g2 = 15
		i3 = 15
		l3 = 30
		g3 = 15
		i4 = 30
		l4 = 30
		g4 = 15
		while x < line:
			x1 = T[1].xcor()
			x2 = T[2].xcor()
			x3 = T[3].xcor()
			x4 = T[4].xcor()
			x0 = T[0].xcor()
			if (x0 < line):
				k = randint(-350,350)
				k1 = randint(-350,350)
				k2 = randint(-350,350)
				k3 = randint(-350,350)
				if abs(x0-k2)<=2 or g0 < 15:
					g0 = reverse(T[0], g0)
				else: 
					if abs(x0-k1)<=5 or l0 < 30:
						l0 = stop(T[0],l0)
					else:
						if abs(x0-k)<=5 or i0 < 30:
							i0 = slow(T[0],i0)
						else: 
							if abs(x0-k3)<=8:
								chonbua(T[0])
							else:
								T[0].forward(randint(5,10))
				end1=time.time()
				time1=end1-start
			else:
				T[0].setx(WIDTH // 2 - 20)
				
			if (x1 < line):
				k = randint(-350,350)
				k1 = randint(-350,350)
				k2 = randint(-350,350)
				k3 = randint(-350,350)
				if abs(x1-k2)<=2 or g1 < 15:
					g1 = reverse(T[1], g1)
				else: 
					if abs(x1-k1)<=5 or l1 < 30:
						l1 = stop(T[1],l1)
					else:
						if abs(x1-k)<=5 or i1 < 30:
							i1 = slow(T[1],i1)
						else: 
							if abs(x1-k3)<=8:
								chonbua(T[1])
							else:
								T[1].forward(randint(5,10))
				end2=time.time()
				time2=end2-start
			else:
				T[1].setx(WIDTH // 2 - 20)
				
			if (x2 < line): 
				k = randint(-350,350)
				k1 = randint(-350,350)
				k2 = randint(-350,350)
				k3 = randint(-350,350)
				if abs(x2-k2)<=2 or g2 < 15:
					g2 = reverse(T[2], g2)
				else: 
					if abs(x2-k1)<=5 or l2 < 30:
						l2 = stop(T[2],l2)
					else:
						if abs(x2-k)<=5 or i2 < 30:
							i2 = slow(T[2],i2)
						else: 
							if abs(x2-k3)<=8:
								chonbua(T[2])
							else:
								T[2].forward(randint(5,10))
				end3=time.time()
				time3=end3-start
			else:
				T[2].setx(WIDTH // 2 - 20)

			if (x3 < line): 
				k = randint(-350,350)
				k1 = randint(-350,350)
				k2 = randint(-350,350)
				k3 = randint(-350,350)
				if abs(x3-k2)<=2 or g3 < 15:
					g3 = reverse(T[3], g3)
				else: 
					if abs(x3-k1)<=5 or l3 < 30:
						l3 = stop(T[3],l3)
					else:
						if abs(x3-k)<=5 or i3 < 30:
							i3 = slow(T[3],i3)
						else: 
							if abs(x3-k3)<=8:
								chonbua(T[3])
							else:
								T[3].forward(randint(5,10))
				end4=time.time()
				time4=end4-start
			else:
				T[3].setx(WIDTH // 2 - 20)

			if (x4 < line): 
				k = randint(-350,350)
				k1 = randint(-350,350)
				k2 = randint(-350,350)
				k3 = randint(-350,350)
				if abs(x4-k2)<=2 or g4 < 15:
					g4 = reverse(T[4], g4)
				else: 
					if abs(x4-k1)<=5 or l4 < 30:
						l4 = stop(T[4],l4)
					else:
						if abs(x4-k)<=5 or i4 < 30:
							i4 = slow(T[4],i4)
						else: 
							if abs(x4-k3)<=8:
								chonbua(T[4])
							else:
								T[4].forward(randint(5,10))
				end5=time.time()
				time5=end5-start
			else:
				T[4].setx(WIDTH // 2 - 20)
			x = min(x1,x2,x3,x4,x0)
			timemin=(time1,time2,time3,time4,time5)
		if(timemin==time1):
			T[0].left(720)
			T[0].forward(200)
			T[1].left(90)
			T[2].left(90)
			T[3].left(90)
			T[4].left(90)
		if(timemin==time2):
			T[1].left(720)
			T[1].forward(200)
			T[0].left(90)
			T[2].left(90)
			T[3].left(90)
			T[4].left(90)
		if(timemin==time3):
			T[2].left(720)
			T[2].forward(200)
			T[1].left(90)
			T[0].left(90)
			T[3].left(90)
			T[4].left(90)
		if(timemin==time4):
			T[3].left(720)
			T[3].forward(200)
			T[1].left(90)
			T[2].left(90)
			T[0].left(90)
			T[4].left(90)
		if(timemin==time5):
			T[4].left(720)
			T[4].forward(200)
			T[1].left(90)
			T[2].left(90)
			T[3].left(90)

		a=[('The red turtle',time1),('The green turtle',time2),('The blue turtle',time3),('The yellow turtle',time4),('The purple turtle',time5)]
		def take_second(elem): 
			return elem[1]
		b=sorted(a,key=take_second)
		bangxephang = Tk()
		name = Label(bangxephang, text = "The 1: "+str(b[0])).grid(row = 0, column = 0) 
		name = Label(bangxephang, text = "The 2: "+str(b[1])).grid(row = 1, column = 0)
		name = Label(bangxephang, text = "The 3: "+str(b[2])).grid(row = 2, column = 0)	
		name = Label(bangxephang, text = "The 4: "+str(b[3])).grid(row = 3, column = 0)
		name = Label(bangxephang, text = "The 5: "+str(b[4])).grid(row = 4, column = 0)
		bangxephang.mainloop()
		time.sleep(5)

	def create_turtles(set): #hàm tạo rùa
		turtles = []
		spacingx = 700 // 8
		newsize = (100, 100)
		for i in range(5):
			racer = turtle.Turtle()
			if set==1:
				shape = str('crt/i/gif1/t' + str(i+1) + '.gif')
				addshape(shape)
				racer.shape(shape)
			if set == 2:
				shape = str('crt/i/gif2/t' + str(i+1) + '.gif')
				addshape(shape)
				racer.shape(shape)
			if set == 3:
				shape = str('crt/i/gif3/t' + str(i+1) + '.gif')
				addshape(shape)
				racer.shape(shape)
			if set == 4:
				shape = str('crt/i/gif4/t' + str(i+1) + '.gif')
				addshape(shape)
				racer.shape(shape)
			if set == 5:
				shape = str('crt/i/gif5/t' + str(i+1) + '.gif')
				addshape(shape)
				racer.shape(shape)
			racer.penup()
			racer.setpos(-700 // 2-100, HEIGHT // 4 - spacingx * i )
			turtles.append(racer)
		return turtles


#tạo đường kẻ kết thúc
	def create_finish_line(): 
		gap_size = 20
		shape("square")
		penup()
		color("white")
		for i in range(10):
			goto(WIDTH // 2 - 20, (HEIGHT // 4 + 20 - gap_size - (i * gap_size * 2)))
			stamp()
			goto(WIDTH // 2 - 20 - gap_size, (HEIGHT // 4 + 20 - (i * gap_size * 2)))
			stamp()
		color("black")
		for i in range(10):
			goto(WIDTH // 2 - 20 - gap_size, (HEIGHT // 4 + 20 - gap_size - (i * gap_size * 2)))
			stamp()
			goto(WIDTH // 2 - 20, (HEIGHT // 4 + 20 - (i * gap_size * 2)))
			stamp()

	def init_turtle(bg):
		screen = turtle.Screen()
		if bg == 1:
			screen.bgpic('bg/background1.gif')
		if bg == 2:
			screen.bgpic('bg/background2.gif')
		if bg == 3:
			screen.bgpic('bg/background3.gif')
		screen.screensize(1280,800)
		screen.setup(1500, 850)
		screen.title('B O N - R A C E')

	t=5
	racers = 5
	init_turtle(bg)
	race(set)
	time.sleep(5)
