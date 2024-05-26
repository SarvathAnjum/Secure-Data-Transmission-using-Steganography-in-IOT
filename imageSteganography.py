from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import os
import cv2
import numpy as np
import random
  

class Stegno:
    output_image_size = 0

    def main(self,root):
        root.title('ImageSteganography')
        root.geometry('700x800')
        root.resizable(width =False, height=False)
        f = Frame(root,bg="#FFE5B4")
        root.configure(bg="#FFE5B4")
       
        
        title = Label(f,text='Image Steganography')
        title.config(font=('verdana',23))
        title.grid(pady=120)       

        b_embed = Button(f,text="Embed",command= lambda :self.frame1_embed(), padx=14)
        b_embed.config(font=('verdana',14))
        b_embed.grid(pady=20)
        b_encode = Button(f,text="Encode",command= lambda :self.frame1_encode(f), padx=14)
        b_encode.config(font=('verdana',14))
        b_decode = Button(f, text="Decode",command=lambda :self.frame1_decode(f), padx=14)
        b_decode.config(font=('verdana',14))
        b_decode.grid(pady =12)

        
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_embed.grid(row=2)
        b_encode.grid(row=3)
        b_decode.grid(row=4)
        
    
        
   
    def frame1_embed(self):
        cover_path = tkinter.filedialog.askopenfilename(title='Select Cover Image')
        img1 = cv2.imread(cover_path)

    # Open the image to hide
        hide_path = tkinter.filedialog.askopenfilename(title='Select Image to Hide')
        img2 = cv2.imread(hide_path)
        for i in range(img2.shape[0]):
            for j in range(img2.shape[1]):
                for l in range(3):
                  
                # v1 and v2 are 8-bit pixel values
                # of img1 and img2 respectively
                    v1 = format(img1[i][j][l], '08b')
                    v2 = format(img2[i][j][l], '08b')
                  
                # Taking 4 MSBs of each image
                    v3 = v1[:4] + v2[:4] 
                  
                    img1[i][j][l]= int(v3, 2)
                  
        cv2.imwrite('hidden_image.png', img1)
        tk.messagebox.showinfo('Success', 'Image is hidden successfully and saved as hidden_image.png in the same directory!')

        cv2.imwrite('captured_image.png',img2);
        tk.messagebox.showinfo('Success', 'Captured Image is saved succesfully as captured_image.png in the same directory')

        
        img = cv2.imread('hidden_image.png') 
        width = img.shape[0]
        height = img.shape[1]
      
    # img1 and img2 are two blank images
        img1 = np.zeros((width, height, 3), np.uint8)
        img2 = np.zeros((width, height, 3), np.uint8)
        tk.messagebox.showinfo('Success', 'Generating the intermediate images!!! This will take a couple of minutes')
      
        for i in range(width):
            for j in range(height):
                for l in range(3):
                    v1 = format(img[i][j][l], '08b')
                    v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                    v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                  
                # Appending data to img1 and img2
                    img1[i][j][l]= int(v2, 2)
                    img2[i][j][l]= int(v3, 2)
      
    # These are two images produced from
    # the encrypted image
    
        cv2.imwrite('intermediate_image1.png', img1)
        tk.messagebox.showinfo('Success', 'Intermediate Image - 1 is saved successfully in the same directory')
        cv2.imwrite('intermediate_image2.png', img2)
        tk.messagebox.showinfo('Success', 'Intermediate Image - 2 is saved successfully in the same directory')
   

        
    def home(self,frame):
            frame.destroy()
            self.main(root)

   

    def frame1_decode(self,f):
        f.destroy()
        d_f2 = Frame(root)
        l2 = Label(d_f2, text='Enter password to decode the stego-image:')
        l2.config(font=('verdana',18))
        l2.grid(pady=30)
        password_entry = Entry(d_f2, show='*')
        password_entry.config(font=('verdana',28))
        password_entry.grid(pady=30)
        
        def verify_password():
            password = password_entry.get()
            if password == 'stegano@908':  # replace with actual password
                self.frame2_decode(d_f2)
            else:
                messagebox.showerror('Incorrect Password', 'The password you entered is incorrect.')
    
    # Add button to verify password
        verify_button = Button(d_f2, text='Verify Password', command=verify_password)
        verify_button.config(font=('verdana',18))
        verify_button.grid(pady=30)


        
        label_art = Label(d_f2, text='')
        label_art.config(font=('verdana',10))
        label_art.grid(row =1,pady=30)
        l1 = Label(d_f2, text='')
        l1.config(font=('verdana',18))
        l1.grid()
        back_button = Button(d_f2, text='cancel', command=lambda : Stegno.home(self,d_f2))
        back_button.config(font=('verdana',18))
        back_button.grid(pady=30)
        back_button.grid()
        d_f2.grid()
        
       
            



    
        

    def frame2_decode(self,d_f2):
        d_f3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Stego Image :')
            l4.config(font=('verdana',18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.decode(myimg)
            l2 = Label(d_f3, text='Hidden data is :')
            l2.config(font=('verdana',18))
            l2.grid(pady=10)
            text_area = Text(d_f3, width=50, height=10)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()
            back_button = Button(d_f3, text='Cancel', command= lambda :self.page3(d_f3))
            back_button.config(font=('verdana',10))
            back_button.grid(pady=8)
            back_button.grid()
            #show_info = Button(d_f3,text='More Info',command=self.info)
            #show_info.config(font=('verdana',9))
            #show_info.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

            
            myimg1 = Image.open('captured_image.png', 'r')
            myimage1 = myimg1.resize((300, 200))
            img2 = ImageTk.PhotoImage(myimage1)
            l4= Label(d_f3,text='Captured Image :')
            l4.config(font=('verdana',18))
            l4.grid()
            panel = Label(d_f3, image=img2)
            panel.image = img2
            panel.grid()
       
            
           



            

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_encode(self,f):
        f.destroy()
        f2 = Frame(root,bg="#FFE5B4")
        label_art = Label(f2, text='')
        #logo=PhotoImage(file="test2.png")
        #Label(root).place(x=50,y=0)
        #logo=PhotoImage(file="download.png")
        #Label(root,image=logo).place(x=110,y=0)
        label_art = Label(f2, text='\'\(°Ω°)/\'')
        label_art.config(font=('verdana',60))
        label_art.grid(row =1,pady=70)
        
        
        l1= Label(f2,text='Select the Image in which \nyou want to hide text :    ')
        l1.config(font=('verdana',18))
        l1.grid()

        bws_button = Button(f2,text='Select',command=lambda : self.frame2_encode(f2))
        bws_button.config(font=('verdana',18))
        bws_button.grid(pady=15)
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda : Stegno.home(self,f2))
        back_button.config(font=('verdana',18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()


    def frame2_encode(self,f2):
        ep= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,100))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep,text='Selected Image')
            l3.config(font=('verdana',18))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Enter the message')
            l2.config(font=('verdana',18))
            l2.grid(pady=15)
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            encode_button = Button(ep, text='Cancel', command=lambda : Stegno.home(self,ep))
            encode_button.config(font=('verdana',11))
            data = text_area.get("1.0", "end-1c")
            back_button = Button(ep, text='Encode', command=lambda : [self.enc_fun(text_area,myimg),Stegno.home(self,ep)])
            back_button.config(font=('verdana',11))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
            f2.destroy()
   

    
   

  
    def genData(self,data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self,pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            # Eigh^th pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self,text_area,myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","Encoding Successful\n Stego Image is saved successfully in the same directory")

    def page3(self,frame):
        frame.destroy()
        self.main(root)

    
    
    

root = Tk()
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#2f4155").place(x=5,y=0)
Label(root,text="",bg="#FFE5B4",fg="white",font="arial 10 bold").place(x=100,y=20)
o = Stegno()
o.main(root)

root.mainloop()
        
