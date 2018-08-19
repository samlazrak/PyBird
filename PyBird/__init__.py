""" Wrapper functions for eBird 2.0 API """
import requests

from PyBird.data import RECENT_OBS_IN_REGION, RECENT_NOTABLE_OBS_IN_REGION, RECENT_OBS_OF_SPECIES_IN_REGION, \
  RECENT_NEARBY_OBS, RECENT_NEARBY_OBS_OF_SPECIES, NEAREST_OBS_OF_SPECIES, RECENT_NEARBY_NOTABLE_OBS, HISTORIC_OBS_ON_DATE
from PyBird.product import TOP_100, CHECKLIST_FEED_ON_DATE, RECENT_CHECKLIST_FEED, REGIONAL_STATS_ON_DATE, VIEW_CHECKLIST
from PyBird.ref import ADJACENT_REGIONS, HOTSPOTS_IN_REGION, NEARBY_HOTSPOTS, eBIRD_TAXONOMY, TAXONOMIC_FORMS, \
  TAXONOMY_VERSIONS, TAXONOMIC_GROUPS, HOTSPOT_INFO, REGION_INFO, SUB_REGION_LIST

def request(token, url, queryString):
  headers = {'X-eBirdApiToken': token}
  if queryString is not None:
    response = requests.request("GET", url, headers=headers, params=queryString)
    return response
  else:
    response = requests.request("GET", url, headers=headers)
    return response