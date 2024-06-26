#!/usr/bin/env python

import os
import sys

#pip install Pillow
# To update, run: python.exe -m pip install --upgrade pip
from PIL import Image

# in case of SSL-Cetrificates Warnings and Fetch Problems:
# pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org Pillow



#import Image

size = 128, 128

ratio_list = []
# Percent Value of
# original image
#ratio_list.append(80)
#ratio_list.append(60)
ratio_list.append(50)
ratio_list.append(40)
ratio_list.append(20)

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

            #newImg = img.resize((newWidth, newHeight), Image.ANTIALIAS) #  ANTIALIAS is deprecated and will be removed in Pillow 10
            newImg = img.resize((newWidth, newHeight), Image.LANCZOS)
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


    print("This is the name of the script: ", sys.argv[0])
    numArgs=len(sys.argv)
    print("Number of arguments: ", len(sys.argv))
    print("The arguments are: " , str(sys.argv))


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




    print("")
    print("#")
    print("# Done")
    print("#")

    # enable line below for "send to" debugging if needed
    #python 2 line below
    #key = raw_input("Press enter to exit: ")
    #python 3 line below
    key = input("Press enter to exit: ")
    print("ciao")
