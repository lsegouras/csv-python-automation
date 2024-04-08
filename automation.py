#Step by step

#pip install py
import pyautogui as py
import time

py.PAUSE = 0.5

#click => py.click
#write => py.write
#press => py.press
#shortcut=> py.hotkey

#Step 1 - Enter the company system - https://dlp.hashtagtreinamentos.com/python/intensivao/login

#press windows key
py.press("win")
#enter program name (chrome)
py.write("chrome")
#enter
py.press("enter")

#enter chrome user
time.sleep(3)
py.click(x=1098, y=447)

#find navigation bar
py.click(x=1291, y=93)

# write link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.write(link)
py.press("enter")

# wait 3 seconds
time.sleep(3)

#Step 2 - Login
py.click(x=864, y=557)
py.write("teste@gmail.com")
py.press("tab")
py.write("password")
py.press("tab")
py.press("enter")
time.sleep(3)

#Step 3 - Import CSV
#pip install pandas numpy openpyxl
import pandas as pd

table = pd.read_csv("products.csv")
print(table)

#Step 5 - Repeat until finish the database

for row in table.index:

#Step 4 - Register a product

  py.click(x=712, y=383)
  #code
  py.write(str(table.loc[row, "code"]))
  py.press("tab")

  #brand
  py.write(str(table.loc[row, "brand"]))
  py.press("tab")

  #type
  py.write(str(table.loc[row, "type"]))
  py.press("tab")

  #category
  py.write(str(table.loc[row, "category"]))
  py.press("tab")

  #price
  py.write(str(table.loc[row, "price"]))
  py.press("tab")

  #cost
  py.write(str(table.loc[row, "cost"]))
  py.press("tab")

  #obs
  obs = table.loc[row, "obs"]
  if not pd.isna(obs):
    py.write(str(obs))   
  

  py.press("tab")

  py.press("enter")

  py.scroll(5000)

