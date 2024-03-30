from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("제목 없음")
root.geometry("640x480")

def open_file():
    file_selected = filedialog.askopenfilename(title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*,*")))
    

    if os.path.isfile(file_selected):
        root.title(os.path.basename(file_selected) + " - 메모장")
        with open(file_selected, "r", encoding="utf8") as fillfile:
            txt.delete("1.0", END)
            txt.insert(END, fillfile.read())
    else:
        return

def save_file():
    file_selected = filedialog.asksaveasfilename(title="select file", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")), defaultextension=".txt" )
    if file_selected is None:
        return

    root.title(os.path.basename(file_selected) + " - 메모장")
    with open(file_selected, "w", encoding="utf8") as fillfile:
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