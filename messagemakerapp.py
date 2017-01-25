import tkinter as tk
import tkinter.ttk as ttk

class MessageMakerApp:

    def __init__(self, master):

        #menus
        self.menuBar = tk.Menu(master)
        fileMenu = tk.Menu(self.menuBar)
        helpMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="File", menu=fileMenu)
        self.menuBar.add_cascade(label="Help", menu=helpMenu)

        #add menu to window
        master.config(menu=self.menuBar)

        #configure main window to be resizable
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # create main continaing frame and configure to be resizable
        frame = tk.Frame(master)
        frame.columnconfigure(0,weight=1)
        frame.columnconfigure(1,weight=2)
        frame.rowconfigure(0, weight=1)
        frame.grid(column=0, row=0, sticky=tk.NSEW)

        # create player listbox and add to frame in column 0
        #fills the column and row cell
        self.playerListBox = tk.Listbox(frame, selectmode=tk.EXTENDED)
        self.playerListBox.grid(row=0, column=0, sticky=tk.NSEW)

        # create frame to contain other elements.  Put in column 1
        #fill grid cell
        self.mainFrame = tk.Frame(frame)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.rowconfigure(1, weight=1)
        self.mainFrame.rowconfigure(2, weight=1)
        self.mainFrame.grid(row=0, column=1, sticky=tk.NSEW)

        #create frame to containt message display elements and scrollbar
        # configure so that it fills the row
        self.conversationFrame = tk.Frame(self.mainFrame, bg="blue")
        self.conversationFrame.grid(row=0, column=0, sticky=tk.NSEW)
        # configure so it's cells expand
        self.conversationFrame.columnconfigure(0, weight=1)
        # self.conversationFrame.columnconfigure(1, weight=1)
        self.conversationFrame.columnconfigure(2, weight=1)
        self.conversationFrame.rowconfigure(0, weight=1)

        self.conversationCanvas = tk.Canvas(self.conversationFrame, bg="red")
        self.conversationCanvas.grid(row=0, column=0, sticky=tk.NSEW)

        self.convesationScroll = tk.Scrollbar(self.conversationFrame, command=self.conversationCanvas.yview, orient="vertical")
        self.convesationScroll.grid(row=0, column=1, sticky=tk.NS)

        self.conversationText = tk.Text(self.conversationFrame, bg="green")
        self.conversationText.grid(row=0, column=2, sticky=tk.NSEW)


        self.sendView = tk.Text(self.mainFrame)
        self.sendView.grid(row=1, sticky=tk.NSEW)


        self.buttonFrame = tk.Frame(self.mainFrame)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.rowconfigure(0, weight=1)
        self.buttonFrame.grid(row=2, sticky=tk.NSEW)

        self.authorCombo = ttk.Combobox(self.buttonFrame)
        self.authorCombo.grid(row=0, sticky=tk.W)

        self.appendButton = tk.Button(self.buttonFrame, text="Append")
        self.appendButton.grid(row=0, column=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = MessageMakerApp(root)
    root.mainloop()
