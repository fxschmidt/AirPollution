"Zusätzliche Funktionen für die Datenanalyse"
import numpy as np
import os
import json
from time import sleep
import requests as requests

def calc_aqi(df,whitout_pm10=True):
    """Calulate the AirQualityIndex for the five key pollutants (poorest level counts). 
    For more see the Dokumentation Folder. The concentrations should be in micro g/m3

    Args:
        df (pd.DataFrame): DataFrame which contain the pollutants
        without_pm10 (Noolean): If the df contains no pm10 column
    Return:
        int: 0 to 5 which represents the quality levels
        list of str: pollutant which is too high
    """
    if whitout_pm10:
        pm2_5,no2,o3,so2 = df[["mean_pm2_5","max_value_no2","max_value_o3","max_value_so2"]]
        #set zero because there is no data for pm10
        pm10=0
    else:
        pm2_5,pm10,no2,o3,so2 = df[["mean_pm2_5","mean_pm10","max_value_no2","max_value_o3","max_value_so2"]]
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
    aqi_values = np.array([pm2_5,pm10,o3,no2,so2])
    aqi_max= np.max(aqi_values)
    # which value is too high, return the pollutant only if level is above fair
    if aqi_max>=1:
        aqi_max_idx = np.argwhere(aqi_max == aqi_max)
        aqi_max_pollutant = [pollutants[i] for i in aqi_max_idx.flatten().tolist()]
    else:
        aqi_max_pollutant=[]
    return aqi_max,aqi_max_pollutant
    
def get_epa_data(param: int,year: int,site: int,folder: str,check_exists=True,only_get_path=False ):
    """Get the data from one of the sites in LA on a daily base


    Args:
        param (int): Parameters of the pollution type (only one)
        year (int): Year
        site (int): use the site code with 4 digits
        folder (str): folder to save the results
        check_exists (Boolean, optional): Check if the data already exists.
        only_get_path (Boolean, optional): only returns the filepath.
    """
    email="felixsch00@outlook.de"
    api_key="goldfox88" 
    #check if file already exists
    savepath=f"{folder}/{param}_{year}_{site}.json"
    if only_get_path:
        return savepath
    if os.path.exists(savepath) and check_exists:
        print(f"Already exists: Year: {year}, Parameter: {param}, Site: {site}")
        return 
    param = str(param)
    state="06"
    county="037"
    bdate = str(year) + "0101"
    edate = str(year) + "1231"
    parameters_req={"email":email,"key":api_key,"param": param  , "bdate":bdate,"edate":edate,"state":state,"county":county,"site":site}
    request_aqi=requests.get(
        f"https://aqs.epa.gov/data/api/dailyData/bySite?",params=parameters_req)
    #print(f"API Request sucessfull: {request_aqi.status_code}")
    if not request_aqi.json()["Data"]: 
        print("Request Empty")
        return 
    if request_aqi.status_code == 200:
        print(f"Save as JSON")
        request_aqi.json()
        with open(savepath,"w") as file:
                json.dump(request_aqi.json(),file,indent=4)
        print(f"Sucessfully get: Year: {year}, Parameter: {param}, Site: {site}")
        sleep(5)
    return 

def change_pollution_unit(df_column,start_unit: str, pollutant: str):
    """Change the Unit of the pollution. The Formula is shown in the get_Data_AirPollution file.

    Args:
        df_column (pd.DataFrame or pd. Series): Columns you want to change the unit (only columns of the same pollutant)
        start_unit (str): Choose from "ppm" and "ppb"
        pollutant (str): Choose from no2, co, so2,o3

    Returns:
        pd.DataFrame: now with the correct unit
    """
    #molare Masse für jeden Schadstoff in g/mol
    M={"no2":46,"o3":48,"so2":64,"co":28}
    try: 
        M=M[pollutant]
    except:
        print("Pollutant isnt key in dict")
    # convert to ppb if necesssary
    if start_unit=="ppm":
        x=df_column
    elif start_unit=="ppb":
        x=df_column/1000
    
    p=1000
    r=8.314
    t=300
    
    y= (0.1 * M * p * x * 1000)/(r*t)
    return y