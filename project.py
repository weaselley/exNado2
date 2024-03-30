##########################################################################################
# Project) 여러 이미지를 합치는 프로그램.
# 사용자는 합치려는 이미지를 1개 이상 섵내, 합쳐진 이미지가 저장될 경로를 지정.
# 가로 넓이, 간격, 포맷 옵션을 지정, 시작을 통해 이미지를 합친다. 닫기를 통해 프로그램 종료.
# 기능 
# 1. 파일 추가
# 2. 선택 삭제
# 3. 찾아보기
# 4. 가로 넓이 지정 (원본유지, 1024, 800, 640)
# 5. 간격 (없음, 좁게, 보통, 넓게)
# 6. 포맷 (PNG, JPG, BMP)
# 7. 시작
# 8. 진행상황
# 9. 닫기
##############################
import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Merge images")
##############################
## function
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        # initialdir="c:/")
        initialdir=r"D:/Work/python_workspace/bk_examples/userlib_result/")

    for file in files:
        # print(file)
        list_file.insert(END, file)

def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
## reversed 설명
# lst1 = [1, 2, 3, 4, 5]
# print("리스트1 뒤집기 전: ", lst1)
# lst1.reverse()
# print("리스트1 뒤집은 후: ", lst1)
# lst2 = [1, 2, 3, 4, 5]
# print("리스트2 뒤집기 전: ", lst2)
# lst3 = reversed(lst2)
# print("리스트2 뒤집은 후: ", lst2)
# print("리스트3: ", list(lst3))

def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    # if folder_selected is None: # Need debugging
    if folder_selected == "":
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

def merge_image():
    try:
        # # print(list_file.get(0, END))
        # images = [Image.open(x) for x in list_file.get(0, END)]
        # # size[0]: width, size[1]: height
        # # widths = [x.size[0] for x in images]
        # # heights = [x.size[1] for x in images]
        # # print(widths)
        # # print(heights)
        # # print("넓이 : ", widths)
        # # print("높이 : ", heights)
        # widths, heights = zip(*(x.size for x in images))

        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1
        else:
            img_width = int(img_width)

        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        img_format = cmb_format.get().lower()

        images = [Image.open(x) for x in list_file.get(0, END)]
        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]
        widths, heights = zip(*(image_sizes))
        # print(image_sizes)
        # print(widths, heights)
## zip 설명
# kor = ["사과", "바나나", "오렌지"]
# eng = ["apple", "banana", "orange"]
# print(list(zip(kor, eng)))
# mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
# print(list(zip(*mixed)))
# kor2, eng2 = zip(*mixed)
# print(kor2)
# print(eng2)
        
        max_width, total_height = max(widths), sum(heights)
        # print("최대 넓이 : ", max_width)
        # print("총 높이 : ", total_height)

        if img_space > 0:
            total_height += (img_space * (len(images) - 1))
        else:
            pass

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0

        for idx, img in enumerate(images):
            if img_width > -1:
                img = img.resize(image_sizes[idx])
            else:
                pass
            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)
            prog_val = (idx + 1) / len(images) * 100
            p_var.set(prog_val)
            prog_bar.update()

        file_name = "merged." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err:
        msgbox.showerror("에러", err)


def start_conv():
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요.")
        return

    # print("가로 넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    merge_image()



##############################
## 01. file frame
frame_file = Frame(root)
frame_file.pack(fill="x", padx=5, pady=5)

btn_addfile = Button(frame_file, text="파일추가", padx=5, pady=5, width=12, command=add_file)
btn_addfile.pack(side="left")

btn_delfile = Button(frame_file, text="선택삭제", padx=5, pady=5, width=12, command=del_file)
btn_delfile.pack(side="right")

##############################
## 02. list frame
frame_list = Frame(root)
frame_list.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(frame_list, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

##############################
## 03. save path frame
frame_path = LabelFrame(root, text="저장경로")
frame_path.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(frame_path)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(frame_path, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

##############################
## 04. option frame
frame_opt = LabelFrame(root, text="옵션")
frame_opt.pack(padx=5, pady=5, ipady=5)

lbl_width = Label(frame_opt, text="가로 넓이", width=10)
lbl_width.pack(side="left", padx=5, pady=5)
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_opt, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

lbl_space = Label(frame_opt, text="간격", width=10)
lbl_space.pack(side="left", padx=5, pady=5)
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_opt, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left")

lbl_format = Label(frame_opt, text="포맷", width=10)
lbl_format.pack(side="left", padx=5, pady=5)
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_opt, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left")

##############################
## 05. progress bar
frame_prog = LabelFrame(root, text = "진행 상황")
frame_prog.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
prog_bar = ttk.Progressbar(frame_prog, maximum=100, variable=p_var)
prog_bar.pack(fill="x", padx=5, pady=5)

##############################
## 06. run
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start_conv)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False) # x(width), y(height)
root.mainloop()