from tkinter import Tk, Label

# Create a new window
window = Tk()
window.title('German Words')
window.geometry("600x300")


label = Label(window, text='Welcome', font=('Arial Black', 78, 'bold'), bg='steelblue', fg='white')
label.pack(pady = 100)
window.mainloop()