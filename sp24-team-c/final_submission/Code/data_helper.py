import numpy as np
import pandas as pd


# read csv file
def read_csv(file_path):
    return pd.read_csv(file_path)


# clean data
def clean_data(df):
    # drop rows with missing values
    df = df.dropna()
    return df


# delete useless columns
def delete_columns(df, columns):
    return df.drop(columns, axis=1)


# according to column to sort the data
def sort_data(df):
    return df.sort_values(by='contact_addr1')


def preprocess_1():
    # read the data
    df = read_csv('PUBLIC_WORKS_VIOLATIONS.csv')
    # delete columns and update df
    df = delete_columns(df, ['case_no', 'value', 'ap_case_defn_key', 'status'])
    # clean data and update df
    df = clean_data(df)
    # sort data and update df
    '''
    place the sort function here
    df = sort_data(df)
    '''
    # save the cleaned data
    df.to_csv('cleaned_PUBLIC_WORKS_VIOLATIONS.csv', index=False)


def preprocess_2():
    # read the data
    df = read_csv('BUILDING_AND_PROPERTY_VIOLATIONS.csv')
    # delete columns and update df
    df = delete_columns(df, ['case_no', 'status', 'ticket_no'])
    # clean data and update df
    df = clean_data(df)
    # sort data and update df
    '''
    place the sort function here
    df = sort_data(df)
    '''
    # save the cleaned data
    df.to_csv('cleaned_BUILDING_AND_PROPERTY_VIOLATIONS.csv', index=False)


def preprocess_3():
    # read the data
    for i in range(0, 5):
        df = read_csv(f'311_Service_Requests_202{i}.csv')
        # delete columns and update df
        df = delete_columns(df, ['case_enquiry_id', 'sla_target_dt', 'closed_dt', 'submitted_photo', 'closed_photo'])
        # clean data and update df
        df = clean_data(df)
        # sort data and update df
        '''
        place the sort function here
        df = sort_data(df)
        '''
        # save the cleaned data
        df.to_csv(f'cleaned_311_Service_Requests_202{i}.csv', index=False)
