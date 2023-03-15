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

