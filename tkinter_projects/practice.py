# from tkinter import *

# if __name__ =="__main__":
#     root=Tk()
#     root.geometry("644x728")
#     root.title("Untitled - Notepad")
#     # Add textarea
#     textArea=Text(root,font="lucida 30")
#     # root.mainloop()

from tkinter import*

if __name__ == "__main__":
    root=Tk()
    root.geometry("644x728")
    root.title("Untiled -Notepad")
    # Add textarea
    textArea=Text(root,font="lucida 30")
    File = None
# Menu bar
    menuBar=Menu(root)
    # File menu
    FileMenu=Menu(menuBar,tearoff=0)
    # ADDINg
    FileMenu.add_command(label="new",command=newFile)
    FileMenu.add_command(label="Open",command=openFile)
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=exitFile)
    menuBar.add_cascade(label="File",menu=menuBar)

    # Edit file for Cut Copy Paste
    editFile=Menu(menuBar)
    editFile.add_command(label="Cut",command=cut)
    editFile.add_command(label="copy",command=copy)
    editFile.add_command(label="paste",command=paste)
    menuBar.add_cascade(label="Edit",menu=menuBar)

    helpFile=Menu(menuBar,tearoff=0)
    helpFile.add_command(label="About notepad",command=about)
    menuBar.add_cascade(label="Help",menu=menuBar)

    root.config(menu=menuBar)



    # textArea=Text(root,font="lucida 30")
    # File = None

    root.mainloop()