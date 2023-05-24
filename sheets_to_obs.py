"""
Created on Tue May 23 12:21:35 2023

@author: dexter
"""
import gspread as gs
import pandas as pd
import time
runsToday=0
while True:
    gc = gs.service_account(filename="<google API service account key json file>")
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1vCcApZK2EVmAmpxkFGzFs9Ys76zHXCa61U5gkSzZNWs/edit#gid=0')
    sheet=sh.worksheet('Sheet1').get_all_values()
    df = pd.DataFrame(sheet[1:], columns=sheet[0])
    #print(df.head())
    
    igt_times1=list(df['Time'])
    dates_played=df['Date']
    dates=[]
    run_number=df['Run Counter']
    max_run_number=0
    
    for i in range(len(dates_played)):
      if dates_played[i]!='':
        dates.append([i,dates_played[i]])
    
    runs_per_day=[i[0] for i in dates]
    date = [i[1] for i in dates]
    
    for i in range(len(runs_per_day)-2,len(runs_per_day)-1):
      times=[]
      
      for j in range(runs_per_day[i],runs_per_day[i+1]):
        #print(igt_times1[j])
        
        
        if igt_times1[j]=='':
          continue
        if j==0:
          continue
        else:
          times.append(igt_times1[j])
          max_run_number=run_number[j]
    
    
    if len(times)>runsToday:
        runsToday=len(times)
        print(times)
        print(max_run_number)
        with open('<Text file to write data into>', 'w') as f:
            content='Sub 20s: '+str(max_run_number)+'/1000 \nToday: \n'
            
            for i in range(len(times)):
                content+=str(times[i])
                content+=', '
                if i%2==1:
                    content+='\n'
            f.write(content)
    time.sleep(60)
    
    
