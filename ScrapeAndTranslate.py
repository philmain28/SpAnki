'''
Created on Thu Dec 19 08:38:43 2019

@author: phil

Code to import song lyrics / subtitles from text files and dump them into an 
sqlite database.
'''

import glob 
import os
import sqlite3
from googletrans import Translator

#%%  Create raw table (only need to run once)

#imports songs in form of  .txt files
files = glob.glob(os.path.join('Songs', "*.txt"))



# Create an sql database for the lyrics
conn = sqlite3.connect('AnkiLyrics.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Lines
  ( Title       TEXT    NOT NULL,
    Line        TEXT     NOT NULL );'''
  )


#%% Scrape the txt files and dump the results into our database
for f in files:
    with open(f, "r") as file:
        title = os.path.basename(f)[:-4] # get rid of file extension 
        raw = file.read()
        lines = raw.split('\n') #split by line
        for line in lines: 
            # Now we make a database entry for each line
            s =  'insert into Lines (Title, Line) \
                  values ("{}","{}")'.format(title, line)
            cursor.execute(s);
            #print(s)

conn.commit()

#%% Creates filtered lyrics by removing blanks and duplicates
            
cursor.execute("select Line, Title from Lines where Line !='' or ' ' group by Line;")
filtered_lyrics = cursor.fetchall()


# Make new sql table
cursor.execute( ''' create table TranslatedLines ( 
  Line        text    not null,
  Translation text    not null, 
  Title       text    not null);'''
  )

translator = Translator(service_urls=['translate.google.com'])
for lyric in filtered_lyrics:
    # Translate lyric
    lyric_en = translator.translate(lyric[0], src='es', dest='en').text
    s =  'insert into TranslatedLines (Line, Translation, Title) \
    values ("{}","{}","{}")'.format(lyric[0], lyric_en, lyric[1])    
    # dump translation into table
    cursor.execute(s);

conn.commit()

