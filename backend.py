import random
class Message:
    def __init__(self,message="Default Message",success = True):
        self.message = message
        self.success = success

class Backend:
    def button1(self)->Message:
        success = False
        if random.randint(1,100) > 50:
            success = True
        message = Message(message = "Knapp 1", success=success)
        return message
    def button2(self)->Message:
        message = Message(message = "Knapp 2", success=False)
        return message

    def button3(self)->Message:
        message = Message(message = "Knapp 3", success=False)
        return message

    def button4(self)->Message:
        message = Message(message = "Knapp 4", success=True)
        return message

    def button5(self)->Message:
        message = Message(message = "Knapp 5", success=True)
        return message
