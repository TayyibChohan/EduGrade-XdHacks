from tkinter import *
from tkinter.ttk import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("HackathonProject-TeacherOutput").sheet1

# Extract and print all of the values

questions = sheet.row_values(1)
while "" in questions:
    questions.remove("")

num = []
print(questions)
window = Tk()

window.title("EduGrade")

window.geometry('350x200')

stnumtxt = Label(window, text="Enter Student Number", font=("Arial Bold", 20))

stnumtxt.grid(column=7, row=0)

stu_num = Entry(window, width=20)
stu_num.grid(column=7, row=2)

def login():
    num.append(stu_num.get())
    window.destroy()



log = Button(window, text="Sumbit", command=login)
log.grid(column=8, row=10)

window.mainloop()

student_num = num[0]
#################################################
for i in range(1, len(questions)):

    window = Tk()

    window.title("EduGrade")

    window.geometry('350x200')
    print(i)

    ques = Label(window, text=questions[i], font=("Arial Bold", 20))

    ques.grid(column=7, row=0)

    txt = Combobox(window, width=20)
    txt.grid(column=7, row=2)
    txt['values'] = ("A", "B", "C", "D", "E", "Text")

    ans = Label(window, text="answer:", font=("Arial", 10))
    ans.grid(column=1, row=2)

    dif = Label(window, text="difficulty:", font=("Arial", 10))
    dif.grid(column=1, row=5)

    combo = Combobox(window)
    combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    combo.current(0)
    combo.grid(column=7, row=5)


    def sumbitted():
        sheet.update_cell(student_num, ((2*(i-1)) + 4), txt.get())
        sheet.update_cell(student_num, ((2 * (i-1)) + 5), combo.get())
        window.destroy()
        return


    sumb = Button(window, text="Sumbit", command=sumbitted)
    sumb.grid(column=8, row=10)

    window.mainloop()