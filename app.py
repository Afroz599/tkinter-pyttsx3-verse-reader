#Importing modules
import pyttsx3
import tkinter as tk
root=tk.Tk()
root.geometry('500x300')
root.title("Healing Touch")
root.configure(bg='black')
label1=tk.Label(root,text="Verses that soothens Heart",font=('Arial',20,'italic')).pack(fill='x',pady=4)
#Creating a dictionary for mapping user input and verses
verses = {
    "happy": "In problems seek Allah's help with sabar and salah",
    "sad": "Do not grieve, indeed Allah is with us",
    "stressed": "Verily, in the remembrance of Allah do hearts find rest",
    "angry": "Those who control anger and forgive people, Allah loves them",
    "lonely": "Allah is closer to you than your jugular vein",
    "Pride":"Do not walk upon the earth arrogantly. Indeed, you will never tear the earth [apart], and you will never reach the mountains in height."
}
#creating function for speech
def say():
    mood=Entr.get()
    mood=mood.lower()
    if mood in verses:
        engine=pyttsx3.init()
        engine.say(verses[mood])
        engine.runAndWait()
    else:
        pass
#user input
label2=tk.Label(root,text="Enter Your current Mood:",font=('Arail',10),fg='Green').pack()
Entr=tk.Entry(root)
Entr.pack(pady=3)
#click to activate function
btn1=tk.Button(root,text='click',font=('Arial',10),command=say).pack(pady=7)
labe3=tk.Label(root,text="Inspired from \n Quran Verses in a Jar",font=('Arial',9)).pack(pady=71)
root.mainloop()
