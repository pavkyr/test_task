# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
#complexity: O(n)
#memory: O(1)

def f(array:list,res:int)->list:
  left_p,right_p=0,len(l)-1

  while left_p<right_p:
    sum=l[left_p]+l[right_p]
    if sum==res:
      return [l[left_p],l[right_p]]
    if sum<res:
      left_p+=1
    else:
      right_p-=1

  return [-1]