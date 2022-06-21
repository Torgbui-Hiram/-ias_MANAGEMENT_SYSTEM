from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import sqlite3


# ========= Main Window Contruction =======
window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title('INDUSTRIAL AND ALLIED SERVICES MANAGEMENT SYSTEM')
s_width = 562
s_height = 1000
window.geometry(f"{s_height}x{s_width}+{180}+{100}")
icon = PhotoImage(file="bitmapimage\IAS_LOGO.png")
logo = PhotoImage(file="bitmapimage\IAS_LOGO.png")
background_img = ImageTk.PhotoImage(file="images\RNG Filling Station.jpg")
window.iconphoto(True, icon)
window.state('zoomed')
window.wm_resizable(height=0, width=0)
# ============== Page creatings =============
page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky=NSEW)
# ============== Variabels declarations =====
pas = StringVar()
user = StringVar()
assigned_role = StringVar()
id_prove = StringVar()
id_number = IntVar()
department_of = StringVar()
last_name_search = StringVar()
first_name_search = StringVar()
rm_last_name = StringVar()
rm_first_name = StringVar()
appointment_date = StringVar()
number_on_id = IntVar()
car_reg_number = StringVar()
last_name = StringVar()
first_name = StringVar()
signup_user_name = StringVar()
signup_pas = StringVar()
signup_confirm_pas = StringVar()
unique_id = StringVar()
first_view_entry = StringVar()
last_view_entry = StringVar()
id_type_entry = StringVar()
depatment_entry = StringVar()
car_number_entry = StringVar
date_employed_entry = StringVar
unique_entry = StringVar
role_entry = StringVar()
id_number_entry = StringVar()
# ===============CLAIM REQUEST VARIABLES==========================
request_date = StringVar()
person_request = StringVar()
station_name = StringVar()
work_scope1 = StringVar()
work_scope2 = StringVar()
item = IntVar()
item_quantity = StringVar()
item_name = StringVar()
item_price = IntVar()
total_cost = IntVar()

# ================ Employee Assigned roll=========================
role_designated = ["GENERATOR", "FEUL PUMPS", "FLAG POLE", "CONFORMANCE TEAM",
                   "ELECTRICAL", "CEVIL WORKS", "PIPE WORKS", "AUTOMATION"]
# ================ Depatment of employee===========================
depatment = ["IT", "HUMAN RESOURCE", "MANAGER", "TEAM LEADER", "TECHNICAL ASSISTANT",
             "DEPT. HEAD", "ACCOUNTANCY", "SECURITY", "OPERATIONS", "SALES"]
# ================ Acceptabel identification cards=================
id_types = ["VOTERS ID", "DRIVERS LINSENCE",
            "PASPORT", "SSNIT", "GHANA CARD", "NHIS"]
# =============== Registered users to have granded access==========

# ============Create Database or connect to one if available============
db = sqlite3.connect('informations\staff_register.db')
# Create cursor
cur = db.cursor()
# ============== Creating rows in staff database afer creation================
# cur.execute("""CREATE TABLE staff_information(
# First Name text,
# Last Name text,
# ID Type text,
# ID_Number integer,
# Date Employed text,
# Car Number text,
# Department text,
# Role text
# )""")
# ============= Creating authentication database===================
# cur.execute("""CREATE TABLE User_authentication(
# User Name text,
# Password text
# )""")
# =======================================================================
# ==================Commiting changes made to database ===================
db.commit()
# ===============closing db==================
db.close()


# ============ User Authentication =========
def check_function():
    # signup_btn.place_configure(x=430, y=510, width=100, height=30)
    # coonecting to database
    db = sqlite3.connect('User_verification.db')
    # Create cursor
    cur = db.cursor()
    # Fetching data from database
    cur.execute(
        "SELECT * FROM login WHERE Username=? AND Password=?", (user.get(), pas.get()))
    row = cur.fetchone()
    if row:
        show_frame(page2)
        messagebox.showinfo("ACCESS GRANTED", f"Welcome {user.get()}")
        page2_Next_btn.config(state=ACTIVE)
        login_btn.place_forget()
        db.commit()
        # closing db
        db.close()
    elif user.get() == "" or pas.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=page1)
        username.delete(0, END)
        password.delete(0, END)
        username.insert(0, "username:")
        password.insert(0, "password")
    else:
        messagebox.showerror(
            "Error", "Invalid username or Password", parent=page1)


# ========= Comands Control functions ===========
def add_details():
    # coonecting to database
    conn_db = sqlite3.connect('informations\staff_register.db')
    # Create cursor
    cur = conn_db.cursor()
    # insert data into database
    cur.execute("INSERT INTO staff_information VALUES (:First_name, :Last_name, :prove_id, :id_number, :appointment_date, :department, :assigned_role, :car_reg_number)",
                {
                    'First_name': first_name.get(),
                    'Last_name': last_name.get(),
                    'prove_id': id_prove.get(),
                    'id_number': id_number.get(),
                    'appointment_date': assigned_role.get(),
                    'department': department_of.get(),
                    'assigned_role': appointment_date.get(),
                    'car_reg_number': car_reg_number.get()

                })
    # commit changes
    conn_db.commit()
    # close db
    conn_db.close()
    first_name_enty.delete(0, END)
    last_name_entry.delete(0, END)
    id_prove.set("")
    id_number.delete(0, END)
    department_of.set("")
    assigned_role.set("")
    vehicle_reg.delete(0, END)
    appoitntment_date_entry.delete(0, END)


# =============Show staff records====================
def update_info():
    selected = my_tree.focus()
    my_tree.item(selected, values=(first_view_name_entry.get(), last_view_name_entry.get(),
                                   id_type_view_entry.get(), id_number_view_entry.get(),
                                   car_number_view_entry.get(), date_employed_view_entry.get(),
                                   depatment_view_entry.get(), role_view_entry.get(), unique_address_entry.get()
                                   ))
    first_view_name_entry.delete(0, END)
    last_view_name_entry.delete(0, END)
    id_type_view_entry.delete(0, END)
    depatment_view_entry.delete(0, END)
    car_number_view_entry.delete(0, END)
    date_employed_view_entry.delete(0, END)
    unique_address_entry.delete(0, END)
    role_view_entry.delete(0, END)
    id_number_view_entry.delete(0, END)


def edit_records():
    first_view_name_entry.delete(0, END)
    last_view_name_entry.delete(0, END)
    id_type_view_entry.delete(0, END)
    depatment_view_entry.delete(0, END)
    car_number_view_entry.delete(0, END)
    date_employed_view_entry.delete(0, END)
    unique_address_entry.delete(0, END)
    role_view_entry.delete(0, END)
    id_number_view_entry.delete(0, END)
    selected = my_tree.focus()
    valu_es = my_tree.item(selected, 'values')
    kount = []
    for v_info in valu_es:
        kount.append(v_info)
    # adding the selected info from tree view
    first_view_name_entry.insert(0, kount[0])
    last_view_name_entry.insert(0, kount[1])
    id_type_view_entry.insert(0, kount[2])
    id_number_view_entry.insert(0, kount[3])
    car_number_view_entry.insert(0, kount[4])
    date_employed_view_entry.insert(0, kount[5])
    depatment_view_entry.insert(0, kount[6])
    role_view_entry.insert(0, kount[7])
    unique_address_entry.insert(0, kount[8])


def show_records():
    global count
    # coonecting to database
    conn_db = sqlite3.connect('informations\staff_register.db')
    # Create cursor
    cur = conn_db.cursor()
    # insert data into database
    cur.execute('SELECT *, oid FROM staff_information')
    records = cur.fetchall()
    count = 0
    for record in records:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
        count += 1
    # commit changes
    conn_db.commit()
    # close db
    conn_db.close()


# ===========window frames================
def show_frame(frame):
    frame.tkraise()


def back_frame(frame):
    frame.tkraise()
# ==========window frames================


# ================Adding staff frame==================
def add_staff():
    page2_blue_frame.place_forget()
    page2_remove_frame.place_forget()
    page2_add_frame.place(x=500, y=250, width=400, height=250)


# ================ Deleting record from database=======================
def delete_db_records():
    unique_id.get()
    # coonecting to database
    conn_db = sqlite3.connect('informations\staff_register.db')
    # Create cursor
    cur = conn_db.cursor()
    # insert data into database
    cur.execute("DELETE FROM staff_information WHERE oid= " + unique_id.get())
    # commit changes
    conn_db.commit()
    # close db
    conn_db.close()


# ==========Remove staff details from system======
logo = ImageTk.PhotoImage(file="image\ias.png")
phone_lbl_img = ImageTk.PhotoImage(file="image\icons8-telephone-24.png")


def claim_request():
    page2_add_frame.place_forget()
    page2_blue_frame.place(x=400, y=100, width=610, height=610)
    page2_remove_frame.place(x=5, y=5, width=600, height=600)

    logo_img = Label(page2_remove_frame, bd=0, image=logo)
    logo_img.place(y=0, x=0)
    main_lbl = Label(page2_remove_frame, font=('impact', 19),
                     text=('PAYMENT REQUEST FORM - MAINTENANCE'), background='#544B4E', foreground='white').place(x=165, y=35)
    company_lbl = Label(page2_remove_frame, font=('impact', 19),
                        text=('INDUSTRIAL AND ALLIED SERVICES'), background='#544B4E', foreground='white').place(x=200, y=0)

    seperation = Frame(page2_remove_frame, width=450,
                       height=5, background='#E55247')
    seperation.place(x=160, y=74)
# ===============input and labels==========================
    date_lbl = Label(page2_remove_frame, font=('airial', 12),
                     text=('DATE.'), background='#544B4E', foreground='black').place(x=400, y=105)
    request_date_entry = ttk.Entry(
        page2_remove_frame, textvariable=request_date, font=('Helvetica', 15, 'bold'))
    request_date_entry.place(x=455, y=105, width=140)
    request_date_entry.configure(background='white')

    team_leader_lbl = Label(page2_remove_frame, font=('airial', 12),
                            text=('TEAM LEADER:'), background='#544B4E', foreground='black').place(x=10, y=105)
    team_leader_entry = ttk.Entry(
        page2_remove_frame, textvariable=person_request, font=('Helvetica', 15, 'bold'))
    team_leader_entry.place(x=140, y=105)
    team_leader_entry.configure(background='white')

    preventative_lbl = Label(page2_remove_frame, font=('airial', 12),
                             text=('STATION NAME:'), foreground='black', background='#544B4E').place(x=10, y=200)
    station_name_entry = ttk.Entry(
        page2_remove_frame, textvariable=station_name, font=('Helvetica', 15, 'bold'))
    station_name_entry.place(x=140, y=200)
    preventative_lbl = ttk.Label(page2_remove_frame, font=('airial', 12),
                                 text=('TYPE OF MAINTENANCE ACTIVITY:'), foreground='black', background='#544B4E').place(x=10, y=150)

    corrective_check_box = ttk.Checkbutton(
        page2_remove_frame, variable=1, textvariable=work_scope1, text='CORRECTIVE')
    corrective_check_box.place(x=280, y=150)
    corrective_check_box = ttk.Checkbutton(
        page2_remove_frame, variable=1, textvariable=work_scope2, text='PREVENTATIVE')
    corrective_check_box.place(x=380, y=150)

    item_lbl = Label(page2_remove_frame, font=('airial', 12),
                     text=('ITEM'), foreground='black', background='#544B4E').place(x=10, y=260)
    item_entry = ttk.Entry(
        page2_remove_frame, textvariable=item, font=('Helvetica', 15, 'bold'))
    item_entry.place(x=5, y=290, width=50)
    item_entry.configure(background='white')

    quantity_lbl = Label(page2_remove_frame, font=('airial', 12),
                         text=('QUANTITY'), foreground='black', background='#544B4E').place(x=75, y=260)
    quantity_entry = ttk.Entry(
        page2_remove_frame, textvariable=item_quantity, font=('Helvetica', 15, 'bold'))
    quantity_entry.place(x=60, y=290, width=100)
    quantity_entry.configure(background='white')
    # ========================================================
    descpription_lbl = Label(page2_remove_frame, font=('airial', 12),
                             text=('DESCRIPTION'), foreground='black', background='#544B4E').place(x=190, y=260)
    description_entry = ttk.Entry(
        page2_remove_frame, textvariable=item_name, font=('Helvetica', 15, 'bold'))
    description_entry.place(width=140, x=165, y=290)
    description_entry.configure(background='white')

    unit_cost_lbl = Label(page2_remove_frame, font=('airial', 12),
                          text=('UNIT COST'), foreground='black', background='#544B4E').place(x=340, y=260)
    unit_cost_entry = ttk.Entry(
        page2_remove_frame, textvariable=item_price, font=('Helvetica', 15, 'bold'))
    unit_cost_entry.place(width=140, x=310, y=290)
    unit_cost_entry.configure(background='white')

    total_cost_lbl = Label(page2_remove_frame, font=('airial', 12),
                           text=('TOTAL COST'), foreground='black', background='#544B4E').place(x=480, y=260)
    total_cost_entry = ttk.Entry(
        page2_remove_frame, textvariable=total_cost, font=('Helvetica', 15, 'bold'))
    total_cost_entry.place(width=140, x=455, y=290)
    total_cost_entry.configure(background='white')
    # ================== Reference column ====================
    refrence_no_lbl = Label(page2_remove_frame, font=('airial', 12),
                            text=('Ref No'), foreground='black', background='#544B4E').place(x=20, y=350)
    refrence_no_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    refrence_no_entry.place(width=50, x=85, y=350)

    payment_type_lbl = Label(page2_remove_frame, font=('airial', 12),
                             text=('Payment Type'), foreground='black', background='#544B4E').place(x=145, y=350)
    payment_type_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    payment_type_entry.place(width=100, x=260, y=350)

    payment_ref_lbl = Label(page2_remove_frame, font=('airial', 12),
                            text=('Payment Ref'), foreground='black', background='#544B4E').place(x=370, y=350)
    payment_ref_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    payment_ref_entry.place(width=100, x=475, y=350)
    # ===================== Authorised column =================
    authorised_by_lbl = Label(page2_remove_frame, font=('airial', 12),
                              text=('Authorised by'), foreground='black', background='#544B4E').place(x=25, y=390)
    authorised_by_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    authorised_by_entry.place(width=100, x=135, y=390)

    signature_lbl = Label(page2_remove_frame, font=('airial', 12),
                          text=('Signature'), foreground='black', background='#544B4E').place(x=245, y=390)
    signature_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    signature_entry.place(width=100, x=315, y=390)

    autorised_date_lbl = ttk.Label(page2_remove_frame, font=('airial', 12),
                                   text=('Date'), foreground='black', background='#544B4E').place(x=425, y=390)
    autorised_date_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    autorised_date_entry.place(width=100, x=475, y=390)
    # =================== Approved column=====================
    approved_lbl = ttk.Label(page2_remove_frame, font=('airial', 12),
                             text=('Approved by'), foreground='black', background='#544B4E').place(x=25, y=430)
    approved_lbl_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    approved_lbl_entry.place(width=100, x=135, y=430)

    approval_signature_lbl = ttk.Label(page2_remove_frame, font=('airial', 12),
                                       text=('Signature'), foreground='black', background='#544B4E').place(x=245, y=430)
    approval_signature_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    approval_signature_entry.place(width=100, x=315, y=430)

    approval_date_lbl = ttk.Label(page2_remove_frame, font=('airial', 12),
                                  text=('Date'), foreground='black', background='#544B4E').place(x=425, y=430)
    approval_date_entry = ttk.Entry(
        page2_remove_frame, font=('Helvetica', 15, 'bold'))
    approval_date_entry.place(width=100, x=475, y=430)
    # ================ Buttons For Action=================
    submit_btn = ttk.Button(
        page2_remove_frame, command=result, text='SUBMIT', cursor='hand2')
    submit_btn.place(x=500, y=500)

    extra_btn = ttk.Button(page2_remove_frame, text='EXTRA', cursor='hand2')
    extra_btn.place(x=415, y=500)

    reset_btn = ttk.Button(page2_remove_frame, text='RESET', cursor='hand2')
    reset_btn.place(x=330, y=500)

    cancel_btn = ttk.Button(page2_remove_frame, text='CANCEL', cursor='hand2')
    cancel_btn.place(x=245, y=500)

    # ================= Seperation Frame================

    seperation_below_frame = Frame(
        page2_remove_frame, width=600, height=50, background='white')
    seperation_below_frame.place(x=0, y=550)

    design_by_lbl = ttk.Label(seperation_below_frame, font=('Helvetiac', 12, 'bold'),
                              text=('By: ACTIVE-24/7 LTD.'), foreground='#1A237E', background='white').place(x=10, y=5)

    phone_contact_img = Label(seperation_below_frame,
                              bd=0, image=phone_lbl_img)
    phone_contact_img.place(y=10, x=520)

    by_contact_lbl = ttk.Label(seperation_below_frame, font=('Helvetiac', 10, 'bold'),
                               text=('0548715522'), foreground='#1A237E', background='white').place(x=500, y=30)

# def claim_details():
#     request_date.get()
#     person_request.get()
#     station_name.get()
#     work_scope1.get()
#     work_scope2.get()
#     item.get()
#     item_quantity.get()
#     item_name.get()
#     item_price.get()
#     total_cost.get()


def result():
    claim = []
    info = (
        f"Team leader:{person_request.get()} Claimed:{ total_cost.get()} /n for {work_scope1.get() or work_scope2.get()}")
    claim.append(info)
    print(claim)


# ==========Search for existed staffs============


def search_staff():
    page2_add_frame.place_forget()
    page2_remove_frame.place_forget()
    page2_blue_frame.place_forget()


# =============Abort search for staff============
def search_cancel():
    page2_add_frame.place_forget()
    page2_remove_frame.place_forget()
    page2_blue_frame.place_forget()


# =============== Logout user=====================
def logout():
    resp = messagebox.askquestion("LOGGING OUT OF SYSTEM",
                                  "PRESS YES TO LOGOUT OR NO TO CANCEL")
    if resp == "yes":
        user.set("")
        pas.set("")
        username.delete(0, END)
        password.delete(0, END)
        username.insert(0, "username:")
        password.insert(0, "password")
        show_frame(page1)


# ============= Empty login entry field============
def clear_box(e):
    login_btn.place(x=575, y=400, width=100, height=30)
    signup_btn.place(x=675, y=400, width=100, height=30)
    if username.get() == "username:" or password.get() == "password:":
        username.delete(0, END)
        password.delete(0, END)
        signup_user_entry.delete(0, END)
        password.configure(show="•")


# ===========Abort new user creation=================
def cancel_create_user():
    cancel = messagebox.askokcancel(
        "ARE SURE YOU SURE TO CANCEL", "YES OR NO")
    if cancel == True:
        signup_frame.place_forget()
        page1_login_frame2.place(x=440, y=210)
        page1_login_frame.place(x=430, y=200)
        username.place(x=550, y=290, width=250, height=35)
        password.place(x=550, y=330, width=250, height=35)
    elif cancel == False:
        signup_frame.place(x=300, y=30)
        username.insert(0, "username:")
        password.insert(0, "password:")

    else:
        username.place(x=350, y=250, width=250, height=35)
        password.place(x=350, y=290, width=250, height=35)


# =========== Create new user on signup page=========
def signup_user_info():
    page1_login_frame.place_forget()
    page1_login_frame2.place_forget()
    login_btn.place_forget()
    signup_frame.place(x=500, y=60)
    signup_btn.place_configure(x=430, y=510, width=100, height=30)
    signup_btn.place_forget()
    username.place_forget()
    password.place_forget()


# =========== New staff registration=================
def register():
    login_btn.place_forget()
    # coonecting to database
    db = sqlite3.connect('User_verification.db')
    # Create cursor
    cur = db.cursor()
    # Fetching data from database
    # cur.execute("CREATE TABLE IF NOT EXISTS login(Username TEXT,Password TEXT)")
    if signup_pas.get() != signup_confirm_pas.get():
        messagebox.showerror(
            "Password Error", "Please Enter A Valid Password!")
    elif signup_user_name.get() == "" or len(signup_user_name.get()) <= 3:
        messagebox.showerror("INCORRECT USER NAME", "Please try again!")
    elif signup_confirm_pas.get() == "" or signup_pas.get() == "":
        messagebox.showerror("ALL FIELD REQUIRED",
                             "Please provide all the informations!")
    else:
        cur.execute("INSERT INTO login VALUES (:Username, :Password)",
                    {
                        'Username': signup_user_name.get(),
                        'Password': signup_pas.get(),
                    })
        messagebox.showinfo("REGISTERED!", "Account creating sucessful")
        db.commit()
        # closing db
        db.close()

# ========= Show and Hide Password===========


def showpassword():
    hide_password.place_forget()
    show_password.place(x=350, y=100)
    password.configure(show='')


def hidepassword():
    show_password.place_forget()
    hide_password.place(x=350, y=100)
    password.configure(show='•')
# =============================================


# ============ PAGE1 BACKGROUND IMAGE =========
show_frame(page1)
company_logo = Label(page2, image=logo)
company_logo.place(x=0, y=0)
safty_img = ImageTk.PhotoImage(
    file="images\icons8-security-shield-green-50.png")
blind_eye_img = ImageTk.PhotoImage(
    file="images\closed-eye.png")
open_eye_img = ImageTk.PhotoImage(
    file="images\open-eye.png")

# =============LOGING FRMAE====================
page1_login_frame = Frame(page1, height=250, width=500,
                          border=20, background="black")
page1_login_frame.place(x=430, y=200)
page1_login_frame2 = Frame(
    page1, height=230, width=480, border=20)
page1_login_frame2.place(x=440, y=210)
safety_login_img = Label(page1_login_frame2, image=safty_img)
safety_login_img.place(x=10, y=70)

# ============ page1 New user signup frame =====
signup_frame = ttk.Frame(page1, height=470, width=370,)
# ==============================================
# ============ page1 Labels =====================
signup_bg = ImageTk.PhotoImage(file="images/use_now.jpg")
signup_lbl1 = ttk.Label(signup_frame, image=signup_bg,).place(
    x=100, y=50)
main_signup = ttk.Label(signup_frame, text="CREATE USER ACCOUNT", foreground="red", font=(
    "impact", 28, "bold"),).place(x=10, y=5)
sign_entry_lbl = ttk.Label(signup_frame, image="", text="Name:", font=(
    "Broad way", 15, "bold"),).place(x=60, y=225,)
sign_entry_lbl2 = ttk.Label(signup_frame, image="", text="Password:", font=(
    "Broad way", 15, "bold"),).place(x=60, y=290)
sign_entry_lbl3 = ttk.Label(signup_frame, image="", text="Confirm password:", font=(
    "Broad way", 15, "bold"),).place(x=60, y=355)
page1_login_lbl = ttk.Label(page1_login_frame2, text="Login Here", foreground="blue", font=(
    "Helvetica", 35, "bold"),).place(x=90, y=0)

# =============================================
# ============= Page1 Entry fields ============
username = ttk.Entry(page1, textvariable=user, font=(
    "Gougy old style", 15, "bold"),)
username.place(x=550, y=290, width=250, height=35)
username.insert(0, "username:")
password = ttk.Entry(page1, textvariable=pas, font=(
    "Gougy old style", 15))
password.place(x=550, y=330, width=250, height=35)
password.insert(0, "password:")
# ================================================
# ==================Signup Page Entry field=======
signup_user_entry = ttk.Entry(signup_frame, textvariable=signup_user_name, foreground="#1C247A", font=(
    "airial", 17))
signup_user_entry.place(x=60, y=250, width=250, height=35)
signup_first_pas_entry = ttk.Entry(signup_frame, textvariable=signup_pas, cursor="hand2", foreground="black", font=(
    "airial", 25))
signup_first_pas_entry.configure(show="•")
signup_first_pas_entry.place(x=60, y=315, width=250, height=35)
signup_user_entry.insert(0, "Enter your name")
signup_confirm_pas_entry = ttk.Entry(signup_frame, textvariable=signup_confirm_pas, cursor="hand2", foreground="black", font=(
    "airial", 25))
signup_confirm_pas_entry.place(x=60, y=380, width=250, height=35)
signup_confirm_pas_entry.configure(show="•")
# ================================================
# ===========Button binding to clear box==========
username.bind("<Button-1>", clear_box)
password.bind("<Button-1>", clear_box)

# ================================================
# ================ Page1 Login/Signup Frame Buttons ==================
login_btn = ttk.Button(page1, command=lambda: check_function(
), text="Login", cursor="hand2")
signup_btn = ttk.Button(page1, text="SignUp",
                        command=lambda: signup_user_info(), cursor="hand2")
signup_btn
create_new_user = ttk.Button(signup_frame, command=lambda: cancel_create_user(),  text="CANCEL", cursor="hand2").place(
    x=78, y=430, width=100, height=30)
created_done = ttk.Button(signup_frame, command=lambda: register(),  text="DONE", cursor="hand2").place(
    x=180, y=430, width=100, height=30)
hide_password = Button(
    page1_login_frame2, image=blind_eye_img, bd=0, command=lambda: showpassword(), cursor="hand2")
hide_password.place(x=350, y=100)
show_password = Button(
    page1_login_frame2, image=open_eye_img, bd=0, command=lambda: hidepassword(), cursor="hand2")

# ===============================================
# ================= Page 2 Frames ===============
page2_add_frame = Frame(page2, bg="#544B4E")
page2_blue_frame = Frame(page2, bg="blue")
page2_remove_frame = Frame(page2_blue_frame, bg="#544B4E")
logo_seperation = Frame(page2, width=1250,
                        height=29, background='#E3493D')
logo_seperation.place(x=164, y=52)
# page2_search_frame = Frame(page2, bg="#544B4E")

# ===============Page2 background ===============
# page2_background = Frame(page2, height=700, width=1250)
# page2_background.place(x=0, y=50)
# background_lbl = Label(page2_background, image=background_img)
# background_lbl.place(x=0, y=0)
# ===============================================
# ============ page2 labels =====================
title = Label(page2, fg="white", background='#22254B', text=" INDUSTRIAL AND ALLIED SERVICES MANAGEMENT SYSTEM  ", font=(
    "Helvetica", 30, "bold"),).place(x=164, y=2)
title2 = Label(logo_seperation, fg="white", background='#E3493D', text=" INDUSTRIAL AND ALLIED SERVICES LTD  ", font=(
    "Helvetica", 10, "bold"),).place(x=400, y=2)
p2_vehi_reg_enty_lbl = Label(page2_add_frame, bg="#544B4E", text="First name of employee: ", font=(
    "airial", 10, "bold"), fg="white").place(x=5, y=5)
p2_vehi_reg_enty_lbl2 = Label(page2_add_frame, text="Last name of employee:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=32)
driver_dept_lbl = Label(page2_add_frame, text="Select depatment of employee:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=60)
driver_role_lbl = Label(page2_add_frame, text="Select designation of employee:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=85)
prof_id_lbl = Label(page2_add_frame, text="Select prove of identity type:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=110)
vehicle_details = Label(page2_add_frame, text="Enter vehicle registration:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=191)
identity_numb = Label(page2_add_frame, text="Enter ID number:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=135)
date_appoimtment = Label(page2_add_frame, text="Enter date of appointment:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=163)
fistname_remove = Label(page2_remove_frame, bg="#544B4E", text="First name of employee: ", font=(
    "airial", 10, "bold"), fg="white").place(x=5, y=5)
lastname_remove = Label(page2_remove_frame, text="Last name of employee:", fg="white", bg="#544B4E", font=(
    "airial", 10, "bold")).place(x=5, y=32)

# =============================================
# ============= Page2 Entry frame field =======
first_name_enty = ttk.Entry(page2_add_frame, textvariable=first_name, font=(
    "Gougy old style", 10, "bold"), background="#E7E6E6")
first_name_enty.place(x=180, y=5, width=200, height=25)
last_name_entry = ttk.Entry(page2_add_frame, textvariable=last_name, font=(
    "Gougy old style", 10, "bold"), background="#E7E6E6")
last_name_entry.place(x=180, y=32, width=200, height=25)
vehicle_reg = ttk.Entry(page2_add_frame, textvariable=car_reg_number, font=(
    "Gougy old style", 10, "bold"), background="#E7E6E6")
vehicle_reg.place(x=215, y=191, width=165, height=25)
id_number = ttk.Entry(page2_add_frame, textvariable=number_on_id, font=(
    "Gougy old style", 10, "bold"), background="#E7E6E6")
id_number.place(x=215, y=135, width=165, height=25)
appoitntment_date_entry = ttk.Entry(page2_add_frame, textvariable=appointment_date, font=(
    "Gougy old style", 10, "bold"), background="#E7E6E6")
appoitntment_date_entry.place(x=215, y=165, width=165, height=25)


# =========================================
# ============== page2_combo_box ==========
depatment_combo = ttk.Combobox(page2_add_frame, textvariable=assigned_role, values=role_designated, font=(
    "airial", 10, "bold")).place(x=217, y=60)
designation_combo = ttk.Combobox(page2_add_frame, textvariable=department_of, values=depatment, font=(
    "airial", 10, "bold")).place(x=217, y=85)
prove_of_id = ttk.Combobox(page2_add_frame, textvariable=id_prove, values=id_types, font=(
    "airial", 10, "bold")).place(x=217, y=110)
# ==========================================
# ============== Page2 Button ==============
page2_Next_btn = ttk.Button(
    page2, text='Next', state=DISABLED, command=lambda: show_frame(page3))
page2_Next_btn.place(x=1130, y=550, height=150, width=200)

page2_add_btn = ttk.Button(page2, text='ADD STAFF', cursor="hand2",
                           command=lambda: add_staff())
page2_add_btn.place(x=1130, y=100, height=150, width=200)
page2_remove_btn = ttk.Button(
    page2, command=lambda: claim_request(), text='REQUEST FORM', cursor="hand2",)
page2_remove_btn.place(x=1130, y=250, height=150, width=200)
page2_search_btn = ttk.Button(
    page2, command=lambda: search_staff(), text='VEHICLE & FUEL', cursor="hand2",)
page2_search_btn.place(x=1130, y=400, height=150, width=200)
add_btn = ttk.Button(page2_add_frame, text='ADD DETAILS',
                     command=lambda: add_details(), cursor="hand2",)
add_btn.place(x=280, y=222, height=25, width=110)
clear_btn = ttk.Button(page2_add_frame, text='RESET', cursor="hand2",)
clear_btn.place(x=160, y=222, height=25, width=110)

cancel_btn = ttk.Button(page2, command=lambda: logout(
), text='Logout', cursor="hand2",)
cancel_btn.place(x=20, y=700, height=25, width=110)
# ===========================================
# ============= Page3 Frame =================
data_viewing_frame = Frame(page3,
                           background="white")
data_viewing_frame.pack(pady=40)

# =============== Page3 Label ===============
delete_db_records_lbl = Label(page3, text="Enter the unique id:", fg="black", font=(
    "Helvetica", 10))
delete_db_records_lbl.place(x=1180, y=12)
# ===========================================
# =============== Page3 Button ==============
page3_btn = ttk.Button(page3, text='Back', command=lambda: back_frame(page2))
page3_btn.place(x=20, y=700, height=25, width=100)
viewing_btn = ttk.Button(page3, text='show record',
                         command=lambda: show_records())
viewing_btn.place(x=10, y=10)
viewing_btn2 = ttk.Button(page3, text='Delete Record',
                          command=lambda: delete_db_records())
viewing_btn2.place(x=100, y=10)
tree_view_edit_btn = ttk.Button(page3, text='EDIT INFO', command=edit_records,)
tree_view_edit_btn.place(x=200, y=10)
tree_view_update_btn = ttk.Button(
    page3, text='UPDATE INFO', command=update_info,)
tree_view_update_btn.place(x=290, y=10)
# ================page3 Treeview================
my_tree = ttk.Treeview(data_viewing_frame)
# ==================Page3 Treeview colums assigned=======
my_tree['columns'] = ('First Name', 'Last Name', 'ID TYPE',
                      'ID NUMBER', 'DATE EMPLOYED', 'CAR NUMBER', 'DEPATMENT', 'ROLE', 'oid')
# columns define
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('First Name', anchor=W, width=150)
my_tree.column('Last Name', anchor=W, width=150)
my_tree.column('ID TYPE', anchor=W, width=150)
my_tree.column('ID NUMBER', anchor=CENTER, width=150)
my_tree.column('DATE EMPLOYED', anchor=CENTER, width=150)
my_tree.column('CAR NUMBER', anchor=CENTER, width=150)
my_tree.column('DEPATMENT', anchor=CENTER, width=150)
my_tree.column('ROLE', anchor=W, width=150)
my_tree.column('oid', anchor=CENTER, width=150)

# Treeview Heading
my_tree.heading('#0', text="oid", anchor=W)
my_tree.heading('First Name', text="FIRST NAME", anchor=W)
my_tree.heading('Last Name', text="LAST NAME", anchor=W)
my_tree.heading('ID TYPE', text="ID TYPE", anchor=W)
my_tree.heading('ID NUMBER', text="ID NUMBER", anchor=CENTER)
my_tree.heading('DATE EMPLOYED', text="DEPATMENT", anchor=CENTER)
my_tree.heading('CAR NUMBER', text="ROLE", anchor=CENTER)
my_tree.heading('DEPATMENT', text="DATE EMPLOYED", anchor=CENTER)
my_tree.heading('ROLE', text="CAR NUMBER", anchor=W)
my_tree.heading('oid', text="UNIQ ID", anchor=CENTER)
my_tree.pack()
# ==============Page3 entry box for oid deleting=======
delete_record_lbl_entry = ttk.Entry(page3, textvariable=unique_id, font=(
    "Helvetica", 12))
delete_record_lbl_entry.place(x=1300, y=11, width=50, height=23)
# ========== Edit and view entry box for Treeview============
first_view_name_entry = ttk.Entry(page3, textvariable=first_view_entry, font=(
    "Helvetica", 10))
first_view_name_entry.place(x=5, y=300, width=150, height=25)
first_view_name_lbl = Label(page3, text="FIRST NAME", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=15, y=275)
last_view_name_entry = ttk.Entry(page3, textvariable=last_view_entry, font=(
    "Helvetica", 10))
last_view_name_entry.place(x=160, y=300, width=150, height=25)
last_view_name_lbl = Label(page3, text="LAST NAME", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=170, y=275)
id_type_view_entry = ttk.Entry(page3, textvariable=id_type_entry, font=(
    "Helvetica", 10))
id_type_view_entry.place(x=315, y=300, width=150, height=25)
id_type_view_lbl = Label(page3, text="ID TYPE", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=325, y=275)
id_number_view_entry = ttk.Entry(page3, textvariable=id_number_entry, font=(
    "Helvetica", 10))
id_number_view_entry.place(x=470, y=300, width=150, height=25)
id_number_view_lbl = Label(page3, text="ID #NO", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=510, y=275)
date_employed_view_entry = ttk.Entry(page3, textvariable=date_employed_entry, font=(
    "Helvetica", 10))
date_employed_view_entry.place(x=625, y=300, width=155, height=25)
date_employed_lbl = Label(page3, text="DEPATMENT", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=635, y=275)
car_number_view_entry = ttk.Entry(page3, textvariable=car_number_entry, font=(
    "Helvetica", 10))
car_number_view_entry.place(x=785, y=300, width=150, height=25)
car_number_view_lbl = Label(page3, text="ROLE", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=785, y=275)
depatment_view_entry = ttk.Entry(page3, textvariable=depatment_entry, font=(
    "Helvetica", 10))
depatment_view_entry.place(x=940, y=300, width=150, height=25)
depatment_view_lbl = Label(page3, text="EMPL. DATE", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=950, y=275)
role_view_entry = ttk.Entry(page3, textvariable=role_entry, font=(
    "Helvetica", 10))
role_view_entry.place(x=1095, y=300, width=150, height=25)
role_view_entry_lbl = Label(page3, text="CAR #NO", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=1090, y=275)
unique_address_entry = ttk.Entry(page3, textvariable=unique_entry, font=(
    "Helvetica", 10))
unique_address_entry.place(x=1250, y=300, width=110, height=25)
unique_address_lbl = Label(page3, text="UNIQUE ID", fg="black", font=(
    "Helvetica", 10, 'bold')).place(x=1260, y=275)

window.mainloop()
