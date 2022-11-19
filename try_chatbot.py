'''Group members:
Elikem Asudo Tsatsu Gale-Zoyiku (56042025)
Marvellous Chapfura (60352025)
Belinda Dzifa Esi Gasu (90762025)
Bright Michael Gyau (79212025)
'''
#creating module called try_chatbot.
#We will call functions and variables from this module in creating the GUI application
bot_name='EliBot'
#setting the bot's name to 'EliBot'
def elibot_responses(vbg):
    #function created that accepts a parameter which the bot will respond to 
    import aiml
    #the inbuilt AIML module
    elibot_kernel=aiml.Kernel()
    #the elibot_kernel is initialized
    elibot_kernel.learn(r"std_startup_elibot.xml")
    #the elibot_kernel is set to learn from a setup AIML/XML file 
    elibot_kernel.respond('Start Session')
    #the elibot_kernel is set to respond to a particular phrase
    #when the kernel responds to this ('Start Session'), the actual AIML file is loaded, and the bot can access it
    while True:
        return(elibot_kernel.respond(vbg))
    # an infinite loop to set the bot to always respond to input from the user