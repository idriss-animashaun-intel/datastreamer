import os
import urllib.request
import zipfile
import shutil
import time
from subprocess import Popen


datastream_plotter_master_directory = os.getcwd()
datastream_plotter_directory = os.path.join(datastream_plotter_master_directory, "datastream-plotter-updates")
datastream_plotter_file = os.path.join(datastream_plotter_directory, "main", "main.exe")

def installation():
    print("*** Downloading new version ***")
    urllib.request.urlretrieve("https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/archive/updates/datastream-plotter-updates.zip", datastream_plotter_master_directory+"\\datastream_plotter_new.zip")
    print("*** Extracting new version ***")
    zip_ref = zipfile.ZipFile(datastream_plotter_master_directory+"\datastream_plotter_new.zip", 'r')
    zip_ref.extractall(datastream_plotter_master_directory)
    zip_ref.close()
    os.remove(datastream_plotter_master_directory+"\datastream_plotter_new.zip")
    time.sleep(5)
    
def upgrade():    
    print("*** Removing old files ***")
    shutil.rmtree(datastream_plotter_directory)
    time.sleep(10)
    installation()


def main(autoinstall=0):
    ### Is datastream_plotter already installed? If yes get file size to compare for upgrade
    if os.path.isfile(datastream_plotter_file):
        local_file_size = int(os.path.getsize(datastream_plotter_file))
        # print(local_file_size)
        ### Check if update needed:
        f = urllib.request.urlopen("https://gitlab.devtools.intel.com/ianimash/datastream-plotter/raw/updates/main/main.exe") # points to the exe file for size
        i = f.info()
        web_file_size = int(i["Content-Length"])
        # print(web_file_size)
        if local_file_size != web_file_size:# upgrade available
            if autoinstall:
                print("*** New upgrade available! Upgrading now *** ")
                upgrade()
            else:
                updt = input("*** New upgrade available! enter <y> to upgrade now, other key to skip upgrade *** ")
                if updt == "y": # proceed to upgrade
                    upgrade()
    ### datastream_plotter wasn't installed, so we download and install it here                
    else:
        if autoinstall:
            print("*** Installing DataStream_Plotter for the first time ***")
            installation()
        else:
            install = input("Welcome to datastream_plotter! If you enter <y> datastream_plotter will be downloaded in the same folder where this file is.\nAfter the installation, this same file you are running now (\"datastream_plotter.exe\") will the one to use to open datastream_plotter :)\nEnter any other key to skip the download\n -->")
            if install == "y":
                installation()
    print('Ready')
    ### We open the real application:
    try:
        Popen(datastream_plotter_file)
        print("*** Opening Datastream Plotter ***")
        if not autoinstall:
            time.sleep(20)
    except:
        print('Failed to open application, Please open manually in subfolder')
        pass

def main_with_autoinstall():
    main(autoinstall=1)

if __name__ == "__main__":
    main()
