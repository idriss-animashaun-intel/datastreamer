from tkinter import Tk
from tkinter import Button
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import sys

current_directory = os.getcwd()

dir = os.path.join("outputs")
if not os.path.exists(dir):
    os.mkdir(dir)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
   



def get_summary():
    folder = folder_path

    params = []

    dstream_dir = os.listdir(folder_path)
    for file in dstream_dir:
                if file == 'Trigger.csv':
                    print("skip Trigger.csv")
                else:
                    params.append(file)

    user_script = "outputs\DataStreamPlot.jrp"
    jsl_path = resource_path("DataStreamPlot.jsl")
    reading_file = open(jsl_path, "r", encoding="utf-8-sig")

    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace('contact', 'Contact idriss.animashaun@intel.com ...The Matrix Has You Now')
        new_file_content += new_line +"\n"
    reading_file.close()
    writing_file = open(user_script, "w", encoding="utf-8-sig")
    writing_file.write(new_file_content)
    writing_file.close()

    dt_list = ""
    for i in range(0, len(params)):
        if params[i]== 'TDAU_CH_CCF.csv':
            dt_list += 'dt' + str(i) + '=Open("' + folder + '\\' + params[i] + '"); :"Temperature (°C)" << Set Name( "' + params[i].strip('.csv') + ' Temperature (°C)" ); '
        elif params[i]== 'TDAU_CH_SA.csv':
            dt_list += 'dt' + str(i) + '=Open("' + folder + '\\' + params[i] + '"); :"Temperature (°C)" << Set Name( "' + params[i].strip('.csv') + ' Temperature (°C)" ); '
        elif params[i]== 'TestInstance.csv':
            dt_list += 'dt' + str(i) + '=Open("' + folder + '\\' + params[i] + '"); For Each Row(:"Time Index (ms)" = :"Time Index (ms)" + 310);'
        else:
            dt_list += 'dt' + str(i) + '=Open("' + folder + '\\' + params[i] + '"); :"Voltage (V)" << Set Name( "' + params[i].strip('.csv') + ' Voltage (V)" ); :"Current (A)" << Set Name( "' + params[i].strip('.csv') + ' Current (A)" ); :"Resistance (Ω)" << Set Name( "' + params[i].strip('.csv') + ' Resistance (Ω)" ); :"Power (W)" << Set Name( "' + params[i].strip('.csv') + ' Power (W)" ); '

    reading_file = open(user_script, "r", encoding="utf-8-sig")

    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace('//all_datatables', dt_list)
        new_file_content += new_line +"\n"
    reading_file.close()
    writing_file = open(user_script, "w", encoding="utf-8-sig")
    writing_file.write(new_file_content)
    writing_file.close()


    ### join tables
    if len(params) > 2:
        reading_file = open(user_script, "r", encoding="utf-8-sig")

        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = stripped_line.replace('//first_param', 'dt' + str(len(params)) + '=dt0 << Join(	Output Table Name("dummy"),	With( dt1 ),	Merge Same Name Columns, By Matching Columns( :"Time Index (ms)" = :"Time Index (ms)"),	Drop multiples( 0, 0 ),	Include Nonmatches( 1, 1 ),	Preserve main table order( 1 ));')
            new_file_content += new_line +"\n"
        reading_file.close()
        writing_file = open(user_script, "w", encoding="utf-8-sig")
        writing_file.write(new_file_content)
        writing_file.close()


        mid_params_list = ""
        for i in range(2, len(params) - 1):
            mid_params_list +='dt' + str(len(params) + i - 1) + '=dt' + str(len(params) + i - 2) + '<< Join(	Output Table Name("dummy"),	With( dt' + str(i) + ' ),	Merge Same Name Columns, By Matching Columns( :"Time Index (ms)" = :"Time Index (ms)"),	Drop multiples( 0, 0 ),	Include Nonmatches( 1, 1 ),	Preserve main table order( 1 ));  '
            dt_count =  len(params) + i - 1
            dt_last = len(params) + i - 2
        reading_file = open(user_script, "r", encoding="utf-8-sig")

        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = stripped_line.replace('//mid_params', mid_params_list)
            new_file_content += new_line +"\n"
        reading_file.close()
        writing_file = open(user_script, "w", encoding="utf-8-sig")
        writing_file.write(new_file_content)
        writing_file.close()
    
        reading_file = open(user_script, "r", encoding="utf-8-sig")

        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = stripped_line.replace('//last_param', 'dt' + str(dt_count + 1) + '=dt' + str(dt_last + 1) + ' << Join(	Output Table Name("Datastream"),	With( dt' + str(len(params) - 1) + ' ),	Merge Same Name Columns, By Matching Columns( :"Time Index (ms)" = :"Time Index (ms)"),	Drop multiples( 0, 0 ),	Include Nonmatches( 1, 1 ),	Preserve main table order( 1 ));')
            new_file_content += new_line +"\n"
        reading_file.close()
        writing_file = open(user_script, "w", encoding="utf-8-sig")
        writing_file.write(new_file_content)
        writing_file.close()
    else:
        dt_count = 2
        reading_file = open(user_script, "r", encoding="utf-8-sig")

        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = stripped_line.replace('//first_param', 'dt' + str(len(params) + 1) + '=dt0 << Join(	Output Table Name("Datastream"),	With( dt1 ),	Merge Same Name Columns, By Matching Columns( :"Time Index (ms)" = :"Time Index (ms)"),	Drop multiples( 0, 0 ),	Include Nonmatches( 1, 1 ),	Preserve main table order( 1 ));')
            new_file_content += new_line +"\n"
        reading_file.close()
        writing_file = open(user_script, "w", encoding="utf-8-sig")
        writing_file.write(new_file_content)
        writing_file.close()

    # final table    
    reading_file = open(user_script, "r", encoding="utf-8-sig")

    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace('//dt_last', 'dt' + str(dt_count + 1))
        new_file_content += new_line +"\n"
    reading_file.close()
    writing_file = open(user_script, "w", encoding="utf-8-sig")
    writing_file.write(new_file_content)
    writing_file.close()
    
    # close tables
    close_dt = ""
    for i in range(0,dt_count + 1):
        close_dt += 'Close( dt' + str(i) + ', "No Save"); '


    reading_file = open(user_script, "r", encoding="utf-8-sig")

    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace('//delete_tables', close_dt)
        new_file_content += new_line +"\n"
    reading_file.close()
    writing_file = open(user_script, "w", encoding="utf-8-sig")
    writing_file.write(new_file_content)
    writing_file.close()

    os.system(user_script)

    


def select_file():
    global folder_path

    folder_path = fd.askdirectory(
        title='Select DataStream Folder',
        initialdir='/')

    showinfo(
        title='Selected Folder',
        message=folder_path
    )


### Main Root
root = Tk()
root.title('DataStreamer v1.01')


mainframe = ttk.Frame(root, padding="60 50 60 50")
mainframe.grid(column=0, row=0, sticky=('news'))
mainframe.columnconfigure(0, weight=3)
mainframe.rowconfigure(0, weight=3)


open_button = Button(
    mainframe,
    text='Select DataStream Folder',
    command=select_file,
    bg = 'blue', fg = 'white', font = '-family "SF Espresso Shack" -size 12'
)

open_button.grid(row = 0, column = 0)




button_0 = Button(mainframe, text="Plot DataStream", height = 1, width = 20, command = get_summary, bg = 'green', fg = 'white', font = '-family "SF Espresso Shack" -size 12')
button_0.grid(row = 1, column = 0, rowspan = 2 )

### Main loop
root.mainloop()