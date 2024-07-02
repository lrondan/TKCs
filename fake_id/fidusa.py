import pandas as pd
from tkinter import messagebox as MBox
from tkinter import *
import random

valor_randon = random.randint(0,232)

with open('fake_id/USA_F_ID.json', 'r')as file:
    listas = pd.read_json(file)
    df1 = pd.DataFrame(data=listas)
    nuevo_df = (df1.iloc[valor_randon])

MBox.showinfo('FID_UK',f'{nuevo_df}')
