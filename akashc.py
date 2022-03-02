def main_screen():
  from tkinter import ttk

  global screen
  screen = tk()

  screen.geometry("500x500")
  screen.title("4rManager")

  Label(text="Login/Register", font=("Calibri", 13)).pack()
  ttk.Label(text="").pack()
  ttk.Button(text="Login").pack()
  ttk.Label(text="").pack()
  ttk.Button(text="Register").pack()

  screen.mainloop()

main_screen()