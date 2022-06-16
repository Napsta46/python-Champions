from tkinter import *

BG_COlOR = "#A582F9"
class PythonChampions:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat Bots")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=100)
        
        head_label = Label(self.window,text="Welcome", pady = 10, bg = BG_COlOR)
        head_label.place(relwidth=1)


        



if __name__ == "__main__":
    app = PythonChampions()
    app.run()