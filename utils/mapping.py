"""Mapping
Given a county input, return it's SSR (Standard Statistical Region)
"""


mapping = {
    "North": ["Cleaveland", "Durham", "Northumberland"],
    "North West": ["Cheshire", "Greater Manchester", "Lnancashire"],
}


def county_to_ssr(county):
    for ssr, c in mapping.items():
        if county in c:
            return ssr
        else:
            return False
