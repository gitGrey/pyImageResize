#!/usr/bin/env python

import os
import sys

#pip install Pillow
# To update, run: python.exe -m pip install --upgrade pip
from PIL import Image

# in case of SSL-Cetrificates Warnings and Fetch Problems:
# pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org Pillow

from enum import Enum

#import Image

class runMode(Enum):
    toWEBP = 1
    toPNG = 2
    toJPG = 3

#
# define your conversion mode here
#
mode = runMode.toWEBP
mode = runMode.toPNG
mode = runMode.toJPG



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

    print("Name of the script  : ", sys.argv[0])
    numArgs=len(sys.argv)
    print("Number of arguments : ", len(sys.argv))
    print("The arguments are   : ", str(sys.argv))

    myImages = [] # list of image filenames

    print("")
    print("Work/run Mode : ", mode.name)


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

                if '.jpeg' in theFile.lower():
                    isImage=1

                if '.png' in theFile.lower():
                    isImage=1

                if '.webp' in theFile.lower():
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

        # we run in drag and drop mode / send to mode / command line mode
        myImages = sys.argv[1:]
        print("Will work on the following images")
        print(myImages)

    i=0
    for infile in myImages:

        if numArgs==1:
            # command line mode
            # or via "right click -> send to"
            outPath = os.path.join(path, "out")
        else:
            # double click mode, means convert all files in
            # folder
            outPath =  os.path.dirname(infile)


        if numArgs==1:
            p_in = os.path.join(path, "in")
            ffn_in = os.path.join(p_in, infile)
        else:
            ffn_in = infile

        fn       = os.path.basename(infile)
        fn_noExt = os.path.splitext(fn)[0]
        ext      = os.path.splitext(fn)[1].lower()

        # file format for PIL export
        fmt =""
        err = False

        if mode == runMode.toJPG and ext == ".jpg":
            err = True

        if mode == runMode.toPNG and ext == ".png":
            err = True

        if mode == runMode.toWEBP and ext == ".webp":
            err = True

        i+=1
        print("")
        print("Convert " + str(i) + " / " + str(len(myImages)))

        if err:
            print("Nothing to do, input and output format are same type: " + ext )
            print("---> " + fn)
            print("---> " + ffn_in)
            continue

        if mode == runMode.toJPG:
            ext = ".jpg"
            fmt = "jpeg"

        if mode == runMode.toPNG:
            ext = ".png"
            fmt = "png"

        if mode == runMode.toWEBP:
            ext = ".webp"
            fmt = "webp"

        fn_out   = fn_noExt + ext
        #ffn_out = os.path.join(outPath,infile) # same name
        ffn_out = os.path.join(outPath,fn_out) # new name (HQ= High Quality)

        print("From : " + infile)
        print("From : " + ffn_in)
        im = Image.open(ffn_in).convert("RGB")
        im.save(ffn_out, fmt)
        print("To   : " + fn_out)
        print("To   : " + ffn_out)



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
