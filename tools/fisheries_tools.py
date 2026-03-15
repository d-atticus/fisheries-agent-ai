import pandas as pd

state_df = pd.read_csv("data/state_fisheries_stats.csv")
scheme_df = pd.read_csv("data/fisheries_schemes.csv")


def get_state_stats(query):

    result = state_df[state_df["state"].str.lower().str.contains(query.lower())]

    if result.empty:
        return None

    row = result.iloc[0]

    return f"""
📍 State Fisheries Data

State: {row['state']}
Fish Production: {row['production_tonnes']} tonnes
Inland Fisheries: {row['inland_percent']}%
Marine Fisheries: {row['marine_percent']}%
Major Species: {row['major_species']}
"""


def get_species_info(query):

    result = state_df[state_df["major_species"].str.lower().str.contains(query.lower())]

    if result.empty:
        return None

    states = ", ".join(result["state"].tolist())

    species = result.iloc[0]["major_species"]

    return f"""
🐟 Fish Species Information

Species: {species}

Major production states:
{states}
"""


def get_scheme_info(query):

    result = scheme_df[scheme_df["scheme_name"].str.lower().str.contains(query.lower())]

    if result.empty:
        return None

    row = result.iloc[0]

    return f"""
📜 Fisheries Scheme

Name: {row['scheme_name']}
Description: {row['description']}
Benefits: {row['benefits']}
Eligible: {row['eligible_beneficiaries']}
Subsidy: {row['subsidy']}
"""