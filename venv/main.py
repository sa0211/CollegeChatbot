from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *


bot=ChatBot("My Bot")

convo=[
    'Hi',
    'HELLO!! how are you doing?',
    'I am doing great.', ''
    'That is good to hear',
    'Yup.',
    'How may I help you',
    'I wanted some info about this college',
    'YES!!, I am here to help you, You can ask me anything I would answer',
    'What is the name of the college',
    'XYZ College',
    'Who is the Principal of this College',
    'Principal of XYZ is ....',
    'This college comes under which University',
    'Mumbai University',
    'ok.',
    'Yes',
    'What are the types of courses College provides?',
    'The College provides with Courses like Computer, Electrical, Mechatronics, Mechanical and Civil !!',
    'can I get contact details of college',
    'Yes!! Put your College contact details',
    'Thanks.',
    'Yeah Sure',
    'who is the placement incharge of college',
    'Placement Incharge of College is Dr. XYZ person',
    'which companies come for placement in your college?',
    'Companies like Capgemini, TATA, Wipro, L&T Infotech, Accenture and many more',
    'What are the college timings',
    '9:00 am to 05:00 pm',
    'online classes are conducted through which medium',
    'Online Classes are conducted with the help of Google Meet',
    'through which medium students get their notes',
    'Students get their notes and important notification via Google Classroom',
    'what is the official website of college',
    'https://XYZ.ac.in/',
    'Are seminars and webinars held in College',
    'Yes, Webinars and Seminars are held in College for Students',
    'ohh that is good.',
    'YES !!',
    'Who is the HOD of computer department',
    'HOD of Computer Department is Dr. XYZ person',
    'are extra curricular activities held in college ?',
    'Yes !!',
    'what are the extra activites held plz mention',
    'Sure! Activities Like - Industrial Visits etc are held',
    'is canteen facility provided by college',
    'YES ! Canteen facility is provided by College',
    'ok thank you for the information',
    'Thank  you  for  reaching  out  to  BOT !!'
    'Have a nice day.'
]


trainer=ListTrainer(bot)


#Bot training using trainers

trainer.train(convo)
print("Hello,you can enter or drop your queries to our Bot!")
#while True:
    #query=input("Enter your question here: ")
    #if query=='exit':
     #   break
    #answer=bot.get_response(query)

answer=bot.get_response("Which website is this")
print("Bot Response: ",answer)

main = Tk()

main.geometry("500x650")

main.title(" College Enquiry Bot ")
img=PhotoImage(file="img.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)



def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)



frame=Frame(main)


sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)


sc.pack(side=RIGHT,fill=Y)



msgs.pack(side=LEFT, fill=BOTH, pady=10)


frame.pack()

#creating text field

textF = Entry(main, font=("Verdana",20))
textF.pack(fill=X, pady=10)


btn=Button(main,text="Ask from bot",font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event) :
    btn.invoke()



# going to bind main window with enter key



main.bind('<Return>',enter_function)


main.mainloop()

