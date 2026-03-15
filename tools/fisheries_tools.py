import pandas as pd
from difflib import get_close_matches

state_df = pd.read_csv("data/state_fisheries_stats.csv")
scheme_df = pd.read_csv("data/fisheries_schemes.csv")

states = state_df["state"].str.lower().tolist()
species_list = state_df["major_species"].str.lower().unique().tolist()
schemes = scheme_df["scheme_name"].str.lower().tolist()


def get_state_stats(query):

    match = get_close_matches(query, states, n=1, cutoff=0.6)

    if not match:
        return None

    result = state_df[state_df["state"].str.lower() == match[0]]

    row = result.iloc[0]

    return f"""
📍 State Fisheries Data

State: {row['state']}

Fish Production: {row['production_tonnes']} tonnes

Inland Fisheries: {row['inland_percent']} %

Marine Fisheries: {row['marine_percent']} %

Major Species: {row['major_species']}
"""


def get_species_info(query):

    match = get_close_matches(query, species_list, n=1, cutoff=0.6)

    if not match:
        return None

    result = state_df[state_df["major_species"].str.lower() == match[0]]

    states_found = ", ".join(result["state"].tolist())

    return f"""
🐟 Fish Species Information

Species: {match[0].title()}

Major Production States:
{states_found}
"""


def get_scheme_info(query):

    match = get_close_matches(query, schemes, n=1, cutoff=0.6)

    if not match:
        return None

    result = scheme_df[scheme_df["scheme_name"].str.lower() == match[0]]

    row = result.iloc[0]

    return f"""
📜 Fisheries Scheme

Name: {row['scheme_name']}

Description: {row['description']}

Benefits: {row['benefits']}

Eligible Beneficiaries: {row['eligible_beneficiaries']}

Subsidy: {row['subsidy']}
"""