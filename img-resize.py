#!/usr/bin/env python3

import os
import sys

#pip install Pillow
# To update, run: python.exe -m pip install --upgrade pip
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#import Image

#debug prints
deb = 1

size = 128, 128

ratio_list = []
# Percent Value of
# original image
ratio_list.append(80)
ratio_list.append(60)
ratio_list.append(50)
ratio_list.append(40)
ratio_list.append(20)

global colorBackground
colorBackground = (73, 109, 137)
colorBackground = "black"

global colorOutline
colorOutline  = (73, 109, 137)
colorOutline  = (0xe4, 0x83, 0x15)
#colorOutline = "lime"


global lp_image_name
lp_image_name = "test-img.png"

def create_dir(d):
    #d = os.path.dirname(f)
    if not os.path.exists(d):
       os.makedirs(d)

       print("")
       create_test_image(d)

       if deb:
           print("Output Dir (created): " + d)
    else:
        if deb:
            print("Output Dir (existing): " + d)

def create_test_image(directory):
    width = 3000
    height= 4000
    print('create image with width x height: %d x %d' % (width, height))

    # with Backgroundcolor
    img = Image.new('RGB', (width, height), colorBackground)

    # Transparent Background
    # (alpha = transparency = last parameter of the color attribute)
    transp = (0, 0, 0, 0)
    #print(transp[3])
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    d = ImageDraw.Draw(img)
    loc=(0,0)
    text="1234567890"
    colorText = (99, 88, 77)

    fontComic = "comic.ttf"
    fontArial = "arial.ttf"
    fontname = fontComic
    #fontname = fontArial
    fontsize=500
    #thefont = ImageFont.truetype(fontname, fontsize)
    thefont = ImageFont.load_default()
    #size2 = d.textsize(text,font=font)
    #print('size width x height: %d x %d' % (size2[0], size2[1]))
    d.text(loc, text, fill=colorText, font=thefont)

    d.rectangle((0, 0, width-2, height-1), outline=colorOutline)
    d.rectangle((1, 1, width-3, height-2), outline=colorOutline)
    d.rectangle((2, 2, width-4, height-3), outline=colorOutline)
    # net line switches off the pixels
    #d.rectangle((width-1, 0, width-1, height-1), outline="black")
    d.rectangle((width-1, 0, width-1, height-1), outline=transp)

    x=10
    y=10
    pixels    = img.load()
    col = pixels[x, y]
    print("Color @ %d %d = %d %d %d" % (x, y, col[0], col[1], col[2]))

    # lp = light painting

    ffn_out = os.path.join(directory, lp_image_name)
    img.save(ffn_out)

def resize(fn, outPath, ratio):

    print("Resize Ratio      : %s%%" % ratio)

    print("Input File        : %s" % fn)

    (filename, file_extension) = os.path.splitext(infile)

    fn_out = filename + "-" + str(ratio)

    print("File Ext          : %s" % file_extension)

    if fn != fn_out:
        #try:

            img = Image.open(fn)


            s = img.size
            print("Cur Size: (w x h) : %d x %d" % (s[0], s[1]))

            ratio = float(ratio) / float(100)

            newWidth = int(  float(s[0])*float(ratio) )
            newHeight = int( float(s[1])*float(ratio) )
            print("New Size: (w x h) : %d x %d" % (newWidth, newHeight))

            newImg = img.resize((newWidth, newHeight), Image.ANTIALIAS)
            #thumbImg = im.thumbnail(size, Image.ANTIALIAS)

            imgType=""

            if file_extension.upper() == ".PNG":
                fn_out = fn_out + ".png"
                imgType="PNG"

            elif file_extension.upper() == ".JPG":
                fn_out = fn_out + ".jpg"
                imgType="JPEG"

            elif file_extension.upper() == ".BMP":
                fn_out = fn_out + ".bmp"
                imgType="BMP"

            else:
                print("")
                print("File Format Not Supported")


            ffn_out = os.path.join(outPath, fn_out)
            print("Output File       : %s" % ffn_out)
            newImg.save(ffn_out, imgType)

# *******************************************************
# *******************************************************
# Program starts here
# *******************************************************
# *******************************************************

if __name__ == '__main__':

    fn       = os.path.basename(__file__) # name des scripts holen
    fn_noExt = os.path.splitext(fn)[0]
    ext      = os.path.splitext(fn)[1]

    fullName = os.path.realpath(__file__)
    path = os.path.dirname(fullName)    # path where this script runs

    print("")
    print("File Extension : %s" % ext)
    print("Current script : %s" % fn_noExt)
    print("Current script : %s" % fn)
    print("Current Path   : %s" % path)
    print("Full Name      : %s" % fullName)

    print("")
    print("This is the name of the script: ", sys.argv[0])
    numArgs=len(sys.argv)
    print("Number of arguments           : ", len(sys.argv))
    print("The arguments are             : " , str(sys.argv))

    p = 'in'
    create_dir(p)

    p = 'out'
    create_dir(p)

    myImages = [] # list of image filenames

    if numArgs==1:
        # no arguments attached we run in
        # folder mode

        #https://stackoverflow.com/questions/142844/drag-and-drop-onto-python-script-in-windows-explorer

        searchDir = "./in" # current dir
        #searchDir = "./lp-images"
        #searchDir="/home/pi/lp/lp-images"
        print("")
        print("Search dir     : %s" % searchDir)
        print("Search dir     : %s" % os.path.realpath(searchDir))

        dirFiles = os.listdir(searchDir) # list of directory files
        #print(dirFiles)
        dirFiles.sort()  # good initial sort but doesnt sort numerically very well

        sorted(dirFiles, reverse=False) # sort numerically in ascending order

        isImage=0

        # below iterates through all entries in a folder
        # it returns file and folder names
        i=0
        for theFile in dirFiles:

            # here we have folders and files
            i+=1

            ffn = os.path.join(searchDir, theFile)
            #print("%s --> %s" % (i, theFile))
            #print("%s --> %s" % (i, ffn))
            #name, ext = os.path.splitext('file.txt')

            if os.path.isdir(ffn):
                # folder / directory
                pass
                #print("Directory found : %s" % theFile)

            if os.path.isfile(ffn):
                #print("File found : %s" % theFile)
                #print("Full Name  : %s" % os.path.dirname(theFile))
                #os.path.join(path, file)):

                isImage=0

                if '.jpg' in theFile.lower():
                    isImage=1

                if '.png' in theFile.lower():
                    isImage=1

                if isImage==1:
                    myImages.append(theFile)

        print("")
        print("%s image[s] found " % len(myImages))
        print("")

        #myimages.sort(reverse=True)
        myImages.sort(key=str.lower)

        if len(myImages)==0:
            # if we have no file in the "in"/"input" Folder
            # we take arguments.
            # in windows we can drag a file and
            # drop it on the *.py file to convert it
            myImages = sys.argv[1:]
            print(myImages)


        #name = input("What is your name? ")




    else:

        myImages = sys.argv[1:]
        print(myImages)


    for infile in myImages:

        if numArgs==1:
            # command line mode
            # or via "right click -> send to"
            outPath = os.path.join(path, "out")
        else:
            # double click mode, means convert all files in
            # folder
            outPath =  os.path.dirname(infile)

        for i in range(len(ratio_list)):
            print("")
            ratio = ratio_list[i]

            if numArgs==1:
                p_in = os.path.join(path, "in")
                ffn_in = os.path.join(p_in, infile)
            else:
                ffn_in = infile

            resize(ffn_in, outPath, ratio)

        print("")
        if numArgs==1:
            print("move input file to output folder")
        else:
            print("input file renamed.")

        fn       = os.path.basename(infile)
        fn_noExt = os.path.splitext(fn)[0]
        ext      = os.path.splitext(fn)[1].lower()
        fn_out   = fn_noExt + "-HQ" + ext
        #ffn_out = os.path.join(outPath,infile) # same name
        ffn_out = os.path.join(outPath,fn_out) # new name (HQ= High Quality)
        os.rename(ffn_in, ffn_out)

        print("inputfile  : %s" % infile)
        print("from here  : %s" % p_in)
        print("moved to   : %s" % outPath)
        print("and renamed: %s" % fn_out)


    print("")
    print("#")
    print("# Done")
    print("#")

    # enable line below for "send to" debugging if needed
    #python 2 line below
    #key = raw_input("Press enter to exit: ")
    #python 3 line below
    #key = input("Press enter to exit: ")

    try: input = raw_input
    except NameError: pass
    key = input("Press enter to exit: ")


    print("ciao")
