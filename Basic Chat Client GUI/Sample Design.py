from tkinter import *

# Main Window of the Client Application
root = Tk()
root.geometry("450x500")
root.title("Chat Client GUI")

# To insert the components into a container we want a Frame
frame = Frame(root)

# A single line textbox
text_box = Entry(frame)

# A send button
send_button = Button(frame, text="Send")

# Typical Layout for Chat
text_box.pack(side='left')
send_button.pack(side='left')

frame.pack(side='bottom')

root.mainloop()
