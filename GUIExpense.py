from tkinter import *
# from tkinter.ttk import Notebook
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# EpochConverter

root = Tk()
root.title("Expense By @IS")
# root.geometry("600x800+3100+0") # 450
# root.geometry("600x800+500+0") # 450
root.geometry("900x800+500+0") # 450

################ Menu Bar ################
menu_bar = Menu(root)
root.config(menu=menu_bar) # familiar .pack()

# Menu file
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Import CSV")

# Help
def About():
    messagebox.showinfo("About","สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูลรายจ่าย\nสนในบริจาคให้เราไหม ขอ 1 บิทคอยก็พอ")

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About", command=About)

# Donate
donate_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Donate",menu=donate_menu)



##########################################


def Save(event=None):
    
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()
    # price = int(price)
    # quantity = int(quantity)
    
    if quantity == '':
        quantity = 1
    elif expense == '' or price == '':
        messagebox.showwarning("Error", "กรุณากรอกข้อมูลให้ครบ (รายการและราคาต่อชิ้น)")
        return
    try :
        dt_d = datetime.now().strftime("%m-%d-%Y")
        dt_t = datetime.now().strftime("%H:%M:%S")
        # dt = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        stamp_ID = datetime.now().strftime("%Y%m%d%H%M%f")
        total_price = int(price) * int(quantity)
        text = f"วันที่ {dt_d} เวลา: {dt_t} \nรายการ: {expense} ราคาต่อชิ้น: {price} บาท จำนวน: {quantity} ชิ้น \nราคารวม: {total_price} บาท\n" 
        v_result.set(text)
        with open("data.csv", 'a', encoding='utf-8', newline='') as f:
            fw = csv.writer(f)
            data = [dt_d, dt_t, stamp_ID, expense, price, quantity, total_price]
        
            fw.writerow(data)

        # update treeview 
        update_table()
        # ex_tv.insert('',0, values=data)

        E1.focus()

        v_show.set(read_data_to_label())
    except Exception as e :
        print(e)
        messagebox.showerror("Error", "กรุณากรอกตัวเลขใหม่ คุณกรอกตัวเลขผิด")
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')
        # messagebox.showwarning("Error", "กรุณากรอกตัวเลขใหม่ คุณกรอกตัวเลขผิด")
        # messagebox.showinfo("Error", "กรุณากรอกตัวเลขใหม่ คุณกรอกตัวเลขผิด")

    
    
    # text_p2 = v_show.get() # ดึงเอา v_show มาเพิ่มตัวที่อัพใหม่
    # text_p2 += text
    # v_show.set(text_p2)
    
    
    # print(f"วันที่ {dt_d} เวลา: {dt_t}  รายการ: {expense} ราคา/ชิ้น: {price} บาท ราคารวม: {total_price} บาท ")

    # Save Data to csv
    
    

    # Claer Value
    v_expense.set('')
    v_price.set('')
    v_quantity.set('')


############# READ data.CSV FUNCTION #############
############# READ data.CSV FUNCTION #############
def read_data_to_label():

    with open("data.csv", encoding="utf-8") as f:
        csv_reader = csv.reader(f, delimiter=',')
        csv_reader = list(csv_reader)
        text = ''
        # dt = datetime.now().strftime("%m-%d-%Y")
        init_date = -6 # Select 6 expense
        try:    
            initial_day = csv_reader[init_date][0]
            text += f"วันที่{csv_reader[init_date][0]}\n"
            for row in csv_reader[init_date::1]:
                # print(csv_reader[init_date][0], row[0])
                if(csv_reader[init_date][0] != row[0]):
                    
                    text += f"\nวันที่ {row[0]} \n"
                    init_date = row[0]
            ##text = '' 
            #print(f"เวลา {row[0]} รายการ {row[1]} ราคาต่อชิ้น {row[2]} จำนวน {row[3]} ราคารวม {row[4]}")
                text += f"เวลา: {row[1]} รายการ: {row[3]} ราคาต่อชิ้น: {row[3]} บาท จำนวน: {row[4]} ชิ้น ราคารวม: {row[5]} บาท\n"
        except :
            init_date = 0
            text += f"วันที่{csv_reader[init_date][0]}\n"
            for row in csv_reader: # Take it All
                # print(csv_reader[init_date][0], row[0])
                if(csv_reader[init_date][0] != row[0]):
                    text += f"\nวันที่ {row[0]} \n"
                    init_date = row[0]
            ##text = '' 
            #print(f"เวลา {row[0]} รายการ {row[1]} ราคาต่อชิ้น {row[2]} จำนวน {row[3]} ราคารวม {row[4]}")
                text += f"เวลา: {row[1]} รายการ: {row[3]} ราคาต่อชิ้น: {row[3]} บาท จำนวน: {row[4]} ชิ้น ราคารวม: {row[5]} บาท\n"
        # print(text)
        # if text == '':
        #     text += "ยังไม่มีรายการในขณะนี้"
        return text

def read_csv():
    with open("data.csv", encoding="utf-8") as f:
        csv_reader = csv.reader(f, delimiter=',')
        csv_reader = list(csv_reader)
        # for row in csv_reader[::-1]:
        #     to_tv.append(row)
        # return to_tv
    return csv_reader 
            
################ Update Record #####################

alltransaction = dict()

def update_table(): # in treeview
    ex_tv.delete(*ex_tv.get_children())
    # for e in ex_tv.get_children():
    #     ex_tv.delete(e)
    try:
        data = read_csv()
        # print(data)
        for e in data:
            # ex_tv.insert('', 'end', values=e)
            # creat transaction data
            alltransaction[e[2]] = e # e[2] = transationID
            ex_tv.insert('', 0, values=e) # Insert to index 0 or Top

        # print(alltransaction)
    except:
        # print("No File")
        pass



#--------------------------------------------------#

################# DELETE ##########################
def UpdateCSV():
    with open("data.csv",'w',encoding="utf-8",newline='') as f:
        csv_writer = csv.writer(f)
        for d in alltransaction:
            csv_writer.writerow(alltransaction[d])
        # Write all alltransaction
        # data = list(alltransaction.values()) # prepare list of data
        # csv_writer.writerows(data) # write many line from nasted list
    update_table()


def DeleteRecord(event=None):
    check = messagebox.askyesno("Confirm?","Do you want to delete this expense")
    # print(check)
    if(check == False): # if press No don't remove this expense
        return

    # print(alltransaction)
    # print("Delete")
    select = ex_tv.selection()
    # print(select)
    data = ex_tv.item(select)
    data = data['values']
    # print(data)
    transaction_id = data[2]
    # print(type(transaction_id))
    # print(chr(transaction_id))
    del alltransaction[f'{transaction_id}']
    UpdateCSV()
    
    



#-------------------------------------------------#

################ press Enter to Save ###############
root.bind("<Return>",Save)
root.bind("<Delete>",DeleteRecord)

# Built Tab
tab = ttk.Notebook(root)
T1 = Frame(tab)
T2 = Frame(tab)
T3 = Frame(tab)
# tab.pack(fill=BOTH, expand=1)

icon_t1 = PhotoImage(file="t1_expense.png")
icon_t2 = PhotoImage(file="t2_expenselist.png")
icon_t3 = PhotoImage(file="t3_tv.png")
icon_b1 = PhotoImage(file="t1_save.png")



tab.add(T1, text=f"{'Add Expense': ^30}", image=icon_t1, compound='top') # T1 T2 is Frame
tab.add(T2, text=f"{'Expense List': ^30}", image=icon_t2, compound='top') 
tab.add(T3, text=f"{'Treeview': ^30}", image=icon_t3, compound='top') 


f1 = Frame(T1)
f1.pack(fill=BOTH)

f2 = Frame(T2)
f2.pack(fill=BOTH)

f3 = Frame(T3)
f3.pack(fill=BOTH)


# Page 1 ---------------------------------------------------
Psedu_lb = ttk.Label(f1)
Psedu_lb.pack()

main_icon = PhotoImage(file="icon_coin.png")
l_img1 = ttk.Label(f1, image=main_icon)
l_img1.pack(pady=10)

l1 = ttk.Label(f1, text="รายการค่าใช้จ่าย", font=(None, 20))
l1.pack(pady=8)
v_expense = StringVar()
E1 = ttk.Entry(f1, textvariable=v_expense, font=(None, 16))
E1.pack(pady=8)

l2 = ttk.Label(f1, text="ราคาต่อชิ้น(บาท)", font=(None, 20))
l2.pack(pady=8)
v_price = StringVar()
E2 = ttk.Entry(f1, textvariable=v_price, font=(None, 16))
E2.pack(pady=8)

l3 = ttk.Label(f1, text="จำนวน(ชิ้น)", font=(None, 20))
l3.pack(pady=8)
v_quantity = StringVar()
E3 = ttk.Entry(f1, textvariable=v_quantity, font=(None, 16))
E3.pack(pady=8) # 
l3_1 = ttk.Label(f1, text=" <Default = 1>", font=(None, 8))
l3_1.pack()

B1 = ttk.Button(f1, text=f"{'Save': >15}", image=icon_b1, compound="left", command=Save)
B1.pack(ipadx=30, ipady=20, pady=10)
#-----------------------------------------------------------

# Page 2 ---------------------------------------------------
show_today = ttk.Label(f2, text="\nประวัติการใช้จ่าย\n", font=(None,16), foreground="green") # Normal Label fg = "green"
show_today.pack()

v_show = StringVar()
try:
    v_show.set(read_data_to_label())
except:
    # print("No File")
    pass
# v_result.set("----------ผลลัพธ์----------")
show = ttk.Label(f2, textvariable=v_show, font=(None,14)) # Normal Label fg = "green"
show.pack()

# ----------------------------------------------------------

# Page 3 ---------------------------------------------------
# header = ["date", "time", "expense", "price_piece", "quantity", "total"]
# header_text = ['วันที่', 'เวลา', 'รายการ', 'ราค่าต่อหน่วย', 'จำนวน', 'ราคารวม'] 
header = ["date", "time", "ID", "expense", "price_piece", "quantity", "total"]
header_text = ['วันที่', 'เวลา', 'ID', 'รายการ', 'ราค่าต่อหน่วย', 'จำนวน', 'ราคารวม'] 
ex_tv = ttk.Treeview(f3, columns=header, show='headings',height=25) # unit of height is number of line
ex_tv.pack()
# for hd in header:
#     	ex_tv.heading(hd,text=hd)
for hd, hd_t in zip(header, header_text):
	ex_tv.heading(hd,text=hd_t)

headerwidth = [80,80,160,180,80,80,80] # width of header

for hd,W in zip(header,headerwidth):
	ex_tv.column(hd,width=W)

update_table()

# for e in (read_csv()[::-1]): #enumerate 
#     ex_tv.insert('', END, values=e)

B_Delete = ttk.Button(T3, text="Delete", command=DeleteRecord)
B_Delete.place(x=80,y=550)

# ----------------------------------------------------------
v_result = StringVar()
v_result.set("\n\n----------Developed By Isoon----------")
result = ttk.Label(f1, textvariable=v_result, font=(None,16), foreground="green") # Normal Label fg = "green"
result.pack(pady=8)

tab.pack(fill=BOTH, expand=1)
# n.pack()
# root.bind("Tab", lambda x: E2.focus())

root.mainloop()
