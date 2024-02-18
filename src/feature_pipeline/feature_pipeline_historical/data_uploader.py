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
    pass


hopsworks_api_key = os.environ['HOPSWORKS_API_KEY']
project = hopsworks.login(api_key_value = hopsworks_api_key)

dataset_df            = pd.read_csv('/mnt/c/Developer/University/SML/sml-project-2023-manfredi-meneghin/datasets/join_dataset_smhi_zyla.csv')
normalized_dataset_df = dataset_normalizer(dataset_df)

dataset_uploader(project, normalized_dataset_df)