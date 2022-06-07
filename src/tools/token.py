import json
from pathlib import Path



def getToken(tokenPath = "token.json"):
    # assert 
    tokenJson = ''
    with open(tokenPath, "r") as token_file:
        tokenJson = json.load(token_file)
    return tokenJson
        


if __name__ == "__main__":
    tokenPath = 'token.json'
    getToken(tokenPath)


