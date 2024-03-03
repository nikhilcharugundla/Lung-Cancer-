from tkinter import *
import ctypes,os
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename
import tensorflow.keras.models as models
import cv2
import matplotlib.pyplot as plt
import  numpy as np

        
home = Tk()
home.title("Chest Cancer Detection")

img = Image.open("images/home.png")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-450)
b= str(lt[1]//2-320)
home.geometry("900x653+"+a+"+"+b)
home.resizable(0,0)
file = ''

model = models.load_model('model/model.h5')

def Exit():
    global home
    result = tkMessageBox.askquestion(
        "Chest Cancer Detection", 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        home.destroy()
        exit()
    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')
        
def browse():
    
    global file,l1
    try:
        l1.destroy()
    except:
        pass
    file = askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=( ("images", ".png"),("images", ".jpg"),("images", ".jpeg")))

def predict():
    global file,l1
    if file!='' or file!= None:
        SIZE = 224
        cls = ['adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib', 'large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa', 'Normal', 'squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa']
        nimage = cv2.imread(file)
        image = cv2.resize(nimage,(SIZE,SIZE))
        image = image/255.0
        image = np.array(image).reshape(-1,SIZE,SIZE,3)
        prediction = model.predict(image)
        pred = prediction[0].argmax()
        print(pred)
        pred = cls[pred]+' ( '+str(round(prediction[0][pred]*100,2))+'% )'
        l1 = Label(home,text="Predicted Output Is: "+pred,font=('',14,'bold'),bg="#c4e4e0",fg="#2b4b47")
        l1.place(x=35,y=600)
        plt.imshow(nimage,cmap="gray")
        pValue = "Prediction : {0}".format(pred)
        plt.title(pValue)
        plt.show()

def about():
    about = Toplevel()
    about.title("Chest Cancer Detection")

    img = Image.open("images/about.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(about, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-450)
    b= str(lt[1]//2-320)
    about.geometry("900x653+"+a+"+"+b)
    about.resizable(0,0)
    about.mainloop()
    
photo = Image.open("images/1.png")
img2 = ImageTk.PhotoImage(photo)
b1=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img2,command=browse)
b1.place(x=0,y=209)

photo = Image.open("images/2.png")
img3 = ImageTk.PhotoImage(photo)
b2=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img3,command=predict)
b2.place(x=0,y=282)

photo = Image.open("images/3.png")
img4 = ImageTk.PhotoImage(photo)
b3=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img4,command=about)
b3.place(x=0,y=354)

photo = Image.open("images/4.png")
img5 = ImageTk.PhotoImage(photo)
b4=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img5,command=Exit)
b4.place(x=0,y=426)

home.mainloop()
