import json
import os

here = os.path.abspath(os.path.dirname(__file__))


def load_json(json_path):
    with open(json_path) as h:
        content = json.load(h)
    return content


def get_forms_lookup(forms_path="resources/forms_lookup.json"):
    matches_path = os.path.join(here, forms_path)
    return load_json(matches_path)


def get_match_dict(match_path="resources/match_dict.json"):
    matches_path = os.path.join(here, match_path)
    return load_json(matches_path)
