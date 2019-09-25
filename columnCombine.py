#Aaron Brown IE 09/25/2019 (>0.0<)

"""
Purpose
To combine csvs from many datasets with matching column names
    - will combine as many csvs are in working directory


Usage
    - place csvs of all files to merge in one folder
    - add this scrpit to that same folder
    - double click this script to run
    - "combined.csv" will be added to folder
    - C'est tout! Passez une journée magique!

Notes
    - be sure to copy paste this file, not remove it from its origin
    - be sure to remove combined file if recombining in same working directory
        (if not removed, the combined.csv will be combined into
            new combined.csv and replace the old)

"""

import pandas as pd
import glob

all_files = glob.glob("*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv("combined.csv", encoding='utf-8', index=False)

"""
                       _____
                   .d88888888bo.
                 .d8888888888888b.
                 8888888888888888b
                 888888888888888888
                 888888888888888888
                  Y8888888888888888
            ,od888888888888888888P
         .'`Y8P'```'Y8888888888P'
       .'_   `  _     'Y88888888b
      /  _`    _ `      Y88888888b   ____
   _  | /  |  /  |      8888888888.d888888b.
  d8b | | /|  | /|      8888888888d8888888888b
 8888_| |_|/  |_|/      d888888888888888888888b
 .Y8P  `'-.            d88888888888888888888888
/          `          `      `Y8888888888888888
|                        __    888888888888888P
 |                       / `   dPY8888888888P'
  '._                  .'     .'  `Y888888P`
     `"'-.,__    ___.-'    .-'
         `-._````  __..--'`
             ``````
"""
