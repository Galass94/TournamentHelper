from tkinter import Image, Tk, ttk
from PIL import ImageTk, Image

#This program's purpose is to help Tournament Organizers to change names and scores
#It creates 4 text files(p1Name and p2Name, p1Score and p2Score) that can be read by the streaming software
#Simply enter the players' names , hit apply and control the score with the '+' buttons
#Once the set is over, you can enter new names, hit apply and press the 'reset scores' button
#The 'swap sides' button exists for games where lobbies can sometimes randomly switch players around and switches names and scores to correct that


#Save all text box content to seperate files
def saveData():
    #Save player names set in GUI to text files
    with open('p1Name.txt', 'w') as p1N:
        p1N.write(p1Entry.get())
    with open('p2Name.txt', 'w') as p2N:
        p2N.write(p2Entry.get())
    #Save scores to text file, writing a 0 if score text box is empty
    with open('p1Score.txt', 'w') as p1S:
        if p1Score.get() == '':
            p1S.write('0')
        else:
            p1S.write(p1Score.get())
    with open('p2Score.txt', 'w') as p2S:
        if p2Score.get() == '':
            p2S.write('0')
        else:
            p2S.write(p2Score.get())

#Reset scores to 0 by pressing a button
def resetScores():
    #Open text files and reset scores to 0
    with open('p1Score.txt', 'w') as p1S:
        p1S.write('0')
    with open('p2Score.txt', 'w') as p2S:
        p2S.write('0')
    #Change scores in the GUI to display the change
    p1Score.delete(0, 'end')
    p1Score.insert(0, '0')
    p2Score.delete(0, 'end')
    p2Score.insert(0, '0')

#Swap names by pressing a button
def swapNames():
    #Get current player names as variables
    p1Name = p1Entry.get()
    p2Name = p2Entry.get()
    p1S = p1Score.get()
    p2S = p2Score.get()
    #Open text files and replace names with each other
    with open('p1Name.txt', 'w') as p1N:
        p1N.write(p2Name)
    with open('p2Name.txt', 'w') as p2N:
        p2N.write(p1Name)
    with open('p1Score.txt', 'w') as file:
        file.write(p2S)
    with open('p2Score.txt', 'w') as file:
        file.write(p1S)
    #Replace text in GUI to display the change
    p1Entry.delete(0, 'end')
    p1Entry.insert(0, p2Name)
    p2Entry.delete(0, 'end')
    p2Entry.insert(0, p1Name)
    p1Score.delete(0, 'end')
    p1Score.insert(0, p2S)
    p2Score.delete(0, 'end')
    p2Score.insert(0, p1S)

#Increment Score by pressing a button
def incScore(scoreObject):
    #get the current score and  empty the text box
    score = int(scoreObject.get())
    scoreObject.delete(0, 'end')
    #Increase the score by one and insert it into the text box
    scoreObject.insert(0, score+1)
    #Check which text box was passed in and write new score to the correct file
    if '2' in str(scoreObject):
        with open('p1Score.txt', 'w') as file:
            file.write(str(score+1))
    elif '4' in str(scoreObject):
        with open('p2Score.txt', 'w') as file:
            file.write(str(score+1))

#Create the main window
root = Tk()
root.title('Tournament Helper')
root.geometry('503x118')
root.resizable(False, False)
#Create button to swap names
nameButton = ttk.Button(root, text='swap sides', width=16, command=swapNames)
nameButton.grid(row=1, column=3, padx=8)
#Create button to reset scores
scoreButton = ttk.Button(root, text='reset scores', width=16, command=resetScores)
scoreButton.grid(row=2, column=3)
#Create text to label player 1 side
p1Label = ttk.Label(root, text='Player 1')
p1Label.grid(row=0, column=2, pady=[5,0], sticky='e')
#Create text box to enter player1s name
p1Entry = ttk.Entry(root, width=30, justify='right')
p1Entry.grid(row=1, column=0, columnspan=3, padx=[5,0], pady=5)
#Creature text box to enter player1s score and insert 0 as default value
p1Score = ttk.Entry(root, width=4, justify='right')
p1Score.insert(0, '0')
p1Score.grid(row=2, column=2, sticky='e')
#Create text box to enter player2s name
p2Entry = ttk.Entry(root, width=30, justify='left')
p2Entry.grid(row=1, column=4, columnspan=3, padx=[0,5], pady=5)
#Create text box to enter player2s score and insert 0 as default value
p2Score = ttk.Entry(root, width=4, justify='left')
p2Score.insert(0, '0')
p2Score.grid(row=2, column=4, sticky='w')
#Create a button to save all values to a text file
saveButton = ttk.Button(root, text='Apply', command=saveData)
saveButton.grid(row=3, column=3, pady=4)
#Create a clickable button to increment player1s score
p1Plus = ttk.Button(root, width=3, text='+', command=lambda:incScore(p1Score))
p1Plus.grid(row=2, column=2, padx=[0,15])
#Create a clickable Button to increment player2s score
p2Plus = ttk.Button(root, width=3, text='+', command=lambda:incScore(p2Score))
p2Plus.grid(row=2, column=4, padx=[15,0])
#Create text to label player 2 side
p2Label = ttk.Label(root, text='Player 2')
p2Label.grid(row=0, column=4, sticky='w', pady=[5,0])
#Import Goldar Image and resize it to fit the window
goldar = Image.open('GoldarHead.png')
goldar_temp = goldar.resize((50,50), Image.LANCZOS)
smoldar = ImageTk.PhotoImage(goldar_temp)
#Create image labels to display goldar next to the scores
imageLabel = ttk.Label(root)
imageLabel.grid(row=2, column=1, rowspan=2, sticky='e')
imageLabel.configure(image=smoldar)
imageLabel2 = ttk.Label(root)
imageLabel2.grid(row=2, column=5, rowspan=2, sticky='w')
imageLabel2.configure(image=smoldar)
#Direct all code at the main window and keeps it open
root.mainloop()