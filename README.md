# Folder Organizer Using Python and Tkinter.

Hello everyone!

<br>

<figure align = "center">
<img src = https://i.imgur.com/cWxnHRx.gif alt = "Folder Organizer" title = "Folder Organizer">
</figure>
<div align = "center"> <em>Folder Organizer</em> </div>

<br>
<div style="text-align: justify">Here is my approach to an application to organize the files you have on any folder on your computer sorting them according to their extension.</div>
<br>
<div style="text-align: justify">This was also the first time I experimented creating a (super simple) user interface on python instead of having the user doing everything on the terminal. I used the module <code>Tkinter</code> to create this window for the user to interact with.</div>
<br>

- [Folder Organizer Using Python and Tkinter.](#folder-organizer-using-python-and-tkinter)
  - [Creating the User Interface](#creating-the-user-interface)
  - [Pressing the Start Button](#pressing-the-start-button)
  - [The organize() function](#the-organize-function)
  - [Installing the Application](#installing-the-application)
  - [Closing notes](#closing-notes)
<hr>

## Creating the User Interface

<hr>
<br>

The first step was creating the main window. Using the Tkinter module, we can create an object of the class ***tkinter.Tk***. In my case, I called it root as most of the examples I found on using this module.

```python
# Creating the main window for the user interface.
root = Tk()
```

After that, I started personalizing my `root` object or main window. Changing the default icon for a free personalized icon, I found at <a href = https://freeicons.io/ecommerce-back-office-system-icon-set-2/fulfillment-automatic-packing-factory-order-machine-sort-icon-382620> freeicons.io</a> (thanks to Ginkaewicons who created the icon.), setting the window geometry and adding a title to it.

```python
# Replace the default icon
try:
    root.iconbitmap('organizer.ico')
except:
    pass

# Setting up the geometry of the window.
root.geometry('320x195')

# By setting both parameters to false the user can not resize the window.
root.resizable(False, False)

# We make sure the program gets the main focus on the user's Desktop.
root.focus()

# Title of the main window
root.title('Organizer.py')

```

Next, I decided on the widgets I wanted the main window to have.

In my case, I decided to add:
 - A Label that will give information to the user about what the program does, what it is expecting, or when it has finished.
 - A Start Button which will start the primary function of the program.
 - A Progress Bar that gives the user a visual reference that tells him that the program is doing something and when it has finished.

```python
# Creating our start button, which will start the program.

startbutton = tk.Button(
    root,                   # Setting the 'master' window for this widget
    text = 'Start',         # Setting the text to display on this widget
    command = find_dir,     # This will be the function that executes when you press the button.
    cursor='hand2',         # This will change the cursor when the user hovers it over the button.
    )

# A description label to give information to the user about the program status.

description_label = tk.Label(
    root,                   # Setting the 'master' window for this widget
                            # Setting the text to display on this widget
    text = 'You can use this program to organize all your different \ntype of files in folders\n\nJust choose the folder that you want to organize\nby clicking the Start button below',
    justify= 'left'         # With this, every new line will start at the left of the label.
    )

# A progress bar for the user to follow the program's progress.

progressbar = ttk.Progressbar(
    root,                   # Setting the 'master' window for this widget
    orient=HORIZONTAL,      # Setting the progress bar horizontally
    length = 240,           # Setting the lenght of the progress bar in pixels
    mode = 'determinate'    # We know when our program finishes so we use the determinate mode
    )
```

You can find information about all of the attributes of these and more widgets <a href=https://docs.python.org/3/library/tkinter.ttk.html#>here.</a>

Finally, I placed the objects in the main window:
```python
#Placing the objects we created for our user interface.

description_label.place(x=4, y= 5)
startbutton.place(x=140, y= 140)
progressbar.pack(side='bottom', pady=5)
```

Since the user can not resize the window, I placed the label and button at specific positions using the *x* and *y* axes. For the progress bar, I put it at the bottom of the window, adding a 5px padding on top and bottom to avoid having it entirely on the window's border.

After doing this we get our main window:

<p align = "center">
<img src = https://i.imgur.com/4ObDxIj.jpg alt = "Main Window" title = "Main Window">
</p>
<p style = "font-size: small" align = "center"><em>Main Window</em></p>

<hr>

## Pressing the Start Button

<hr>

<br>

<div style="text-align: justify">Now that the main window is done the start button will be the one responsible of doing what the main goal of the program is. Once it is pressed it will call the <code>find_dir()</code> function which will prompt the user about which folder he wants to organize using the <code>filedialog</code> method from the Tkinter module.
</div>
<br>

```python
# The find dir function will ask the user for the folder he wants to organize. 
# In case he presses 'Cancel', the `dirname` variable will be empty
# In this case, we ask the user to please select a folder to be able to organize it
def find_dir():
    global description_label
    frm = ttk.Frame(root, padding=10)
    ttk.Label(frm, text="Select the folder that you want to organize")
    dirname = filedialog.askdirectory(parent=root, initialdir='~', title='Select the folder that you want to organize')
    # If the user closes the file dialog or presses cancel the dirname will be empty in this case, we change the text on the label of the main window and do nothing else.
    if dirname == '':
        description_label['text'] = 'Please select a folder to continue\n\nJust choose the folder that you want to organize\nby clicking the Start button below'
    else:
    # Once we have the directory that the user wants to organize we pass it to the function organize()
        organize(dirname)
```

<p align = "center">
<img width = 600 src = https://i.imgur.com/nR5fova.jpg alt = "Selecting the Folder" title = "Selecting the Folder">
</p>
<p style = "font-size: small" align = "center"><em>Selecting the Folder</em></p>

If the user closes the window asking for the folder or presses 'Cancel' the program will return to the main window and inform him that a folder is needed for the program to work allowing him to press the start button to start the process again.
<p align = "center">
<img src = https://i.imgur.com/njnljvL.jpg alt = "Not Selecting the Folder" title = "Not Selecting the Folder">
</p>
<p style = "font-size: small" align = "center"><em>Message displayed when no folder was selected</em></p>

After that, if the user selected a folder, two things could happen:
1. There are no files on the selected folder, in which case the program will inform the user about it and give him the option to press the start button again if he wants to.
<p align = "center">
<img src = https://i.imgur.com/a0NPJD4.jpg alt = "Folder with no files" title = "Folder with no files">
</p>
<p style = "font-size: small" align = "center"><em>Message displayed when a folder with no files was selected</em></p>

2. There are files on the selected folder in which case the program will call the `organize()` function which will then organize all the files into folders.

<p align = "center">
<img src = https://i.imgur.com/rOnyHII.jpg alt = "Folder Organized Message" title = "Folder Organized Message">
</p>
<p align = "center">
<em>Folder Organized Message</em>
</p>


<hr>

## The organize() function

<hr>

The `organize()` function is in charge of putting every file in the correct folder. To achieve this, I created different categories of files, and using `match case`, I assigned every file to a folder. In case there is an extension that doesn't fall into any of the categories I created, the program will put it into a folder called *Others*

I won't put the portion of the code that does this here because it's a little bit too long, but you can check the code [here](https://github.com/nicolasagudelo/Folder_Organizer) to see the categories I created and what extension falls into each category.

Thanks to [file-extensions.org](https://www.file-extensions.org/), the place from where I got lists of the most common file extensions and got the idea of how to name each category.

<hr>

## Installing the Application

<hr>

You can find the code for the application at [this repository](https://github.com/nicolasagudelo/Folder_Organizer) at GitHub.

You can also download the executable on this [link](https://github.com/nicolasagudelo/Folder_Organizer/releases/download/v1.0/folder_organizer.zip)

<hr>

## Closing notes

<hr>

Feel free to contact me through my email (public on my profile) if you find any issue or problem with the application or if you have any advice about how something might be better implemented. You can also try adding more stuff to the application; I would love to see that.

Thanks.