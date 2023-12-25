from typing import Callable
from datetime import datetime

#Big notation O(n)

def func(num:list)->float:
  total=0
  for i in num:
    total+=i**2
  return float(total)

def total_time_cal(callback:Callable, values:list)->float:
  t1 = datetime.now()
  print(callback(values))
  t2 = datetime.now()
  diff = t2-t1
  print(f"Start time: {t1}")
  print(f"End time : {t2}")
  print(f" Difference in time : {diff.total_seconds()}")
  
  
total_time_cal(func,[1,2,3,4,5,56,89,565,24,2635,6565,465464,464,565,654,64,46,4,64,64,64,6,4,9,45,79,66,4,6,549,79,])