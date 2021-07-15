#!/usr/bin/python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os 
from tkinter import filedialog


class Window(Tk):

    def __init__(self):
        super(Window, self).__init__()
        
        self.title('Smart USB App')
        self.minsize(500, 400)
        
        self.createLabel()
        self.text_entry()
        
        self.create_labels()
        self.create_menu()
        
        
        
        
        
        
        #self.button = ttk.Button(self, text = 'Start', command = self.Click_me)
        #self.button.grid(column=0, row=2)
        
    def createLabel(self):
        
        labelFont = ('times', 20,  'bold')
        label = Label(self, text = "Smart-USB, course IE202 ")
        label.config(font = labelFont, bg = 'gray', fg = 'orange')
        label.grid(column = 0, row = 0)
        
        self.labelFrame = ttk.LabelFrame(self, text = "Names         ID ")
        self.labelFrame.grid(column = 1 , row = 3 , padx = 20, pady = 40)
        
    def create_labels(self):
            ttk.Label(self.labelFrame, text = "Raghad Alfalati    1816822").grid(column = 1, row = 4)
            ttk.Label(self.labelFrame, text = " Raghad Baeshen  1816822").grid(column = 1, row = 5)
            ttk.Label(self.labelFrame, text = "Asma Sarouji       1805753").grid(column = 1, row = 6)
            ttk.Label(self.labelFrame, text = "Raid Al-Tamimi    1319511").grid(column = 1, row = 7)
            ttk.Label(self.labelFrame, text = "**************************").grid(column = 1, row = 8)
            ttk.Label(self.labelFrame, text = "Insructor:Eng.Asma Siddiqui").grid(column = 1, row = 9)
            
        
        
    #def Click_me(self):
        
        #self.button.configure(text = 'Exit')
        #self.label3.configure( text = "Hello this program is made by Engineering student at KAU")
        #self.lable3.grid(column = 0 , row = 3)
        
        
       # self.button.configure.grid(column = 0, row = 10)
    
    def create_menu(self):
        menuBar = Menu(self)
        self.config(menu= menuBar)
        
        
        help_menu = Menu(menuBar, tearoff = 0)
        menuBar.add_cascade(label = 'Help', menu = help_menu)
        help_menu.add_command(label = "About ", command = self.about)
        
        help_menu.add_command(label = "All files in USB", command = self.all_files)
        
    
    def all_files(self):
        return filedialog.askopenfilename(title = "All files in USB")
        
    def about(self):
        newwin = Toplevel(self)
        
        
        
    def window_close(self):
        self.quit()
        self.destroy()
        exit()
    
    
    
    def text_entry(self):
        self.name = StringVar()
        self.path = StringVar()
        
        self.label = ttk.Label(self, text = "Enter your name")
        self.label.grid(column = 0, row = 3)
        
        self.textbox =  ttk.Entry(self, width = 20 , textvariable = self.name)
        self.textbox.grid(column = 0, row = 4)
        self.textbox.focus()
        
        
        self.button = ttk.Button(self, text = "START" , command = self.click_me)
        self.button.grid(column = 0, row = 5)
        #self.button.configure(state = "disabled")
        
    def click_me(self):
        self.label.configure(text = "Hello " + self.name.get())
        self.label.grid(column = 0, row = 3)
        
        
        self.label = ttk.Label(self, text = "Enter the path name of the file and the extension")
        self.label.grid(column = 0, row = 7)
        
        self.textbox =  ttk.Entry(self, width = 20 , textvariable = self.path)
        self.textbox.grid(column = 0, row = 8)
        self.textbox.focus()
        
        self.button = ttk.Button(self, text = "create file" , command = self.create_file)
        self.button.grid(column = 0, row = 10)
        
        self.button = ttk.Button(self, text = "Open file", command = self.open_file)
        self.button.grid(column = 0, row = 11)
        
        self.button = ttk.Button(self, text = "Rename the file", command = self.rename_info)
        self.button.grid(column = 0, row = 12)
        
        self.button = ttk.Button(self, text = "Copy/paste the file", command = self.paste_info)
        self.button.grid(column = 0, row = 13)
        
        self.button = ttk.Button(self, text = "Move the file", command = self.move_info)
        self.button.grid(column = 0, row = 14)
        
        self.button = ttk.Button(self, text = "Display files", command = self.display_file)
        self.button.grid(column = 1, row = 19)

        self.button = ttk.Button(self, text = "Exit", command = self.window_close)
        self.button.grid(column = 1, row = 20)
        
        self.button = ttk.Button(self, text = "Delete the file", command = self.Delete_file)
        self.button.grid(column = 0, row = 15)
        
    
    
    def display_file(self):
        import time
        import Adafruit_GPIO.SPI as SPI
        import Adafruit_SSD1306
        from PIL import Image
        from PIL import ImageDraw
        from PIL import ImageFont
        import subprocess
        import os 
        RST = 0
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
        disp.begin()
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image1 = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image1)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = -2
        top = padding
        bottom = height-padding
        x = 0
        font = ImageFont.load_default()
        while True:
            os.chdir("/mnt/usb_share")
            text = os.popen("ls").read()
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            disp.clear()
            disp.display()
            draw.text((x, top),       "Names of files: " ,  font=font, fill=255)
            draw.text((x, top+15),     text, font=font, fill=255)
            disp.image(image1)
            disp.display()
            time.sleep(2)
            if disp.height == 64:
                image = Image.open('img1.png').convert('1')
            else:
                image = Image.open('img1.png').convert('1')
                disp.image(image)
                disp.display()
                time.sleep(2)
            if disp.height == 64:
                image = Image.open('img3.jpg').convert('1')
            else:
                image = Image.open('img3.jpg').convert('1')
                disp.image(image)
                disp.display()
                time.sleep(2)
            if disp.height == 64:
                image = Image.open('img4.jpg').convert('1')
            else:
                image = Image.open('img4.jpg').convert('1')
        disp.image(image)
        disp.display()
        time.sleep(2)












    def Delete_file(self):
        self.target = StringVar()
        
        self.label = ttk.Label(self, text = "Are you sure? ")
        self.label.grid(column = 1, row = 11)
        
        self.button = ttk.Button(self, text = "YES", command = self.yes_delete )
        self.button.grid(column = 1, row = 12)
        
        self.button = ttk.Button(self, text = "NO", command = self.no_delete )
        self.button.grid(column = 1, row = 13)
    
    def yes_delete(self):
        import os
        os.remove(str(self.path.get()))
        
    def no_delete(self):
        pass 
    
    
    def move_info(self):
        
        self.target = StringVar()
        
        self.label = ttk.Label(self, text = "      Enter the target path              ")
        self.label.grid(column = 1, row = 7)
        self.textbox =  ttk.Entry(self, width = 20 , textvariable = self.target)
        self.textbox.grid(column = 1, row = 8)
        self.textbox.focus()
        self.button = ttk.Button(self, text = "MOVE" , command =self.move_file )
        self.button.grid(column = 1, row = 9)
        
    def move_file(self):
        import os
        import shutil
        shutil.move(str(self.path.get()),self.target.get())
        
    def rename_info(self):
        self.target = StringVar()
        
        self.label = ttk.Label(self, text = "  Enter the target path and name")
        self.label.grid(column = 1, row = 7)
        self.textbox =  ttk.Entry(self, width = 20 , textvariable = self.target)
        self.textbox.grid(column = 1, row = 8)
        self.textbox.focus()
        self.button = ttk.Button(self, text = "RENAME" , command = self.rename_file )
        self.button.grid(column = 1, row = 9)
    
    def rename_file(self):
        import os
        os.rename(str(self.path.get()), str(self.target.get()))
    
    
    
        
    def paste_info(self):
        self.target = StringVar()
        
        self.label = ttk.Label(self, text = "      Enter the target path              ")
        self.label.grid(column = 1, row = 7)
        self.textbox =  ttk.Entry(self, width = 20 , textvariable = self.target)
        self.textbox.grid(column = 1, row = 8)
        self.textbox.focus()
        self.button = ttk.Button(self, text = "PASTE" , command =self.copy_file )
        self.button.grid(column = 1, row = 9)
        
    def copy_file(self):
        import shutil
        shutil.copy(str(self.path.get()), str(self.target.get()))
        
    
    def create_file(self):
        file = open(str(self.path.get()), 'w+')
        file.close()
    
    def open_file(self):
        import subprocess
        subprocess.call(['xdg-open', str(self.path.get())])
        #os.system(str(self.path.get()))
        
        
        
  
window = Window()
window.mainloop()









































from colorama import init
init()
from colorama import Fore
print(Fore.BLUE + 'HELLO THIS PROGRAM IS MADE BY ENGINEERING STUDENTS IN KAU')

print(Fore.WHITE + '{0:<8}|{1:^8}|{2:>8}'.format('Name', 'ID', 'Major'))
print('{0}'.format('-'*30))
names_list = ['Raghad', 'Raghad', 'Asma', 'Raid']
ID_list = [1805753, 28474, 14479, 4847]
Majors_list = Fore.RED + 'Engineering'

for i in range(4):
    print('{0:<13}|{1:<8}|{2:>8}'.format(Fore.GREEN + names_list[i], ID_list[i], Fore.GREEN + Majors_list))

while 1 : 
         path=input('Enter the path name of the file and extension:\n')
     
         op = int(input(Fore.WHITE + 'Please chose :\n1.Delete the file\n2.Write to the file\n3.Read from the file\n4.Rename the file\n5.Copy and paste the file\n6.Move file\n:'))
         if op == 1:
                
                
                delete = open(path, 'a+')
                mak_sure = input('Are you sure? Yes or No ')
                if mak_sure.lower() == 'yes':
                        
                        print('Deleting now...')
                        import os
                        os.remove(path)
                        print('Complete.')
            
                elif mak_sure.lower() == 'no':
                        print('ok the file will not delete')
                        break
                else: 
                        print('error input!')
         elif op == 2:
             
                data = open(path, 'w')
                info = input('Input the text and data here to add to the file:\n')
                print('Writing....')
                data.write(info)
                print('Complete')
                data.close()
            
         elif op == 3:
                reading = open(path, 'r')
                print('opening the file..')
                print('-----------------------------')
                print(reading.read())
                print('-----------------------------')
                reading.close()
            
                
         elif op == 4:
                new_name = input('Enter the new name with the path for the file: ')
        
                import os 
                os.rename(path, new_name)
                print('Complete')
            
                 
         elif op == 5:
                target_place = input('Please input the target path:\n')
                import shutil
                shutil.copy(path,target_place)
                print('Complete.')
         elif op == 6:
                import os
                import shutil 
                target_place = input('Please input the target path:\n')
                shutil.move(path,target_place)
                print('Complete....')
            
            
            
                
         else:
              print('Error input!')
            
                
        
        
    

    
