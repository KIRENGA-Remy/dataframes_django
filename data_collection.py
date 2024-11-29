import requests
import pandas as pd
try:
    # Fetch the vehicle data (hotels)
    vehicle_api = requests.get('http://127.0.0.1:8000/hotel/list/all')
    vehicle_api.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    vehicle_api_data = vehicle_api.json()
    # Fetch the tour owner data
    vehicle_owners_api = requests.get('http://127.0.0.1:8000/tours_list_all')
    vehicle_owners_api.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    vehicle_owners_api_data = vehicle_owners_api.json()
    # Convert the hotel data (list of dicts) into a pandas DataFrame
    vdf = pd.DataFrame(vehicle_api_data)
    print("The vdf is:\n{}".format(vdf))
    # Convert the tour owner data (list of dicts) into a pandas DataFrame
    odf = pd.DataFrame(vehicle_owners_api_data)
    print("The odf data is:\n{}".format(odf))
    merged_df = pd.merge(vdf, odf, on='id', how='inner')
    print(merged_df.head())
    # merged_df2 = pd.merge(vdf, odf, on='id', how='outer')
    # print(merged_df2.head())
    # merged_df3 = pd.merge(vdf, odf, on='id', how='cross')
    # print(merged_df3.head())
    # merged_df4 = pd.merge(vdf, odf, on='id', how='right')
    # print(merged_df4.head())
    # merged_df5 = pd.merge(vdf, odf, on='id', how='left')
    # print(merged_df5.head())
    # print("the shape of merged inner df is: {}".format(merged_df.shape))
    # print("the shape of merged outer df is: {}".format(merged_df2.shape))
    # print("the shape of merged cross df is: {}".format(merged_df3.shape))
    # print("the shape of merged right df is: {}".format(merged_df4.shape))
    # print("the shape of merged left df is: {}".format(merged_df5.shape))
    print("the null points are: {}".format(merged_df.isnull()))
    print("the sum of null points is: {}".format(merged_df.isnull().sum()))
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")









# import requests
# import pandas as pd
# inner_merged_df = None
# try:
#     # device data
#     device_api = requests.get('http://127.0.0.1:8000/devices/all?skip=0&limit=5000')
#     device_api.raise_for_status()
#     device_api_data = device_api.json()
#     #Owner data
#     device_owner_api = requests.get("http://127.0.0.1:8000/devices/owners?skip=0&limit=100")
#     device_owner_api.raise_for_status()
#     device_owner_data = device_owner_api.json()
#     #Data frame
#     ddf = pd.DataFrame(device_api_data)
#     odf = pd.DataFrame(device_owner_data)
#     #Merged data frame
#     inner_merged_df = pd.merge(ddf, odf, left_on="owner_id", right_on="id", how="outer")
#     # BEFORE Data cleaning
#     print("Before removing null values")
#     print(inner_merged_df.isnull().sum())
#     inner_merged_df.ffill(inplace=True)
#     inner_merged_df.bfill(inplace=True)
#     print("After removing null values")
#     print(inner_merged_df.isnull().sum())
#     # ================DATA PREPROCESSING DATE CONVERSION ==========
#     inner_merged_df['created_at'] = pd.to_datetime(inner_merged_df['created_at'])
#     print(inner_merged_df.dtypes)
#     # Cross merge
#     # inner_merged_df = pd.merge(ddf, odf, how="cross")
#     # return shape
#     print(inner_merged_df.shape)
#     # print("Merged DataFrame:")
#     # print(inner_merged_df)
# except requests.exceptions.RequestException as e:
#     print("Error during API call:", e)
# except KeyError as e:
#     print("Error during merging:", e)
