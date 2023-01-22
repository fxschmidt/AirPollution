"Zusätzliche Funktionen für die Jupyter Notebooks"
import numpy as np
import os
import json
from time import sleep
import requests as requests


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