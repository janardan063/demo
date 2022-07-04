#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, numpy as np, pandas as pd
import cv2

import os 
import os.path

path1  = r'F:\\check\\board5\\Photos\\'
ok = os.listdir(path1)
okk=sorted(ok)

out = 'F:\\check\\board5\\Cropped\\'
folder_names = []

c=0

path  = r'F:\\check\\board5\\CSV\\'
oo = os.listdir(path)
oo=list(oo)
ooo=sorted(oo)


for h in range(len(ooo)):
    pth=str(path)+str(ooo[h])
    
    df1 = pd.read_csv(pth)

    for k in okk:
        k=k[:-4]
        
        if k == (ooo[h][:-4]):
            for i in range(len(df1)):
                try:
                    a = str(path1) + str(k) + ".jpg"

                    x,y,x_2,y_2 = df1['x0'][i],df1['y0'][i],df1['x1'][i],df1['y1'][i]
                    img = cv2.imread(a)
                    new_img = img[y:y_2,x:x_2]
                    path2 = out+ df1['cls'][i]
                    path2=str(path2)

                    c+=1


                    if not os.path.exists(path2):
                        os.mkdir(path2)
                    os.chdir(path2)

                    cv2.imwrite(path2+"\\"+str(c)+".jpg",new_img)
                    print("Writing Done")
                except Exception as e:
                    print(e)

