'''Group members:
Elikem Asudo Tsatsu Gale-Zoyiku (56042025)
Marvellous Chapfura
Belinda Dzifa Esi Gasu (90762025)
Bright Michael Gyau (79212025)
'''
from tkinter import *
#importing all functions from tkinter to create the chatbot window
from try_chatbot import elibot_responses, bot_name
#importing functions and variables from try_chatbot module created by us
BG_GRAY='#ABB289'
BG_COLOR='#17202A'
TEXT_COLOR='white'
FONT='ComicSansMS'
FONT_BOLD='ComicSansMS 13 bold'
#creating variables that will be used in creating chatbot window

class Chat_Bot:
    #creating a class to initialize a Chat_Bot object
    def __init__(self):
        #constructor to initialize Chat_Bot attributes
        self.window=Tk()
        #creating a window/canvas for chatbot
        self._setup_main_window()
        #calling _setup_main_window method
    def run(self):
        self.window.mainloop()
        #method to run GUI application indefinitely until it's closed
    def _setup_main_window(self):
        # _setup_main_window method to create widgets for chatbot window
        self.window.title(bot_name)
        #creating and configuring chatbot window
        self.window.resizable(width=False,height=False)
        #the window is set to not be resizable
        self.window.configure(width=600,height=600,bg='#4a7abc')
        #the height and width of the window are set, background color also
        #creating,configuring, and placing the head of the chatbot window
        head_label=Label(self.window,bg='beige',fg='black',text=' ',font=FONT_BOLD,pady=10)
        head_label.place(relwidth=1)
        #
        #line=Label(self.window,width=450,bg='red')
        #line.place(relwidth=1,rely=0.4,relheight=0.012)
        # creating a text widget which will display the user's message and the bot's response
        self.text_widget=Text(self.window,width=20,height=2,bg='white',fg='black',font='ComicSansMS',padx=5,pady=5)
        self.text_widget.place(relheight=0.8,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor='arrow',state=DISABLED)
        #placing and configuring the text widget
        #
        scrollbar=Scrollbar(self.text_widget)
        #creating a scrollbar for the chatbot window so previous messages can be seen
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        #placing and configuring the scrollbar
        #
        bottom_label=Label(self.window,bg='beige',height=80)
        #creating a bottom for the chatbot window in which user will enter messages etc.
        bottom_label.place(relwidth=1,rely=0.825)
        #
        self.message_entry=Entry(bottom_label,bg='white',fg='black',font=FONT)
        #text entry box in which messages to the bot will be entered
        self.message_entry.place(relwidth=0.74,relheight=0.03,rely=0.009,relx=0.011)
        #placing the text entry box within the bottom
        self.message_entry.focus()
        #making sure the cursor is always in the text entry box whenever the application starts
        self.message_entry.bind('<Return>',self._on_enter_pressed)
        #binding a function to the message entry box. This will send the message typed in the message entry box to the bot whenever the enter button is pressed
        send_button=Button(bottom_label,text='SEND',command=lambda:self._on_enter_pressed(None),font=FONT_BOLD,width=20,bg='light blue')
        #creating a send button which will send the message the user types to the bot
        send_button.place(relx=0.77,rely=0.009,relheight=0.03,relwidth=0.22)
        #placing the send button in the bottom of the chatbot window
    def _on_enter_pressed(self,event):
        #creating a _on_enter_pressed method which will take whatever a user has typed
        #in the text entry box when enter is pressed or the send button is pressed
        #it takes event as a parameter (event is if the Return key is pressed( from the binding ))
        message=self.message_entry.get()
        #function to get message from text entry box
        self._insert_message(message,'You')
        #calling the _insert_message method
    def _insert_message(self,message,sender):
        #creating a _insert_message method which takes a message and the sender name as parameters
        if not message:
            return
        self.message_entry.delete(0,END)
        #clears the text_entry box after every message the user enters
        message1=f'{sender}: {message}\n\n'
        self.text_widget.configure(state=NORMAL)
        #activates the text widget so a message can be inserted for the user to see
        self.text_widget.insert(END,message1)
        #inserts the users message in the text widget
        self.text_widget.configure(state=DISABLED)
        #the text widget is deactivated
        #
        self.message_entry.delete(0,END)
        #clears the text entry box after user presses send or enter/return
        message2=f'{bot_name}: {elibot_responses(message)}\n\n'
        #the message from the entry box is passed into the elibot_responses function which elicits a response from the bot
        self.text_widget.configure(state=NORMAL)
        #activates the text widget for the bot's responses to be entered for the user to see
        self.text_widget.insert(END,message2)
        #the reply from the bot is displayed in the text widget
        self.text_widget.configure(state=DISABLED)
        #the text widget is deactivated
        self.text_widget.see(END)
        #the text widget is set to display the last message in  it

if __name__=='__main__':
    app=Chat_Bot()
    app.run()
#an object called app is created using the Chat_Bot class.
#the class takes no parameters because the __init__ constructor does not take any parameters
#the 'run' method of the object is called
