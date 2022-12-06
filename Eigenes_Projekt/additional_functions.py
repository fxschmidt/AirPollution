"Zusätzliche Funktionen für die Datenanalyse"
import numpy as np 

def calc_aqi(pm2_5: float,pm10: float,no2: float,o3: float,so2: float,return_string=False):
    """Calulate the AirQualityIndex for the five key pollutants (poorest level counts). 
    For more see the Dokumentation Folder. The concentrations should be in micro g/m3

    Args:
        pm2_5 (float): Particles less than 2.5 µm
        pm10 (float): Particles less than 10 µm
        no2 (float): Nitrogen dioxide
        o3 (float): Nitrogen dioxide
        so2 (float): Sulphur dioxide
        return_string(Boolean): True if a string with the description should be returned
    Return:
        int: 0 to 5 which represents the quality levels (if retrun_string False)
        list of str: pollutant which is too high
    """
    #classify pm2.5
    if pm2_5<10:
        pm2_5=0
    elif pm2_5<20:
        pm2_5=1
    elif pm2_5<25:
        pm2_5=2
    elif pm2_5<50:
        pm2_5=3
    elif pm2_5<75:
        pm2_5=4
    else:
        pm2_5=5
        
    if pm10<20:
        pm10=0
    elif pm10<40:
        pm10=1
    elif pm10<50:
        pm10=2
    elif pm10<100:
        pm10=3
    elif pm10<150:
        pm10=4
    else:
        pm10=5
        
    if no2<40:
        no2=0
    elif no2<90:
        no2=1
    elif no2<120:
        no2=2
    elif no2<230:
        no2=3
    elif no2<340:
        no2=4
    else:
        no2=5
        
    if o3<50:
        o3=0
    elif o3<100:
        o3=1
    elif o3<130:
        o3=2
    elif o3<240:
        o3=3
    elif o3<380:
        o3=4
    else:
        o3=5    
        
    if so2<100:
        so2=0
    elif so2<200:
        so2=1
    elif so2<350:
        so2=2
    elif so2<500:
        so2=3
    elif so2<750:
        so2=4
    else:
        so2=5
            
    # choose the highest AQI Value
    pollutants = ["pm2_5","pm10","o3","no2","so2"]
    aqi_index = np.array([pm2_5,pm10,o3,no2,so2])
    aqi_max = np.max(aqi_index)
    # which value is too high, return the pollutant only if level is above fair
    if aqi_max>=1:
        aqi_max_idx = np.argwhere(aqi_index == aqi_max)
        aqi_max_pollutant = [pollutants[i] for i in aqi_max_idx.flatten().tolist()]
    else:
        aqi_max_pollutant=[]
    if return_string:
        description=["Good","Fair","Moderate","Poor","Very poor","Extremely poor"]
        return description[aqi_max] , aqi_max_pollutant
    else: 
        return aqi_max,aqi_max_pollutant
    

