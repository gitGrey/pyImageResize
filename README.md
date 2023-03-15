# pyImageResize
python file to shrink down JPG, PNG, BMP images from digital cameras/smart phones for use in powerpoint, email,  ... . It makes use of python's PIL (Python Image Library)

Under Windows it can be integrated into the "SendTo" menu and files can be send directly 
to the script, which get converted and outputted on the initial file location/directory.

# Usage:

## Linux
put your images into the **'in'** folder and execute the **'img-resize.py'** script <br>
. <br>
. <br>
wait <br>
. <br>
. <br>
=> check the output folder <br>

## Windows
put your images into the **'in'** folder and execute the **'img-resize.py'** script <br>
. <br>
. <br>
wait <br>
. <br>
. <br>
=> check the output folder <br>

or add a link to the *.py-Files into the **'SendTo'  / 'Senden An'** Folder of Windows Context Menu
therefore type: <br>
> Windows-Key + 'R'<br>
> shell:sendto <br>
add now a link / Verknüpfung to your *.py files <br>

with this you can now select a image file in windows explorer and send it directly to the pyImageResize script. 


You can also do 'drag and drop' files in windows to the PY script.
To do so, pls follow: <br>
Drag and drop onto Python script in Windows Explorer <br>
https://stackoverflow.com/questions/142844/drag-and-drop-onto-python-script-in-windows-explorer <br>
<br>
**... stackoverflow citation:**

> Here’s a registry import file that you can use to do this. Copy the following into a .reg file and run it (Make sure that your .py extensions are mapped to Python.File).

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Python.File\shellex\DropHandler]
@="{60254CA5-953B-11CF-8C96-00AA00B8708C}"
```

> This makes Python scripts use the WSH drop handler, which is compatible with long filenames. To use the short filename handler, replace the GUID with **86C86720-42A0-1069-A2E8-08002B30309D**.

# Example Test Run - Terminal Output
```
./img-resize.py 

File Extension : .py
Current script : img-resize
Current script : img-resize.py
Current Path   : /home/gitgrey/Pictures/pyImageResize
Full Name      : /home/gitgrey/Pictures/pyImageResize/img-resize.py

This is the name of the script:  ./img-resize.py
Number of arguments           :  1
The arguments are             :  ['./img-resize.py']
Output Dir (existing): in
Output Dir (existing): out

Search dir     : ./in
Search dir     : /home/gitgrey/Pictures/pyImageResize/in

1 image[s] found 


Resize Ratio      : 80%
Input File        : /home/gitgrey/Pictures/pyImageResize/in/test-img.jpg
File Ext          : .jpg
Cur Size: (w x h) : 3014 x 4367
New Size: (w x h) : 2411 x 3493
Output File       : /home/gitgrey/Pictures/pyImageResize/out/test-img-80.jpg

Resize Ratio      : 60%
Input File        : /home/gitgrey/Pictures/pyImageResize/in/test-img.jpg
File Ext          : .jpg
Cur Size: (w x h) : 3014 x 4367
New Size: (w x h) : 1808 x 2620
Output File       : /home/gitgrey/Pictures/pyImageResize/out/test-img-60.jpg

Resize Ratio      : 50%
Input File        : /home/gitgrey/Pictures/pyImageResize/in/test-img.jpg
File Ext          : .jpg
Cur Size: (w x h) : 3014 x 4367
New Size: (w x h) : 1507 x 2183
Output File       : /home/gitgrey/Pictures/pyImageResize/out/test-img-50.jpg

Resize Ratio      : 40%
Input File        : /home/gitgrey/Pictures/pyImageResize/in/test-img.jpg
File Ext          : .jpg
Cur Size: (w x h) : 3014 x 4367
New Size: (w x h) : 1205 x 1746
Output File       : /home/gitgrey/Pictures/pyImageResize/out/test-img-40.jpg

Resize Ratio      : 20%
Input File        : /home/gitgrey/Pictures/pyImageResize/in/test-img.jpg
File Ext          : .jpg
Cur Size: (w x h) : 3014 x 4367
New Size: (w x h) : 602 x 873
Output File       : /home/gitgrey/Pictures/pyImageResize/out/test-img-20.jpg
move input file to output folder

#
# Done
#
Press enter to exit: 
```
