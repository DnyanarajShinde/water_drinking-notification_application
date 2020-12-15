# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:02:02 2020

@author: lenovo
"""

import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
                
               title = "please drink water now",
               message ="The National Academies of Sciences, Engineering and Medicine determined that an adequate daily fluid intake is: about 15.5 cups (3.7 litres) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
               app_icon="C:/Users/lenovo/Desktop/water/icon.ico",
               timeout=5
               )
        time.sleep(60*60)