import tkinter

import PIL as pil
import PIL.Image
import PIL.ImageTk
import PIL.ExifTags as TAGS
import pandas

from tkinter import *

from PIL import ImageTk

df = pandas.DataFrame()
df['Name'] = ""
df['Class'] = ""
df['Format'] = ""
df['Width'] = ""
df['Height'] = ""
df['Mode'] = ""
df['Palette'] = ""


# Кратеры

def images_to_df(min_n, max_n, img_pass, cluster, dataframe):
    for i in range(min_n, max_n):
        name = str(i) + '.jpg'
        image = PIL.Image.open(img_pass + "\\" + name)
        s = pandas.Series(
            [image.filename, cluster, image.format, str(image.width), str(image.height), image.mode, image.palette],
            index=["Name", "Class", "Format", "Width", "Height", "Mode", "Palette"])
        dataframe = pandas.concat([dataframe, s.to_frame().T], ignore_index=True)
    return dataframe


# Кратеры
df = images_to_df(1, 87, "D:\\PictuersShov\\ConcaveRootSurface", "ConcaveRootSurface", df)

# Прожог
df = images_to_df(1, 87, "D:\\PictuersShov\\IncompletePenetration", "IncompletePenetration", df)

# Трещина
df = images_to_df(1, 89, "D:\\PictuersShov\\Crack", "Crack", df)

# Порезы
df = images_to_df(1, 86, "D:\\PictuersShov\\InternalProtrusion", "InternalProtrusion", df)

# Свищи
df = images_to_df(1, 89, "D:\\PictuersShov\\LackofFusion", "LackofFusion", df)
# df = pandas.concat([df, temp_df], ignore_index=True)

# Наплыв
df = images_to_df(1, 84, "D:\\PictuersShov\\NondefectiveImage", "NondefectiveImage", df)

# Несплавления
df = images_to_df(1, 89, "D:\\PictuersShov\\SlagInclusions", "SlagInclusions", df)

# Шлак
df = images_to_df(1, 88, "D:\\PictuersShov\\SurfaceFinish", "SurfaceFinish", df)

# Подрез
df = images_to_df(1, 90, "D:\\PictuersShov\\Other", "Other", df)

df = df.drop("Name", axis=1)
print(df.head())
dups = df.pivot_table(columns=["Class"], aggfunc='size')
print(dups.keys()[0] + "    " + str(dups[0]))

root = Tk()
root.geometry('1000x1000+0+0')
canvas = Canvas(root, width=600, height=600)

def image_resize(path):
    img = PIL.Image.open(path + "\\" + "1.jpg")
    img = img.resize((50, 50), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img


img0 = image_resize("D:\\PictuersShov\\ConcaveRootSurface")
img1 = image_resize("D:\\PictuersShov\\Crack")
img2 = image_resize("D:\\PictuersShov\\IncompletePenetration")
img3 = image_resize("D:\\PictuersShov\\InternalProtrusion")
img4 = image_resize("D:\\PictuersShov\\LackofFusion")
img5 = image_resize("D:\\PictuersShov\\NondefectiveImage")
img6 = image_resize("D:\\PictuersShov\\Other")
img7 = image_resize("D:\\PictuersShov\\SlagInclusions")
img8 = image_resize("D:\\PictuersShov\\SurfaceFinish")


txt = Text(width=80, height=100)
txt.tag_configure("center", justify='right')

txt.insert("1.0", dups.keys()[8] + "    " + str(dups[8]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[7] + "    " + str(dups[7]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[6] + "    " + str(dups[6]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[5] + "    " + str(dups[5]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[4] + "    " + str(dups[4]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[3] + "    " + str(dups[3]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[2] + "    " + str(dups[2]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[1] + "    " + str(dups[1]))
txt.insert("1.0", '\n' * 4)
txt.insert("1.0", dups.keys()[0] + "    " + str(dups[0]))
txt.insert("1.0", '\n' * 9)
txt.insert("1.0", df.head())
txt.tag_add("center", 1.0, "end")
txt.pack(side=LEFT)
canvas.pack(side=RIGHT)
canvas.create_image(1, 8, anchor=NW, image=img0)
canvas.create_image(1, 75, anchor=NW, image=img1)
canvas.create_image(1, 140, anchor=NW, image=img2)
canvas.create_image(1, 204, anchor=NW, image=img3)
canvas.create_image(1, 270, anchor=NW, image=img4)
canvas.create_image(1, 335, anchor=NW, image=img5)
canvas.create_image(1, 400, anchor=NW, image=img6)
canvas.create_image(1, 460, anchor=NW, image=img7)
canvas.create_image(1, 525, anchor=NW, image=img8)
root.mainloop()
