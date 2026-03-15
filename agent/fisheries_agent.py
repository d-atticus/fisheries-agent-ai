from tools.fisheries_tools import get_state_stats, get_species_info, get_scheme_info


def run_agent(question):

    q = question.lower()

    state = get_state_stats(q)
    if state:
        return state

    species = get_species_info(q)
    if species:
        return species

    scheme = get_scheme_info(q)
    if scheme:
        return scheme

    return "Try searching for a state, fish species, or fisheries scheme."