import pyqrcode
import sys
##import pypng

def makeCode(myString, myName, myScale) :
    big_code = pyqrcode.create(myString)
    big_code.png(myName.replace(" ","").rstrip("\n") + ".png", scale=myScale, module_color=[0, 0, 0, 0], background=[0xff, 0xff, 0xff])
    ##big_code.show()
    

def readText():
    file = open("tarotData.txt")
    data = file.readlines()

    #testing with one example
    # name = data[0]
    # string = data[1]
    # print("Name: " + name)
    # print("String: " + string)

    #makeCode(string, name, 5)

    it= iter(data)
    for x in it:
        name = x
        string = next(it).strip("\n")
        makeCode(string, name, 5)
  