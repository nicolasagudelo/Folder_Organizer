# Author: Nicolas Agudelo

#Importing the libraries we are going to be using.
import os
import shutil
import tkinter as tk
from tkinter import TclError, ttk, filedialog, Tk, HORIZONTAL

# The find dir function will ask the user for the folder he wants to organize. In case he presses 'Cancel' the dirname variable will be empty in this case we ask the user to please select a folder to be able to organize it
def find_dir():
    global description_label
    frm = ttk.Frame(root, padding=10)
    ttk.Label(frm, text="Select the folder that you want to organize")
    dirname = filedialog.askdirectory(parent=root, initialdir='~', title='Select the folder that you want to organize')
    if dirname == '':
        description_label['text'] = 'Please select a folder to continue\n\nJust choose the folder that you want to organize\nby clicking the Start button below'
    else:
        organize(dirname)

# The organize function is the heart of the code here we will examine each file on the selected folder and classify it accordint to its extension.

def organize(directory):
    
    os.chdir(directory)
    
    global description_label
    global progressbar
    # We get the files from the folder selected by the user ignoring folders within that folder.
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # We use the step variable to increase the progress on our progress bar.
    step = 1
    total_files = len(files)

    for file in files:
        step += 1
        # We separate the name of the files from its extension
        name, ext = os.path.splitext(file)
        ext = ext.lower()
        # On each iteration we update our root window to increase the progress bar value.
        root.update_idletasks()
        progressbar['value'] = step * (100/total_files)
        # Using match case to call the move_files function according to the type of file.
        match ext:
            case '.abw'|'.aww'|'.chm'|'.cnt'|'.dbx'|'.djvu'|'.doc'|'.docm'|'.docx'|'.dot'|'.dotm'|'.dotx'|'.epub'|'.gp4'|'.ind'|'.indd'|'.key'|'.keynote'|'.mht'|'.mpp'|'.odf'|'.ods'|'.odt'|'.opx'|'.ott'|'.oxps'|'.pages'|'.pdf'|'.pmd'|'.pot'|'.potx'|'.pps'|'.ppsx'|'.ppt'|'.pptm'|'.pptx'|'.prn'|'.ps'|'.pub'|'.pwi'|'.rtf'|'.sdd'|'.sdw'|'.shs'|'.snp'|'.sxw'|'.tpl'|'.vsd'|'.wpd'|'.wps'|'.wri'|'.xps'|'.numbers'|'.ods'|'.sdc'|'.sxc'|'.xls'|'.xlsm'|'.xlsx':
                move_files(directory, file, '/Documents/')
            case '.3ga'|'.aac'|'.aiff'|'.amr'|'.ape'|'.arf'|'.asf'|'.asx'|'.cda'|'.dvf'|'.flac'|'.gp4'|'.gp5'|'.gpx'|'.logic'|'.m4a'|'.m4b'|'.m4p'|'.midi'|'.mp3'|'.ogg'|'.opus'|'.pcm'|'.rec'|'.snd'|'.sng'|'.uax'|'.wav'|'.wma'|'.wpl'|'.zab':
                move_files(directory, file, '/Audio Files/')
            case '.264'|'.3g2'|'.3gp'|'.ard'|'.asf'|'.asx'|'.avi'|'.bik'|'.dat'|'.dvr'|'.flv'|'.h264'|'.m2t'|'.m2ts'|'.m4v'|'.mkv'|'.mod'|'.mov'|'.mp4'|'.mpeg'|'.mpg'|'.mts'|'.ogv'|'.prproj'|'.rec'|'.rmvb'|'.swf '|'.tod'|'.tp'|'.ts'|'.vob'|'.webm'|'.wlmp'|'.wmv':
                move_files(directory, file, '/Video Files/')
            case '.bmp'|'.cpt'|'.dds'|'.dib'|'.dng'|'.emf'|'.gif'|'.heic'|'.ico'|'.icon'|'.jpeg'|'.jpg'|'.pcx'|'.pic'|'.png'|'.psd'|'.psdx'|'.raw'|'.tga'|'.thm'|'.tif'|'.tiff'|'.wbmp'|'.wdp'|'.webp':
                move_files(directory, file, '/Images/')
            case '.air'|'.app'|'.application'|'.appx'|'.bat'|'.bin'|'.com'|'.cpl'|'.deb'|'.dll'|'.elf'|'.exe'|'.jar'|'.js':
                move_files(directory, file, '/Executable Files/')
            case '.abr'|'.ai'|'.ani'|'.cdt'|'.djvu'|'.eps'|'.fla'|'.icns'|'.ico'|'.icon'|'.mdi'|'.odg'|'.pic'|'.psb'|'.psd'|'.pzl'|'.sup'|'.vsdx'|'.xmp':
                move_files(directory, file, '/Graphic Files/')
            case '.3d'|'.3ds'|'.c4d'|'.dgn'|'.dwfx'|'.dwg'|'.dxf'|'.ipt'|'.lcf'|'.max'|'.obj'|'.pro'|'.skp'|'.stl'|'.u3d'|'.x_t':
                move_files(directory, file, '/3D Graphics/')
            case '.eot'|'.otf'|'.ttc'|'.ttf'|'.woff':
                move_files(directory, file, '/Font Files/')
            case '.1st'|'.alx'|'.application'|'.asp'|'.csv'|'.htm'|'.html'|'.log'|'.lrc'|'.lst'|'.md'|'.nfo'|'.opml'|'.plist'|'.reg'|'.rtf'|'.srt'|'.sub'|'.tbl'|'.text'|'.txt'|'.xml'|'.xmp'|'.xsd'|'.xsl'|'.xslt':
                move_files(directory, file, '/Text Files/')
            case '.001'|'.002'|'.003'|'.004'|'.005'|'.006'|'.007'|'.008'|'.009'|'.010'|'.7z'|'.7z.001'|'.7z.002'|'.7z.003'|'.7z.004'|'.7zip'|'.a00'|'.a01'|'.a02'|'.a03'|'.a04'|'.a05'|'.ace'|'.air'|'.appxbundle'|'.arc'|'.arj'|'.bar'|'.bin'|'.c00'|'.c01'|'.c02'|'.c03'|'.cab'|'.cbr'|'.cbz'|'.cso'|'.deb'|'.dlc'|'.gz'|'.gzip'|'.hqx'|'.inv'|'.isz'|'.jar'|'.msu'|'.nbh'|'.pak'|'.part1.exe'|'.part1.rar'|'.part2.rar'|'.pkg'|'.pkg'|'.r00'|'.r01'|'.r02'|'.r03'|'.r04'|'.r05'|'.r06'|'.r07'|'.r08'|'.r09'|'.r10'|'.rar'|'.rpm'|'.sit'|'.sitd'|'.sitx'|'.tar'|'.tar.gz'|'.tgz'|'.uax'|'.vsix'|'.webarchive'|'.z01'|'.z02'|'.z03'|'.z04'|'.z05'|'.zab'|'.zip'|'.zipx':
                move_files(directory, file, '/Compressed Files/')
            case '.000'|'.ccd'|'.cue'|'.daa'|'.dao'|'.dmg'|'.img'|'.img'|'.iso'|'.mdf'|'.mds'|'.mdx'|'.nrg'|'.tao'|'.tc'|'.toast'|'.uif'|'.vcd':
                move_files(directory, file, '/Disk Images/')
            case '.apk'|'.asec'|'.bbb'|'.crypt'|'.crypt14'|'.ipa'|'.ipd'|'.ipsw'|'.lqm'|'.mdbackup'|'.nbh'|'.nomedia'|'.npf'|'.pkpass'|'.rem'|'.rsc'|'.sbf'|'.sis'|'.sisx'|'.spd'|'.thm'|'.tpk'|'.vcf'|'.xap'|'.xapk':
                move_files(directory, file, '/Mobile Phone Related Files/')
            case '.accdb'|'.accdt'|'.csv'|'.db'|'.dbf'|'.fdb'|'.gdb'|'.idx'|'.mdb'|'.mdf'|'.sdf'|'.sql'|'.sqlite'|'.wdb':
                move_files(directory, file, '/Databases Files/')
            case '':
                pass
            case _:
                move_files(directory, file, '/Others/')
        description_label.config(text = '{step}/{total_files} organized'.format(step = step, total_files = total_files))
    # In case there are no files to be organized within the folder we inform the user.
    if total_files == 0:
        description_label['text'] = 'There are no files on this folder\n\nYou can now close the program\n\nOr\n\nOrganize other folder by clicking the Start button again.'
    # If not we let him know once the folder has been organized.
    else:
        description_label.config(text = 'Folder organized!\n\nYou can now close the program\n\nOr\n\nOrganize other folder by clicking the Start button again.')

# The move_files function will be on charge of moving the files to their respective folder. It will check if the folder already exists if it does it will just move the file if not it will create the folder first and move the file after that.
def move_files(directory, file, path):
    try:
        shutil.move(file, directory + path + '{file}'.format(file = file))
    except FileNotFoundError:
        os.makedirs(directory + path)
        shutil.move(file, directory + path + '{file}'.format(file = file))
    except PermissionError:
        pass


# Creating the main window for the user interface.
root = Tk()
# Replace the default icon
try:
    root.iconbitmap('organizer.ico')
except:
    pass
# Setting up the geometry of the window.
root.geometry('320x195')
# By setting both of these parameters to false the user can not resize the window.
root.resizable(False, False)
# We make sure the program gets the main focus on the user's Desktop.
root.focus()
# Title of the main window
root.title('Organizer.py')

# Creating our start button which will start the program.

startbutton = tk.Button(
    root, 
    text = 'Start', 
    command = find_dir, 
    cursor='hand2',
    )

# A description label to give information to the user about the program status.

description_label = tk.Label(
    root,
    text = 'You can use this program to organize all your different \ntype of files in folders\n\nJust choose the folder that you want to organize\nby clicking the Start button below',
    justify= 'left',
    anchor = 'center'
    )

progressbar = ttk.Progressbar(
    root,
    orient=HORIZONTAL,
    length = 240,
    mode = 'determinate'
    )

#Placing the objects we created for our user interface.
description_label.place(x=4, y= 5)
startbutton.place(x=140, y= 140)
progressbar.pack(side='bottom', pady=5)

root.mainloop()