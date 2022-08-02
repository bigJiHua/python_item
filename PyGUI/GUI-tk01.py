# 使用tkinter
# import tkinter
# tkinter._test() 测试模板
import tkinter as tk


def say_hello():
    print("hello World!")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hello World!")
    window.geometry("500x250")
    button_hello = tk.Button(window, text="Hello WOrld!\n(click me)", command=say_hello)
    button_quit = tk.Button(window, text='QUIT', fg="red", command=window.destroy)
    button_hello.pack(side="top")
    button_quit.pack(side='bottom')
    window.mainloop()
