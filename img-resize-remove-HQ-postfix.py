#!/usr/bin/env python

import os
import sys


            
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
            p_in = os.path.join(path, "in")
            ffn_in = os.path.join(p_in, infile)                            
        else:
            # double click mode, means convert all files in
            # folder
            outPath =  os.path.dirname(infile)
            ffn_in = infile
      
      
        fn       = os.path.basename(ffn_in) 
        fn_noExt = os.path.splitext(fn)[0]
        ext      = os.path.splitext(fn)[1].lower()  
        
        # get the length of string
        length = len(fn_noExt)
        # Get last character of string i.e. char at index position len -1
        trigger = "-HQ"
        triggerLen = len(trigger)
        lastChars = fn_noExt[-triggerLen:]
        
        if lastChars==trigger:
            # remove "trigger"
            fnn = fn_noExt[0:length-triggerLen]     
            fn_out   = fnn + ext

            #ffn_out = os.path.join(outPath,infile) # same name 
            ffn_out = os.path.join(outPath,fn_out) # new name without (HQ)
            
            
            print("")
            if os.path.isfile(ffn_out):
                print("No Rename - file Exists:")
                print("       : %s" % ffn_out)
            else:
                print("Rename:")
                print("  From : %s" % ffn_in)
                print("  To   : %s" % ffn_out)
                os.rename(ffn_in, ffn_out)                  
            
        else: 
            # do nothing
            pass
        
    
    

    
    print("")    
    print("#")
    print("# Done")
    print("#")
    
    # enable line below for "send to" debugging if needed
    input("Press enter to exit ;)")