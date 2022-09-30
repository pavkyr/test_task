# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

import re 

def fun(num:int)->list:
  result=[]
  match=re.findall(r'([5-6]{2,})',str(num))
  if len(match)==0:
    return 0
  for i in match:
    lenght=len(i)
    if i != lenght*'5' and i !=lenght*'6':
      result.append(i)
  return int(max(result))