# Get data from excel

import pandas as pd
finalData = pd.read_excel("Speeha-Participants-2022.xlsx",sheet_name = 'Details').__array__()
# finalData=df[df['Category']=="Super Senior"]
# print(finalData)

# Create Copies of a image

from PIL import Image

for row in finalData:
    t=row[4] if type(row[4])==str else row[3]
    img=Image.open(row[2]+'.jpg')
    img.save("total-photos/"+row[3]+"/"+row[2]+"/"+row[1].title()+" - "+t.title()+".jpg")


# Iterate through all the images in a folder

import os
from wand.image import Image
from wand.drawing import Drawing

def getYcoordinates(categoryName):
    if(categoryName=="Superman A" or categoryName=="Superman B"):
        return 1380
    else:
        return 1470

def getXcoordinates(categoryName):
    if(categoryName=="Superman A" or categoryName=="Superman B"):
        return 1040
    else:
        return 830

def textMaxLength(categoryName):
    if(categoryName=="Superman A" or categoryName=="Superman B"):
        return 43
    else:
        return 50

folder_dir = 'C:/Users/jhaka/Desktop/total-photos'
for branchName in os.listdir(folder_dir):
    for CategoryName in os.listdir(folder_dir+"/"+branchName):
        for imageName in os.listdir(folder_dir+"/"+branchName+"/"+CategoryName):
            # os.remove("total-photos/"+branchName+"/"+CategoryName+"/"+imageName)

            # Edit image & Insert filename
            myImage = Image(filename ="total-photos/"+branchName+"/"+CategoryName+"/"+imageName)
            draw = Drawing()
            draw.font_size = 70
            draw.font_family="Book Antiqua"
            customXCoordinates=int(((textMaxLength(CategoryName)-len(imageName)-4)/2)*40) # To write the text on center
            draw.text(getXcoordinates(CategoryName)+customXCoordinates,getYcoordinates(CategoryName), imageName[:-4]) # cordinates-(X pos,Y pos)
            draw(myImage)
            myImage.save(filename="total-photos/"+branchName+"/"+CategoryName+"/"+imageName)
