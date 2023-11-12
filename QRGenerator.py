import qrcode
from tkinter import *

# title, size
cp=Tk()
cp.title('QR Generator')
cp.geometry('500x500')
cp.config(bg='#261797')

# file saved! message

def generate():
  img = qrcode.make(msg.get())
  type(img)
  img.save(f'{save_name.get()}.png')
  Label(cp, text='File Saved!', bg='#3353fa', fg='black', font=('Arial Black', 18)).pack()

def show():
  img = qrcode.make(msg.get())    
  type(img)
  img.show()

frame = Frame(cp,bg='#3353fa')
frame.pack(expand=True)

# enter the text or url

Label (frame,text='Enter Text or URL:',font=('Arial Black',14),
   bg='#3353fa').grid(row=0,column=0,sticky='w')

msg = Entry(frame)
msg.grid(row=0,column=1)

# enter the file name

Label( frame,text='File Name(Save As):',font=('Arial Black',14),
   bg='#3353fa').grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

# buttons to show or save qrcode

btn = Button(cp, text='Show QR code', bd='15', command=show, width=15)
btn.pack()
btn = Button(cp, text='Save QR code', command=generate, bd='15',width=10)
btn.pack()

cp.mainloop()
