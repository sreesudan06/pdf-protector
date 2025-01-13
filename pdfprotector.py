from tkinter import * # import all the components of the Tkinter module into your py script.
from tkinter import filedialog # submodule used for creating file and directory selection dialogs in your GUI application.
from tkinter import messagebox #this module allows you to show messages/info to users. 
import PyPDF2 #this module allows you to perform various operations like reading, writing, and modifying PDFs.
import os 

def main_entry():

    root = Tk()
    root.title("PDF protector")
    root.geometry("600x430+300+100")
    root.resizable(False,False)


    #Open a file dialog to select a file
    def browse():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="select a file",
                                            filetype=(('pdf file','*.pdf'),('all files','*.*')))
        entry1.insert(END,filename)

    # file handling and exception handling opertions 
    def protect():
        mainfile=source.get()
        protectfile=target.get()
        code=password.get()
        print(f"mainfile : {mainfile}, protectfile : {protectfile}, pwd:{code}")
        if mainfile=="" and protectfile=="" and code=="":
            messagebox.showerror("invalid","all entries are empty!!")

        elif mainfile=="":
            messagebox.showerror("invalid","please type source pdf filename")

        elif protectfile=="":
            messagebox.showerror("invalid","plaese type target pdf filename")    

        elif code=="":
            messagebox.showerror("inavlid","please type password")

        else:
            try:
                print("trial")
                print(f"file : {filename}")
                out=PyPDF2.PdfWriter()
                file=PyPDF2.PdfReader(filename)

                for page in file.pages:
                    out.add_page(page)

                #password
                out.encrypt(code)

                with open(protectfile,"wb") as f:        #opening new file
                   out.write(f)                          #writing into new file

                source.set("")  
                target.set("")
                password.set("")

                messagebox.showerror("info","Sucessfully done!!")

            except:
                messagebox.showerror("invalid","invalid entry!!")  

    #icon
    image_icon=PhotoImage(file="image/reset-password.png")

    root.iconphoto(False,image_icon)

    #main 
    top_image=PhotoImage(file="image/banner_4.png")
    Label(root,image = top_image).pack()

    frame=Frame(root,width=580,height=290,bd=5,relief=GROOVE)
    frame.place(x=10,y=130)

    ##1
    source=StringVar()
    Label(frame, text= "Source PDF File:",font= "arial 10 bold",fg= "#4c4542") .place(x=30,y=50)
    entry1=Entry(frame, width=30, textvariable=source, font= "arial 15" ,bd=1)
    entry1.place(x=150, y=48)

    Button_icon=PhotoImage(file="image/play.png")
    Button(frame,image=Button_icon, width=35, height=24, bg="#f2f2f2",command=browse).place(x=500,y=47)

    ##2
    target=StringVar()
    Label(frame, text= "Target PDF File:",font="arial 10 bold" ,fg="#4c4542").place(x=30,y=100)
    entry2=Entry (frame, width=30, textvariable=target, font= "arial 15" ,bd=1)
    entry2.place(x=150,y=100)

    ##3
    password=StringVar()
    Label(frame, text= "Set User Password:",font= "arial 10 bold" ,fg="#4c4542").place(x=15,y=150)
    entry3=Entry(frame, width=30, textvariable=password, font= "arial 15" ,bd=1)
    entry3.place(x=150,y=150)

    button_icon=PhotoImage(file= "image/play.png")
    Protect=Button(root, text= "Protect PDF File" ,compound=LEFT, image=button_icon,width=230, height=50, bg= "#f2f2f2",font="arial 14 bold",command=protect).place(x=200,y=330)

    root.mainloop()

main_entry()