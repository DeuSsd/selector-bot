import json
from pathlib import Path



def get_token(tokenPath = "token.json"):
    # assert 
    tokenJson = ''
    with open(tokenPath, "r") as token_file:
        tokenJson = json.load(token_file)
    return tokenJson.get("TOKEN")
        


if __name__ == "__main__":
    tokenPath = 'token.json'
    get_token(tokenPath)


