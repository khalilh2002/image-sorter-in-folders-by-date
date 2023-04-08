import tkinter.filedialog as tk
import os
import shutil
from tkinter import *
import tkinter.messagebox
import time

def file_manager(path_name,dir_name,i):
    os.chdir(path_name)
    new_path = os.path.join(path_name, dir_name)
    file_list = os.listdir()
    if dir_name not in file_list:
        os.mkdir(new_path)
    shutil.move(i, new_path)

window=Tk()
window.geometry("400x100")
window.title('code for file manager')


answer = tkinter.messagebox.askokcancel(title='start',message='do you want to start')
if answer:
    path_name=tk.askdirectory(initialdir='/home/khalil/',title='chose folder')
    try:
        os.chdir(path_name)
    except Exception:
        print('empty')

    file_list=os.listdir()
    num=len(file_list)

    if num==0 :
        print("empty dir ...exit")
        exit(0)
    count = 0
    for i in file_list:

        if i[:3]== 'IMG':
            dir_name=i[4:8]+'_folder'
            file_manager(path_name,dir_name,i)

        elif i[:4]=='PANO':
            dir_name = i[5:9] + '_folder'
            file_manager(path_name,dir_name,i)

        elif i[:4]=='Scre':
            dir_name = i[11:15] + '_folder'
            file_manager(path_name,dir_name,i)

        elif i[:8]=='Snapchat':
            dir_name = 'Snapchat_folder'
            file_manager(path_name,dir_name,i)
        else:
            try:
                if 2000 <=  int(i[:4]) <= 2050:
                    dir_name=i[:4]+'_folder'
                    file_manager(path_name, dir_name, i)
                else:
                    dir_name = 'other_folder'
                    file_manager(path_name, dir_name, i)
            except Exception :
                dir_name = 'other_folder'
                file_manager(path_name, dir_name, i)
        count+=1
    if count==num:
        print('done')
        Label(window, text='Done', font=('arial', 20, 'bold'), fg='Green').pack()

    else:
        print('faild')
        Label(window, text='Faild', font=('arial', 20, 'bold'), fg='red').pack()
else:
    x=5
    mg=Label(window, text='Exit after {}'.format(x), font=('arial', 20, 'bold'), fg='black')
    while x!=0:
        mg.config(text='Exit after ...{}'.format(x))
        mg.pack()
        x-=1
        time.sleep(0.8)
        window.update()
    exit(0)

window.mainloop()