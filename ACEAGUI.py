import tkinter as tk

master = tk.Tk()

def question_finder(course,license):
    print(course,license)
        #Code that returns questions given course and license text here.
        #Pass questions into qlist.  I put two filler questions here.
    questioner(["Would you like to attend a conference?","Would you like to take it in person or online?"], tuple())

def questioner(qlist,answers):
    qs=len(answers)
    answer=tk.Entry(master)
    answer.grid(sticky="e",row=6, column=0)

    next=tk.Button(master,text='Next', command=lambda: questioner(qlist,entry(answers,answer,prompt)))
    next.grid(sticky="e",row=7,column=1)
    if qs<len(qlist):
        prompt=tk.Label(master, text=qlist[qs])
        prompt.grid(sticky="w",row=5,column=0)




    else:
        next.destroy()
        recommender(answers)
        print(answers)

def entry(answers,answer,prompt):
    prompt.destroy()
    return answers+tuple((answer.get(),))


def recommender(answers):
    #This is where the answers are used to give recommendations
    tk.Label(master, text="Recommendations").grid(sticky="w",row=5,column=0)
    tk.Label(master, text="This is the first recommendation").grid(sticky="w",row=6,column=0)
    tk.Label(master, text="This is the second recommendation").grid(sticky="w",row=7,column=0)
    pass

tk.Label(master, text="Course Info:").grid(sticky="w",row=1,column=0)
tk.Label(master, text="License Info:").grid(sticky="w",row=2,column=0)

e1= tk.Entry(master)
e2= tk.Entry(master)

e1.grid(sticky="e",row=1, column=1)
e2.grid(sticky="e",row=2, column=1)

tk.Button(master,text="X",command=master.quit).grid(sticky="w",row=0,column=0)
tk.Button(master,text='Submit', command=lambda: question_finder(e1.get(),e2.get())).grid(sticky="e",row=4,column=1)

tk.mainloop()
