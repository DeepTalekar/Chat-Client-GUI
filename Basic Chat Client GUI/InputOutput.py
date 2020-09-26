'''
Extras: The border can be given by the two commands 
    1. For the thickness
    2. For the Background
    1. ---> highlightthickness = 1(integer)
    2. ---> highlightbackground = "#212"(just an example)

Some may have a default background and hence for a custom/configured background we need to first set the border as zero
For that we have to use the parameter 'bd' (bd=0) when we create a button

'''
from tkinter import *

# Created a Class for the Text in the Placeholder
class placeholderState():
    __slots__ = 'default_color','placeholder_text', 'placeholder_color', 'state_placeholder'
    '''
    This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances.
    For More info on the Cautions and Notes on the Use of '__slots__' can be found from the following link:
    https://docs.python.org/3/reference/datamodel.html#slots
    '''

# Main Window of the Client Application
root = Tk()
root.geometry("600x600")
root.title("Chat Client GUI")

# To insert the components into a container we want a Frame
outside_frame = Frame(root, width= 300, height= 400)
inside_frame1 = Frame(outside_frame,  pady=10)  # Added Some Y padding
inside_frame2 = Frame(outside_frame,  pady=10)



# To print the data entered by the Client in the Text area 
recieve_send_data = Text(inside_frame1, width= 45)
recieve_send_data.bind("<Key>", lambda x : "break")     # We Dont Need the Client to edit the Text area so we Restrict it



# Event Handler For the Button to Display the Text entered into the Text area
def show_sent_message(event):
    global recieve_send_data, text_box
    i = text_box.get()
    if len(i) == 0:
        print("Nothing to be Send")
    else:
        recieve_send_data.insert(END, "{} \n".format(i))
        text_box.delete(0, END)


# To Display the Placeholder
def placeholder(box, placeholder_text, color = "grey"):
    default_color = box.cget('fg')  # Reteriving the Color of the Font Used in the Box where we want to place the Placeholder

    state = placeholderState()                      # Creating an Object state of the type placeholderState()
    state.default_color = default_color             # Setting the Default Foreground Color when the User Focuses Into the component(here Entry)
    state.placeholder_text = placeholder_text       
    state.placeholder_color = color                 # Setting the Default Color when the User Focuses Into the  component(here Entry)
    state.state_placeholder = True                  # Since when the window is made there should be a Placeholder 

    def focusIn(event, box= box, state= state):
        # Since when the Focus is In the Component(here Entry) the Foreground color should be the default one 
        # And the Placeholder text shouldn't be displayed hence we delete the Placeholder text
        if state.state_placeholder: 
            box.delete(0, END)
            box.config(fg = state.default_color)
        
        # Setting the Placeholder state as False Since the cursor Focuses on the Component
        state.state_placeholder = False
    
    def focusOut(event, box= box, state = state):
        # If the Focus is gone out of the Component then the Placeholder text should again come into the picture 
        # And hence retrive the Foreground color of the placeholder and the text
        if box.get() == '':
            box.insert(0, state.placeholder_text)
            box.config(fg = state.placeholder_color)

        # Also modifying the State of the Placeholder as True again
        state.state_placeholder = True
    
    # Inserting the Placeholder text into the component and also modifying the Foreground color
    box.insert(0, placeholder_text)
    box.config(fg = color)

    # Binding the component when its in Focus and when its out of Focus
    box.bind("<FocusIn>", focusIn)
    box.bind("<FocusOut>", focusOut)


    return state



# A single line textbox
text_box = Entry(inside_frame2, width= 50)
# Demanding the Text to be set as Placeholder Text
placeholder(text_box, "Type a message")

# A send button
send_button = Button(inside_frame2, text="Send")
# Binded the Event Handler to the Event to be performed with this Component
send_button.bind("<Button>", show_sent_message)


# Typical Layout for Chat
text_box.pack(side='left',padx=5)
send_button.pack(side='left',padx=5)
recieve_send_data.pack(fill=Y)
inside_frame1.pack()
inside_frame2.pack(side='bottom')

outside_frame.pack(fill=Y, expand=True)
root.mainloop()