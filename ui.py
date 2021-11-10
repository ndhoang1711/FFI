from os import name
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import pandas as pd
import glob
import process

window = tk.Tk()
window.title("Filter information")
window.geometry("1000x1000")
window.pack_propagate(False)
window.resizable(0, 0)

# Frame for treeview
frame1 = tk.LabelFrame(window, text="output data")
frame1.place(height=500, width=1000)

# Frame for openfile
file_frame = tk.LabelFrame(window, text="Open Dir")
file_frame.place(height=100, width=1000, rely=0.65, relx=0)

# tao button trong file frame
btnBrowse = Button(window, text="Browse", command=lambda: path())
btnBrowse.place(rely=0.72, relx=0.6)

#pathfile = StringVar()
#txt = Entry(window, width=50, text=pathfile)
#txt.grid(column=0, row=2)
#pathfile.set("browse your path!")

# tao run button trong file frame
btnRun = Button(window, text="Run and Export", command=lambda: process_data())
btnRun.place(rely=0.72, relx=0.3)

# tao run button trong clear
btnRun = Button(window, text="Clear", command=lambda: clear())
btnRun.place(rely=0.72, relx=0.45)

# khởi tạo đường dẫn người dùng đã chọn
label_file = ttk.Label(file_frame, text="No directory selected")
label_file.place(rely=0, relx=0)

export_noti = ttk.Label(file_frame, text="")
export_noti.place(rely=0.2, relx=0)
# tao box de in ra ket qua

# Frame for choose data wanna filter
choose_frame = tk.LabelFrame(window, text="Choose your data you wanna filter")
choose_frame.place(height=150, width=1000, rely=0.45, relx=0)

# tạo checkbox tuy chon data cho người dùng filter trong choose frame
# Checkbox device name
var_name = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Device name",
                         variable=var_name, onvalue=1, offvalue=0)
cb_name.place(rely=0.1, relx=0)

# Checkbox Serial number
var_serial = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Serial Number",
                         variable=var_serial, onvalue=1, offvalue=0)
cb_name.place(rely=0.1, relx=0.1)

# Check box LAN interface
var_lan = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Lan Interface",
                         variable=var_lan, onvalue=1, offvalue=0)
cb_name.place(rely=0.1, relx=0.2)

# Check box WAN interface
var_wan = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Wan Interface",
                         variable=var_wan, onvalue=1, offvalue=0)
cb_name.place(rely=0.1, relx=0.3)

# Check box CROSS interface
var_cross = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Cross Interface",
                         variable=var_cross, onvalue=1, offvalue=0)
cb_name.place(rely=0.1, relx=0.4)

# Check box Model
var_model = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Device model",
                         variable=var_model, onvalue=1, offvalue=0)
cb_name.place(rely=0.3, relx=0)

#check box lan 2

var_lan2 = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Interfaces Lan 2",
                         variable=var_lan2, onvalue=1, offvalue=0)
cb_name.place(rely=0.3, relx=0.1)

var_type = tk.IntVar()
cb_name = tk.Checkbutton(choose_frame, text="Type of Router",
                         variable=var_type, onvalue=1, offvalue=0)
cb_name.place(rely=0.3, relx=0.2)

# tao treeview hiển thị thông tin sau khi xử lý
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="top", fill="x")
treescrolly.pack(side="right", fill="y")
# treescrollx.place(x=0, y=420 )
# treescrolly.place(x=0, y=0)

def clear():
    tv1.delete(*tv1.get_children())

def path():
    filepath = filedialog.askdirectory()    
    label_file["text"] = filepath
# print(pathfile)


def fileProcess():
    try:
        files = glob.glob(label_file["text"] + '\\*.txt')
        file_big = label_file["text"] + '/bigfile.txt'
        with open(file_big, 'wb') as fnew:
            for f in files:
                with open(f, 'rb') as fold:
                    for line in fold:
                        fnew.write(line)
                        fnew.write("\n".encode(encoding='utf_8'))
        f = open(label_file["text"] + '/bigfile.txt', 'r')
        big_file = f.read().split("Processing")

    # print(big_file)
        
        return big_file
    except ValueError:
        tk.messagebox.showerror(
            "information", f"Please choose your Directory first")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror(
            "information", f"Please choose your Directory first")
        return None

#LANI = []

def process_data():
    clear()
    # khoi tao agrs interfaces de truyen vao cac ham duoc goi tai vai.py
    #interfaces.clear()
    interfaces = fileProcess()

    # khoi tao cac bien va goi lai cac gia tri tu vai.py
    CROSSI = process.CROSS_INT(interfaces, var_cross.get())
    NAME = process.DEVICE_NAME(interfaces, var_name.get())
    LANI = process.LAN_INT(interfaces, var_lan.get())
    #LAN2 = process.LAN_INT2(interfaces, var_lan2.get())
    MD = process.MODEL_DEVICE(interfaces,var_model.get())
    SN = process.SERIAL_DEVICE(interfaces, var_serial.get())
    WANI = process.WAN_INT(interfaces, var_wan.get())
    TYPE = process.TYPE_ROUTER(interfaces, var_type.get())


    #####Tao bien luu heading#########

    # if var_model.get() == 1:
    #     tk.messagebox.showinfo("information", f"box check")
    # tao bang dataframe
    data = {'DEVICE NAME' : NAME,
            "WAN INTERFACE": WANI,
            "LAN INTERFACE": LANI,
            "CROSS INTERFACE": CROSSI,
            "SERIAL NUMBER": SN,
            "DEVICE MODEL": MD,
            "TYPE OF ROUTER": TYPE}
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.transpose()
    file_path = label_file["text"]
    df.to_excel(file_path + '\output.xlsx')
    try:
        excel_filename = r"{}".format(file_path)
        dataf = pd.read_excel(excel_filename + '\output.xlsx')
        noti = "We are also exported Excel file to you with named ''output'' at"
        export_noti["text"] = noti + " " + file_path
    except ValueError:
        tk.messagebox.showerror("information", f"can't get your data! sorry")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror(
            "information", f"Please choose your Directory first")
        return None
    except PermissionError:
        tk.messagebox.showerror(
            "information", f"Please close your xlsx file first!")

    tv1["column"] = list(dataf.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    dataf_row = dataf.to_numpy().tolist()
    for row in dataf_row:
        tv1.insert("", "end", values=row)

    #tv1.insert(END, df)
    #return None
    # print(df)
    # print(interfaces)


mainloop()
