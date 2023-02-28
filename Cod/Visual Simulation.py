from tkinter import *
from satelit import *
import time
from math import *
from matplotlib.patches import Ellipse
from PIL import Image,ImageTk

# !!! change the file locations for the background, satelite and planet for the program to be functional !!! (*)
root=Tk()
root.title('Simulare orbita')
root.geometry("793x784")
x_centru = 396
y_centru = 392

#functia pentru a inchide interfara
def quit():
    root.destroy()

#functia de creeare orbita + ozn + planeta

def create():

    button1.config(state='disabled')
    x_size = 2*int(e_1.get())
    y_size = 2*int(e_2.get())
    apogee_distance = int(e_3.get())
    planet_diameter = int(e_5.get())

 
    my_canvas.create_oval( 396-x_size, 392-y_size, 396+x_size, 392+y_size,width = 5)
    elipsa = Ellipse( (396,392), width=x_size*2,height=y_size*2)
    satelit.image = my_canvas.create_image( 396 , 392-y_size,image=imagine)

   
            # Redimensionam planeta in functie de datele introduse
            # 1.11 provinde din faptul ca poza initiala este de dimensiune 75/67 si pastram raportul cand o redimensionam

    width = int(planet_diameter*1.11)
    height = planet_diameter
    resize_image = imagine_planeta.resize((width, height))
 
    imagine_planeta_resized = ImageTk.PhotoImage(resize_image)
    my_canvas.create_image(396-x_size/2+apogee_distance,392,image=imagine_planeta_resized)

            # Variabile path retine traictoria elipsei pe care am creat-o in functie de datele introduse

    path = elipsa.get_path()
 
            # Varibaila vertices este o matrice care contine coordonatele unor puncte de pe elipsa, dar nu in format corect

    vertices = path.vertices.copy()

            # Folosim aceasta functie pentru a transforma coordonatele obtinute anterior intr-un format corect
    vertices = elipsa.get_patch_transform().transform(vertices)

            # Prin bucla while true determinam o miscare continua a satelitului
            # Practic creeam imaginea satelitului in fiecare, trepat in fiecare punct de coordonate care se afla vertices ( cream imagine, se asteapta un timp, o stergem , trecem la urmatoarea)
  
    while True:
            i=0
            for i in range(len(vertices)) :
                x = vertices[i][0]
                y = vertices [i][1]
                if y< 396-planet_diameter/2:
                        my_canvas.delete(satelit.image)
                        satelit.image = my_canvas.create_image( x , y,image=imagine_rotita)
                    
                if y> 396-planet_diameter/2:
                        my_canvas.delete(satelit.image)
                        satelit.image = my_canvas.create_image( x , y,image=imagine)
                        

                my_canvas.update()

                    #Am impartit elipsa in 8 parti egale, pentru care se asteapta o perioada diferita pentru fiecare, pentru a prezenta, orientativ, viteza punctului pe traictorie
                if x_size - y_size> 40:

                    if i < len(vertices)/8:
                        time.sleep(0.1)

                    if i >= len(vertices)/8:
                        if i<=len(vertices)/4:
                            time.sleep(0.15)

                    if i > len(vertices)/4:
                        if i<=3*len(vertices)/8:
                            time.sleep(0.15)

                    if i > 3*len(vertices)/8:
                        if i<=len(vertices)/2:
                            time.sleep(0.1)

                    if i > len(vertices)/2:
                        if i<=len(vertices)/8*5:
                            time.sleep(0.05)
                    
                    if i > len(vertices)/8*5:
                        if i <= len(vertices)/8*6:
                            time.sleep(0.04)
                    
                    if i > len(vertices)/8*6:
                        if i <= len(vertices)/8*7:
                            time.sleep(0.04)
                    
                    if i > len(vertices)/8*7:
                        time.sleep(0.05)

                else:
                    if i < len(vertices)/8:
                        time.sleep(0.1)

                    if i >= len(vertices)/8:
                        if i<=len(vertices)/4:
                            time.sleep(0.1)

                    if i > len(vertices)/4:
                        if i<=3*len(vertices)/8:
                            time.sleep(0.1)

                    if i > 3*len(vertices)/8:
                        if i<=len(vertices)/2:
                            time.sleep(0.1)

                    if i > len(vertices)/2:
                        if i<=len(vertices)/8*5:
                            time.sleep(0.1)
                    
                    if i > len(vertices)/8*5:
                        if i <= len(vertices)/8*6:
                            time.sleep(0.1)
                    
                    if i > len(vertices)/8*6:
                        if i <= len(vertices)/8*7:
                            time.sleep(0.1)
                    
                    if i > len(vertices)/8*7:
                        time.sleep(0.1)

# Am creat canvasul

my_canvas = Canvas(root,width=793,height=784)
my_canvas.pack(fill="both",expand=True)

# Am setat fundalul ca fiind o poza fara drepturi de autor

# (*) HERE!!!!
bg= PhotoImage(file=r"C:\Users\Mihai\Desktop\Eliptic orbit\galaxy.png")
my_canvas.create_image(0,0, image=bg,anchor="nw")


# Am creat locurile pentru a introduce datele ( cu text ajutator ), butonul Create, care creeaza  traictoria, planeta si satelitul + miscarea acestuia

    # Locul de introdus date
e_1 = Entry(root, width=14, borderwidth=5)
e_1.insert(0,"Semi-major axis")

e_2 = Entry(root, width=14, borderwidth=5)
e_2.insert(0,"Semi-minor axis")

e_3 = Entry(root, width=14, borderwidth=5)
e_3.insert(0,"Perigee distance")


''' e_4 = Entry(root, width=6, borderwidth=5) apogee nu era necesar pentru reprezentare '''


e_5 = Entry(root, width=13, borderwidth=5)
e_5.insert(0,"Planet diameter")



#Butoanele; Butonul create este one time use, pentru a se evita creearea mai multor reprezentari in acelasi window( se suprapuneau )

button1 = Button(root, text="Create orbit", command=create)
button1.config(state='normal')
button3_window = my_canvas.create_window(625,35,anchor="nw",window=button1)

button_quit = Button(root, text='Quit', command =quit )
button_quit_window =  my_canvas.create_window(700,720,anchor="nw",window=button_quit)

entry_window1 = my_canvas.create_window(25,35,anchor="nw",window=e_1)
entry_window2 = my_canvas.create_window(175,35,anchor="nw",window=e_2)
entry_window3 = my_canvas.create_window(325,35,anchor="nw",window=e_3)

''' entry_window4 = my_canvas.create_window(410,10,anchor="nw",window=e_4) '''

entry_window5 = my_canvas.create_window(474,35,anchor="nw",window=e_5)




# Initializam satelitul aparine clasei cu acelasi nume si afla in fisierul classes 
# Am intializat in program imaginile folosite pentru satelit, satelit rotit ( satelitul se roteste in punctul de apogee si perigee ) si planeta

satelit = Satelit(my_canvas)
# (*) HERE !!!
imagine = PhotoImage(file=r"C:\Users\Mihai\Desktop\Eliptic orbit\alien.png")
imagine_rotita = PhotoImage(file=r"C:\Users\Mihai\Desktop\Eliptic orbit\alien_reversed.png")
imagine_planeta = Image.open(r"C:\Users\Mihai\Desktop\Eliptic orbit\planet.png")

root.mainloop()