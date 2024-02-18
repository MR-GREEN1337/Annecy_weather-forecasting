import os
import pandas as pd
import hopsworks

def dataset_normalizer(dataset_df):
    '''
    Given a dataset with the columns names extracted from the APIs data, return a dataset (dataframe)
    with the name of the columns according to the feature group on Hopsworks platform
    '''

    pass


def dataset_uploader(project, normalized_dataset_df):
    '''
    Given the Hopsworks project and a normalized dataset, upload it to Hopsworks
    '''
    fs = project.get_feature_store()
    fg = fs.get_or_create_feature_group(
        name="annecy-weather",
        version=1,
        primary_key=['date', 'time', 'dep_ap_iata_code', 'arr_ap_iata_code', 'flight_iata_number'], 
        description="Annecy weather data")
    fg.insert(normalized_dataset_df)


hopsworks_api_key = os.environ["HOPSWORKS_API_KEY"]
project = hopsworks.login(api_key_value = hopsworks_api_key)

dataset_df = pd.read_csv("/workspaces/Annecy_weather-prediction/datasets/annecy_weather_data_open_weather.csv")
#normalized_dataset_df = dataset_normalizer(dataset_df)

dataset_uploader(project, dataset_df)