import os
import pandas as pd

def create_directories(directories):
    """
    Creates the necessary directories for storing plots and data.

    Args:
        directories (list of str): A list of directory paths to create.
    """
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def extract_transform():
    """
    Extracts and transforms data from arrest records for analysis

    Returns:
        - `pred_universe`: The dataframe containing prediction-related data for individuals
        - `arrest_events`: The dataframe containing arrest event data
        - `charge_counts`: A dataframe with counts of charges aggregated by charge degree
        - `charge_counts_by_offense`: A dataframe with counts of charges aggregated by both charge degree and offense category
    """
    # Extracts arrest data CSVs into dataframes
    pred_universe = pd.read_csv('https://www.dropbox.com/scl/fi/a2tpqpvkdc8n6advvkpt7/universe_lab9.csv?rlkey=839vsc25njgfftzakr34w2070&dl=1')
    arrest_events = pd.read_csv('https://www.dropbox.com/scl/fi/n47jt4va049gh2o4bysjm/arrest_events_lab9.csv?rlkey=u66usya2xjgf8gk2acq7afk7m&dl=1')

    # Creates two additional dataframes using groupbys
    charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
    charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name='count')

    # Create felony flag per arrest_id based on arrest_events
    felony_charge = arrest_events.groupby('arrest_id')['charge_degree'].apply(
        lambda degrees: (degrees == 'F').any()
    ).reset_index(name='has_felony_charge')

    # Merge felony charge flag into prediction universe
    # Convert arrest_id to string to avoid merge issues
    pred_universe['arrest_id'] = pred_universe['arrest_id'].astype(str)
    felony_charge['arrest_id'] = felony_charge['arrest_id'].astype(str)
    pred_universe = pred_universe.merge(felony_charge, on='arrest_id', how='left')

    # Fill missing felony charge flag as False
    pred_universe['has_felony_charge'] = pred_universe['has_felony_charge'].fillna(False)

    # Create rearrest_felony variable (boolean) = y_felony == 1 and has_felony_charge
    pred_universe['rearrest_felony'] = (pred_universe['y_felony'] == 1) & (pred_universe['has_felony_charge'])

    # Create charge_type column based on y_felony: 1 = Felony, else Misdemeanor
    pred_universe['charge_type'] = pred_universe['y_felony'].apply(lambda x: 'Felony' if x == 1 else 'Misdemeanor')

    return pred_universe, arrest_events, charge_counts, charge_counts_by_offense
