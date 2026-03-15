from tools.fisheries_tools import (
    get_state_stats,
    get_species_info,
    get_scheme_info
)

def run_agent(message):

    query = message.lower()

    # try state tool
    state = get_state_stats(query)
    if state:
        return state

    # try species tool
    species = get_species_info(query)
    if species:
        return species

    # try scheme tool
    scheme = get_scheme_info(query)
    if scheme:
        return scheme

    return """
🤖 Fisheries AI Assistant

Try asking:

• Bihar fisheries
• Rohu fish
• PMMSY scheme
• Inland fisheries production
"""