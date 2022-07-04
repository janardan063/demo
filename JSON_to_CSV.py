#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd , numpy as np, json

import cv2
f = open('F:/new_regions.json',)

data = json.load(f)

data = data.get('board_view')

cls= {}
values_list = []

for i in range(len(data)):
    if len(data[i]['region']) != 0:
        for j in range(len(data[i]['region'])):
            try:
                if data[i]['region'][j]['fillet_check'][0] == "Yes":
                    # print("********************")
                    class_name = data[i]['region'][j]['cls']
                    cls[class_name] = {}
                    cls[class_name]['z_axis'] = data[i]['z_axis']
                    camera_names = data[i]['camera_name'].split('_')
                    
                    camera_final_name = camera_names[0]+'_'+camera_names[-1:][0]
                    cls[class_name]['camera_name'] = camera_final_name.lower()
                    cls[class_name]['view'] = data[i]['view']
                    cls[class_name]['cell_number'] = data[i]['cell_number']
                    cls[class_name]['img_h'] = data[i]['img_size'][0]
                    cls[class_name]['img_w'] = data[i]['img_size'][1]


                    if cls[class_name]['camera_name'] == 'top_center':
                        dw = 5472
                        dh = 3648
                    else: 
                        dw = 2592
                        dh = 1944
                    
                    x0 = data[i]['region'][j]['x']*dw
                    y0 = data[i]['region'][j]['y']*dh
                    x1 = (data[i]['region'][j]['x']+data[i]['region'][j]['w'])*dw
                    y1 = (data[i]['region'][j]['y']+data[i]['region'][j]['h'])*dh

                    cls[class_name]['x0'] = int(x0)
                    cls[class_name]['y0'] = int(y0)
                    cls[class_name]['x1'] = int(x1)
                    cls[class_name]['y1'] = int(y1)
            except Exception as e:
#                 print("excpt issss::::",e)
                pass

new_2 = pd.Series(cls.keys())
df = pd.DataFrame(cls.values(), columns=['cell_number', 'z_axis' , 'camera_name','x0','y0','x1','y1'])
df['cls'] = new_2
df = df.replace(['top_back'],'top_bottom')

df.to_csv('F:/no_fillet.csv')

