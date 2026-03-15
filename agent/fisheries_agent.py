
from tools.fisheries_tools import scheme_tool, state_tool, knowledge_tool


def run_agent(query):

    q = query.lower()

    if "scheme" in q or "pmmsy" in q:
        return scheme_tool(query)

    elif "production" in q or "state" in q:
        return state_tool(query)

    else:
        return knowledge_tool(query)
