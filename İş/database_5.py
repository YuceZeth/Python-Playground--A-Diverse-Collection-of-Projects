from tkinter import *
from tkinter import ttk
import sqlite3

LARGE_FONT = ('Veranda', 12)
MED_FONT = ('Veranda', 10, 'bold')
SMALL_FONT = ('Helvetica', 9, 'bold')


class CACFP_DB:

  def setup_db(self):
    # Open db
    self.conn = sqlite3.connect('cacfp_test.db')
    # Create a cursor
    self.c = self.conn.cursor()

    # Create the table if it doesn't exist
    try:
      self.c.execute("CREATE TABLE if not exists Staffing(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, lname TEXT NOT NULL, fname TEXT NOT NULL, title TEXT NOT NULL, department TEXT NOT NULL, payType TEXT NOT NULL, start INTEGER NOT NULL, end_dt INTEGER NOT NULL, t_hours INTEGER NOT NULL, perinc REAL NOT NULL, inc_type TEXT NOT NULL, inc_date INTEGER NOT NULL, hrs_month INTEGER NOT NULL, month_yr INTEGER NOT NULL, c_hours REAL NOT NULL, per_c_hours REAL NOT NULL, gross_hrly REAL NOT NULL, gross_hrly_entry REAL NOT NULL, emp_tax REAL NOT NULL, ue_tax REAL NOT NULL, total_tax REAL NOT NULL, cost_per_emp REAL NOT NULL, cost_total TEXT NOT NULL);")

      self.conn.commit()

    except sqlite3.OperationalError:
      print("ERROR: Table not Created")

  def submit_record(self):
    # Insert record into the db
    staff_dtls = [self.lname_entry.get(), self.fname_entry.get(), self.title_entry.get(),
                  self.department_entry.get(), self.payType_entry.get(), self.start_entry.get(),
                  self.end_dt_entry.get(), self.t_hours_entry.get(), self.perinc_entry.get(),
                  self.inc_type.get(), self.inc_date_entry.get(), self.hrs_month_entry.get(),
                  self.month_yr_entry.get(), self.c_hours_entry.get(), self.per_c_hours_entry.get(),
                  self.gross_hrly_entry.get(), self.gross_monthly_entry.get(), self.emp_tax_entry.get(),
                  self.ue_tax_entry.get(), self.total_tax_entry.get()]

    for element in staff_dtls:
      c.excecute("INSERT INTO staffing VALUES (?)", (element))

    self.conn.commit()
    self.c.close()
    self.conn.close()

  def __init__(self, root):

    root.title('CACFP (CACFP_developmant_version.py)')
    root.geometry('1200x600')
    root.state('zoomed')

    mainlabel = ttk.Label(root, text='\nBudget Detail Worksheet', font=LARGE_FONT, justify=CENTER)
    mainlabel.grid(row=0, column=0, columnspan=50, padx=5, sticky=W + E)
    subtext = ttk.Label(root, text='Sponsors and Affiliated Sites')
    subtext.grid(row=1, column=0, padx=5, sticky=W + E)

    filler = ttk.Label(root, text='------')
    filler.grid(row=3, column=0, padx=25)

    # ----- Create Notebook -----#
    nb = ttk.Notebook(root)
    nb.grid(row=3, column=0, columnspan=50, rowspan=49, padx=5, pady=5, sticky='NESW')

    # ----- Notebook Tab1 -----#
    tab1 = ttk.Frame(nb)
    nb.add(tab1, text='Staffing')
    # tab1.grid_columnconfigure(8, minsize=10)

    # ----- Tab1 Headings (row 0) ----- #
    emp_head = ttk.Label(tab1, text='\nEMPLOYEE DETAILS', font=MED_FONT)
    emp_head.grid(row=0, column=0, columnspan=12, sticky=W + E)

    # ---- Frames (boxes) within tab1 ------
    box1 = ttk.Frame(tab1, width=600, height=75, relief='raised', borderwidth='1')
    box1.grid(row=1, column=0, padx=10, pady=20, sticky=W)

    box2 = ttk.Frame(tab1, width=600, height=75, relief='raised', borderwidth='1')
    box2.grid(row=3, column=0, padx=10, pady=20, sticky=W)

    # ---- Box 1 labels and entry boxes -----
    lname = ttk.Label(box1, text='\nLast Name', font=SMALL_FONT, justify=CENTER)
    lname.grid(row=1, column=0, padx=2, pady=5, sticky='W')
    lname_entry_value = StringVar(box1, value="")
    lname_entry = ttk.Entry(box1, textvariable=lname_entry_value)
    lname_entry.grid(row=2, column=0, padx=2, pady=5, sticky=W)

    fname = ttk.Label(box1, text='\nFirst Name', font=SMALL_FONT, justify=CENTER)
    fname.grid(row=1, column=1, padx=2, pady=5, sticky='W')
    fname_entry_value = StringVar(box1, value="")
    fname_entry = ttk.Entry(box1, textvariable=fname_entry_value)
    fname_entry.grid(row=2, column=1, padx=2, pady=5, sticky=W)

    title = ttk.Label(box1, text='\nPosition Title', font=SMALL_FONT, justify=CENTER)
    title.grid(row=1, column=2, padx=2, pady=5, sticky='W')
    title_entry_value = StringVar(box1, value="")
    title_entry = ttk.Entry(box1, textvariable=title_entry_value)
    title_entry.grid(row=2, column=2, padx=2, pady=5, sticky=W)

    department = ttk.Label(box1, width=15, text='\nDeptartment', font=SMALL_FONT, justify=CENTER)
    department.grid(row=1, column=3, padx=2, pady=5, sticky='W')
    department_entry_value = StringVar(box1, value="")
    department_entry = ttk.Entry(box1, textvariable=department_entry_value)
    department_entry.grid(row=2, column=3, padx=2, pady=5, sticky='W')

    payType = ttk.Label(box1, width=15, text='Pay Type\n(Hourly or Monthly)', font=SMALL_FONT, justify=CENTER)
    payType.grid(row=1, column=4, padx=2, pady=5, sticky='W')
    payType_entry_value = StringVar(box1, value="")
    payType_entry = ttk.Entry(box1, textvariable=payType_entry_value)
    payType_entry.grid(row=2, column=4)

    start = ttk.Label(box1, text='\nStart Time', font=SMALL_FONT, justify=CENTER)
    start.grid(row=1, column=5, padx=5, pady=5, sticky='W')
    start_entry_value = StringVar(box1, value="")
    start_entry = ttk.Entry(box1, width=12, textvariable=start_entry_value)
    start_entry.grid(row=2, column=5, padx=2, pady=5, sticky=W)

    end_dt = ttk.Label(box1, text='\nEnd Time', font=SMALL_FONT, justify=CENTER)
    end_dt.grid(row=1, column=6, padx=5, pady=5, sticky='W')
    end_dt_entry_value = StringVar(box1, value="")
    end_dt_entry = ttk.Entry(box1, width=12, textvariable=end_dt_entry_value)
    end_dt_entry.grid(row=2, column=6, padx=2, pady=5, sticky=W)

    t_hours = ttk.Label(box1, text='Total Work\nHours', font=SMALL_FONT, justify=CENTER)
    t_hours.grid(row=1, column=7, padx=5, pady=5, sticky='W')
    t_hours_entry_value = IntVar(box1, value="")
    t_hours_entry = ttk.Entry(box1, width=12, textvariable=t_hours_entry_value)
    t_hours_entry.grid(row=2, column=7, padx=2, pady=5, sticky=W)

    perinc = ttk.Label(box1, width=10, text='Annual %\nIncrease', font=SMALL_FONT, justify=CENTER)
    perinc.grid(row=1, column=8, padx=5, pady=5, sticky='W')
    perinc_entry_value = StringVar(box1, value="")
    perinc_entry = ttk.Entry(box1, width=12, textvariable=perinc_entry_value)
    perinc_entry.grid(row=2, column=8, padx=2, pady=5, sticky=W)

    inc_type = ttk.Label(box1, text='Increase Type\n(Merit or COL)', font=SMALL_FONT, justify=CENTER)
    inc_type.grid(row=1, column=9, padx=2, pady=5, sticky='W')
    inc_type_entry_value = StringVar(box1, value="")
    inc_type_entry = ttk.Entry(box1, width=15, textvariable=inc_type_entry_value)
    inc_type_entry.grid(row=2, column=9)

    inc_date = ttk.Label(box1, text='Increase\nDate', font=SMALL_FONT, justify=CENTER)
    inc_date.grid(row=1, column=10, padx=5, pady=5, sticky='W')
    inc_date_entry_value = StringVar(box1, value="")
    inc_date_entry = ttk.Entry(box1, width=14, textvariable=inc_date_entry_value)
    inc_date_entry.grid(row=2, column=10, padx=2, pady=5, sticky=W)

    # ---- Box 2 labels and entry boxes for tab1 -----
    hrs_month = ttk.Label(box2, text='Total Work\nHrs/Month', font=SMALL_FONT, justify=CENTER)
    hrs_month.grid(row=1, column=0, padx=5, pady=5, sticky='W')
    hrs_month_entry_value = StringVar(box2, value="")
    hrs_month_entry = ttk.Entry(box2, width=12, textvariable=hrs_month_entry_value)
    hrs_month_entry.grid(row=2, column=0, padx=2, pady=5, sticky=W)

    month_yr = ttk.Label(box2, text='Total Work\nMonths/Yr', font=SMALL_FONT, justify=CENTER)
    month_yr.grid(row=1, column=1, padx=5, pady=5, sticky='W')
    month_yr_entry_value = StringVar(box2, value="")
    month_yr_entry = ttk.Entry(box2, width=12, textvariable=month_yr_entry_value)
    month_yr_entry.grid(row=2, column=1, padx=2, pady=5, sticky=W)

    c_hours = ttk.Label(box2, text='Total Hrs Worked\nfor CACFP', font=SMALL_FONT, justify=CENTER)
    c_hours.grid(row=1, column=2, padx=2, pady=5, sticky='W')
    c_hours_entry_value = StringVar(box2, value="")
    c_hours_entry = ttk.Entry(box2, textvariable=c_hours_entry_value)
    c_hours_entry.grid(row=2, column=2, padx=2, pady=5, sticky=W)

    per_c_hours = ttk.Label(box2, text='% Hrs Worked\nfor CACFP', font=SMALL_FONT, justify=CENTER)
    per_c_hours.grid(row=1, column=3, padx=2, pady=5, sticky='W')
    per_c_hours_entry_value = StringVar(box2, value="")
    per_c_hours_entry = ttk.Entry(box2, textvariable=per_c_hours_entry_value)
    per_c_hours_entry.grid(row=2, column=3, padx=2, pady=5, sticky=W)

    gross_hrly = ttk.Label(box2, text='Gross Hourly\n(before deductions)', font=SMALL_FONT, justify=CENTER)
    gross_hrly.grid(row=1, column=4, padx=5, pady=5, sticky='W')
    gross_hrly_entry_value = StringVar(box2, value="")
    gross_hrly_entry = ttk.Entry(box2, textvariable=gross_hrly_entry_value)
    gross_hrly_entry.grid(row=2, column=4, padx=2, pady=5, sticky=W)

    gross_monthly = ttk.Label(box2, text='Gross Monthly\n(before deductions)', font=SMALL_FONT, justify=CENTER)
    gross_monthly.grid(row=1, column=5, padx=5, pady=5, sticky='W')
    gross_monthly_entry_value = StringVar(box2, value="")
    gross_monthly = ttk.Entry(box2, textvariable=gross_monthly_entry_value)
    gross_monthly.grid(row=2, column=5, padx=2, pady=5, sticky=W)

    emp_tax = ttk.Label(box2, text='Employer Tax\nPer Month', font=SMALL_FONT, justify=CENTER)
    emp_tax.grid(row=1, column=6, padx=5, pady=5, sticky='W')
    emp_tax_entry_value = StringVar(box2, value="")
    emp_tax = ttk.Entry(box2, textvariable=emp_tax_entry_value)
    emp_tax.grid(row=2, column=6, padx=2, pady=5, sticky=W)

    ue_tax = ttk.Label(box2, text='Unemployment\nTax Rate/Month', font=SMALL_FONT, justify=CENTER)
    ue_tax.grid(row=1, column=7, padx=5, pady=5, sticky='W')
    ue_tax_entry_value = StringVar(box2, value="")
    ue_tax = ttk.Entry(box2, textvariable=ue_tax_entry_value)
    ue_tax.grid(row=2, column=7, padx=2, pady=5, sticky=W)

    total_tax = ttk.Label(box2, text='Total Tax Paid\nPer Month', font=SMALL_FONT, justify=CENTER)
    total_tax.grid(row=1, column=8, padx=5, pady=5, sticky='W')
    total_tax_entry_value = StringVar(box2, value="")
    total_tax = ttk.Entry(box2, textvariable=total_tax_entry_value)
    total_tax.grid(row=2, column=8, padx=2, pady=5, sticky=W)

    cost_per_emp = ttk.Label(box2, width=13, text='Annual Cost\nto CACFP', font=SMALL_FONT, justify=CENTER)
    cost_per_emp.grid(row=1, column=9)
    cost_per_emp = ttk.Label(box2, width=12, text='$ 00,000.00', relief=SUNKEN, borderwidth=0)
    cost_per_emp.grid(row=2, column=9, padx=2, pady=5, sticky=W)
    cost_per_emp.configure(background='white')

    # ----- Root Command Bar (works with tab1 data)
    cmd_bar = ttk.Frame(root, width=150, height=615, relief='raised', borderwidth='2')
    cmd_bar.grid(row=6, column=100, sticky=NSEW)

    cmd_bar_title = ttk.Label(cmd_bar, text='Command Bar', font=MED_FONT, justify=CENTER)
    cmd_bar_title.grid(row=0, column=0, pady=5, padx=10, sticky=N)
    cmd_bar.grid_propagate(0)

    # ----- Action Buttons -----
    submit_1 = ttk.Button(cmd_bar, text='Submit', command=lambda: self.submit_record())
    submit_1.grid(row=3, column=0, pady=15)

    # # ----- End Tab1 Detail Labels ----- #

    self.setup_db()


root = Tk()
db = CACFP_DB(root)
root.mainloop()