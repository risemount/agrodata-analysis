import pandas as pd
import os

crops = ["Rice", "Maize", "Wheat", "Soybean", "Tomato", "Sugarcane", "Taro", "Cabbage"]

response_files = os.listdir("./response/")

rice_header = {
    "縣市名稱": "COUNTYNAME",
    "初步種植面積": "BeginPlantArea",
    "實際種植面積": "RealPlantArea",
    "收穫面積": "HarvestArea",
    "無收穫面積": "NoHarvestArea",
    "稻穀總產量": "Yield",
    "稻穀單位產量": "UnitYield",
    "糙米總產量": "RiceYield",
    "糙米單位產量": "RiceUnitYield"
}

crop_header = {
    "縣市名稱": "COUNTYNAME",
    "種植面積": "RealPlantArea",
    "收穫面積": "HarvestArea",
    "每公頃收量": "UnitYield",
    "收量": "Yield"
}

# Initialize a new data frame
all_data = pd.DataFrame()

for crop in crops:
    # Filter filenames by crop
    fnames = [res for res in response_files if crop in res]

    for fname in fnames:
        splited_fname = fname.split("_")

        if len(splited_fname) == 3:
            year = int(splited_fname[1]) + 1911
            season = splited_fname[2].split(".")[0]
        else:
            year = int(splited_fname[1]) + 1911
            season = splited_fname[2]

        df = pd.read_csv(f"./response/{fname}", encoding = "big5")

        if crop == "Rice":
            # Rename Chinese header
            df.rename(columns = rice_header, inplace = True)
            df = df.filter(items = crop_header.values())
        else: 
            df.rename(columns = crop_header, inplace = True)

        df['Crop'] = crop
        df['Year'] = year
        df['Season'] = season

        df.drop([0, df.shape[0]-1], inplace = True)

        # Append the processed DataFrame to the main DataFrame
        all_data = pd.concat([all_data, df], ignore_index=True)
        

all_data.to_csv("./agrodata.csv", index = False, encoding = "big5")
        



