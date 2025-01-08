#%%
import pickle
from pathlib import Path
from fubon_neo.sdk import FubonSDK

with open('info.pkl', 'rb') as f:
    user_info_dict = pickle.load(f)

sdk = FubonSDK()
accounts = sdk.login(user_info_dict['id'], user_info_dict['pwd'], Path(user_info_dict['cert_path']).__str__())
print(accounts)
#%%

sdk.init_realtime() # 建立行情連線
reststock = sdk.marketdata.rest_client.stock  
reststock.intraday.ticker(symbol='2330')
# %%
