import pandas as pd

#Functions for implementation
#def getTime

data = pd.read_csv('/Users/young_vo/Downloads/hydrate_detection_project/data/data2.csv')


pipeOpen = True
ignore = False
numsOfWarning = 0
index = 0
previousVolume = data.iloc[0]['Inj Gas Meter Volume Instantaneous']
previousValve = data.iloc[0]['Inj Gas Valve Percent Open']

while index < len(data):
    if(pd.isna(data.iloc[index]['Inj Gas Valve Percent Open'])):
        valve = previousValve
    else:
        valve = data.iloc[index]['Inj Gas Valve Percent Open']
    
    if(pd.isna(data.iloc[index]['Inj Gas Meter Volume Instantaneous'])):
        volume = previousVolume
    else:
        volume = data.iloc[index]['Inj Gas Meter Volume Instantaneous']

    if previousVolume == 0 and volume != 0:
        pipeOpen = True
    if previousValve == 100 and valve != 100:
        ignore = False

    jump = valve - previousValve
    if valve == 100 and jump < 50:
        if ignore == True:
            ignore = False
            continue
        else:
            if volume == 0 and pipeOpen:
                numsOfWarning += 1
                pipeOpen = False
    
    if jump > 50:
        ignore = True

    index += 1
    previousVolume = volume
    previousValve = valve

print(numsOfWarning)