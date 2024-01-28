
import re

# Function to extract Req/Defect IDs and comments from the commit message
def extract_req_id_defect_id(commit_message):
    # Pattern to match Req/Defect IDs
    id_pattern = r'\b(Req \d+|Defect \d+)\b'
    matches = re.findall(id_pattern, commit_message)
    request_id = ' '.join(matches)
    return request_id


import tokenize


def tokenize_code(code):
    return [tok.string for tok in tokenize.tokenize()]