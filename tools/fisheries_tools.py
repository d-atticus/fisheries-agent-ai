
import pandas as pd

schemes = pd.read_csv("data/fisheries_schemes.csv")
states = pd.read_csv("data/state_fisheries_stats.csv")
knowledge = pd.read_csv("data/fish_farming_knowledge.csv")


def scheme_tool(query):

    query = query.lower()

    for _, row in schemes.iterrows():
        if row["scheme_name"].lower() in query:
            return row.to_dict()

    return "Scheme not found."


def state_tool(query):

    query = query.lower()

    for _, row in states.iterrows():
        if row["state"].lower() in query:
            return row.to_dict()

    return "State data not found."


def knowledge_tool(query):

    query = query.lower()

    for _, row in knowledge.iterrows():
        if row["question"].lower() in query:
            return row["answer"]

    return "Information not found."
    
