#abrir dict de real id
import random
from tkinter import messagebox as MBox
from tkinter import *
import pandas as pd

valor_randon = random.randint(0,999)

with open('fake_id/UK_F_ID.json', 'r')as file:
    listas = pd.read_json(file)
    df = pd.DataFrame(data=listas)
    nuevo_df = (df.iloc[valor_randon])

MBox.showinfo('FID_UK',f'{nuevo_df}')
