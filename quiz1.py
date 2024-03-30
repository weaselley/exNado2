from tkinter import *
import os

root = Tk()
root.title("제목 없음")
root.geometry("640x480")

def open_file():
    file_path_temp = file_path + "/mynote.txt"

    if os.path.isfile(file_path_temp):
        print("open file: ", file_path_temp)
        with open(file_path_temp, "r", encoding="utf8") as fillfile:
            txt.delete("1.0", END)
            txt.insert(END, fillfile.read())
    else:
        print("Cannot open file.")

def save_file():
    file_path_temp = file_path + "/mynote.txt"
    print("save file: ", file_path_temp)

    with open(file_path_temp, "w", encoding="utf8") as fillfile:
        fillfile.write(txt.get("1.0", END))
        

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_result'

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", side="left", expand=True)

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()