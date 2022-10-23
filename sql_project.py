from tkinter import *
import tkinter.font as font
import mysql.connector as connector

gui = Tk()
gui.configure(background="light blue")
gui.title("Simple Calculator")
gui.geometry("304x470")


def clearr():
    expression_field.delete(0, END)


def equalpress():
    global result
    result = expression_field.get()
    global x
    x = eval(result)
    clearr()
    expression_field.insert("end", x)


def Make_connection():
    global con
    con = connector.connect(host="localhost", port='3306',user="root", password="darshan123")
    print('Connection Made')


def use_database(name):
    query = "USE " + str(name)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    print("We are using", name, "database")


def ans_up():
    try:
        query = 'insert into calss(cal_ans,exp) values({},"{}")'.format(x, result)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
    except NameError:
        pass


def main():
    Make_connection()
    value = input("enter the database name :")
    use_database(value)
    ans_up()


expression_field = Entry(gui, highlightthickness=1, width=6, font='Arial 24', justify="right")
expression_field.config(highlightbackground="black", highlightcolor="black")
expression_field.grid(columnspan=4, ipadx=89, pady=8)
buttonFont = font.Font(size=9, weight='bold')
button1 = Button(gui, text=' 1 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "1"), height=4, width=8)
button1.grid(row=2, column=0, padx=5, pady=5)
button2 = Button(gui, text=' 2 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "2"), height=4, width=8)
button2.grid(row=2, column=1, padx=5, pady=5)
button3 = Button(gui, text=' 3 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "3"), height=4, width=8)
button3.grid(row=2, column=2, padx=5, pady=5)
button4 = Button(gui, text=' 4 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "4"), height=4, width=8)
button4.grid(row=3, column=0, padx=5, pady=5)
button5 = Button(gui, text=' 5 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "5"), height=4, width=8)
button5.grid(row=3, column=1, padx=5, pady=5)
button6 = Button(gui, text=' 6 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "6"), height=4, width=8)
button6.grid(row=3, column=2, padx=5, pady=5)
button7 = Button(gui, text=' 7 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "7"), height=4, width=8)
button7.grid(row=4, column=0, padx=5, pady=5)
button8 = Button(gui, text=' 8 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "8"), height=4, width=8)
button8.grid(row=4, column=1, padx=5, pady=5)
button9 = Button(gui, text=' 9 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "9"), height=4, width=8)
button9.grid(row=4, column=2, padx=5, pady=5)
button0 = Button(gui, text=' 0 ', font=buttonFont, fg='white', bg='black',
                 command=lambda: expression_field.insert("end", "0"), height=4, width=8)
button0.grid(row=5, column=0, padx=5, pady=5)
plus = Button(gui, text=' ADD\n+', font=buttonFont, fg='black', bg='orange',
              command=lambda: expression_field.insert("end", "+"), height=4, width=8)
plus.grid(row=2, column=3, padx=5, pady=5)
minus = Button(gui, text=' SUB\n- ', font=buttonFont, fg='black', bg='orange',
               command=lambda: expression_field.insert("end", "-"), height=4, width=8)
minus.grid(row=3, column=3, padx=5, pady=5)
multiply = Button(gui, text=' MULTI\n* ', font=buttonFont, fg='black', bg='orange',
                  command=lambda: expression_field.insert("end", "*"), height=4, width=8)
multiply.grid(row=4, column=3, padx=5, pady=5)
divide = Button(gui, text=' DIVIDE\n/ ', font=buttonFont, fg='black', bg='orange',
                command=lambda: expression_field.insert("end", "/"), height=4, width=8)
divide.grid(row=5, column=3, padx=5, pady=5)
equal = Button(gui, text=' EQUALS\n=', font=buttonFont, fg='black', bg='orange',
               command=equalpress, height=4, width=8)
equal.grid(row=5, column=2, padx=5, pady=5)
clear = Button(gui, text='Clear\nX', font=buttonFont, fg='black', bg='orange',
               command=clearr, height=4, width=8)
clear.grid(row=5, column=1, padx=5, pady=5)
Decimal = Button(gui, text='DECIMAL\n.', font=buttonFont, fg='black', bg='orange',
                 command=lambda: expression_field.insert("end", "."), height=4, width=8)
Decimal.grid(row=6, column=0, padx=5, pady=5)
gui.mainloop()

if __name__ == '__main__':
    main()
