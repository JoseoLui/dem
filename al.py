#!/usr/bin/python
#−∗−coding:utf−8−∗−
from visual import *
from random import *
from time import sleep
#Se define la estructura de la pantalla a desplegar
scene=display() 
scene.title='Atractor_de_Lorenz'
scene.autoscale=0
scene.range=(100, 100, 100) #Tamaño de la escena

r=28.   #Generar soluciones caóticas
S=10.   #Generar soluciones caóticas
b=8./3. #Generar soluciones caóticas

tray=[] #Listas para guardar los valores de trayectoria
bola=[] #dimensión
vel=[]  #velocidad
pos=[]  #y posición

parts=25.
pos0= vector(randint(-10,10), randint(-10,10), randint(-10,10))
def inicio():
	i=0
	while i<parts:
		tray.append(curve(color=(i/parts, 1-i/parts, 0)))
		bola.append(sphere(color=(i/parts, 1-i/parts, 0)))
		vel.append(vector(0, 0, 0))
		pos.append(vector(pos0.x, pos0.y, pos0.z+0.01*i))
		bola[i].pos=pos[i]
		i+=1
t=0
fps=70
dt=1./(3.*fps)

inicio()
while 1 :
	i=0
	while i<parts:
		vel[i].x=S*pos[i].x+S*pos[i].y        #Velocidad en la posición X
		time.sleep(.1)

		vel[i].y=pos[i].x*pos[i].z+r*pos[i].x-pos[i].y
		time.sleep(.1)

		vel[i].z=pos[i].x*pos[i].y-b*pos[i].z
		time.sleep(.1)

		pos[i].x=pos[i].x+vel[i].x*dt
		#time.sleep(.1)

		pos[i].y=pos[i].y*vel[i].y*dt
		#time.sleep(.1)

		pos[i].z=pos[i].z+vel[i].z*dt
		#time.sleep(.1)

		bola[i].pos=pos[i]
		tray[i].append(pos[i])

		i+=1
	t+=dt
	rate(fps)