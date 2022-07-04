#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, numpy as np, pandas as pd
import cv2

import os 
import os.path

path  = r'C:\Users\Janardan Pandey\Downloads\data_22_6_22\for_negative_data'
oo = os.listdir(path)

out = 'C:\\Users\\Janardan Pandey\\Downloads\\data_22_6_22\\empty\\'
folder_names = []
for k in oo:
    folder_names.append(str(oo)+'\\'+k)
folder_names


df1 = pd.read_csv('F://work_damage_1.csv')


for k in oo:
    for i in range(len(df1)):
        for j in range(0,5):
            try:
                a = str(path) + "\\cell_" + str(int(df1['cell_number'][i])) + "_z_" + str(df1['z_axis'][i]) + "\\" + str(df1['camera_name'][i])+"_"+ str(j) + ".png"
                
                x,y,x_2,y_2 = df1['x0'][i],df1['y0'][i],df1['x1'][i],df1['y1'][i]
                img = cv2.imread(a)
                new_img = img[y:y_2,x:x_2]
                path1 = out+ df1['cls'][i]


                if not os.path.exists(path1):
                    os.mkdir(path1)
                os.chdir(path1)

                cv2.imwrite(path1+"\\"+'{0}_{1}_{2}_{3}_{4}_{5}.jpg'.format(str(df1['camera_name'][i]),str(df1['z_axis'][i]),str(df1['cell_number'][i]),"good_comp_3",str(j),str(k)),new_img)
            except:
                pass
                

