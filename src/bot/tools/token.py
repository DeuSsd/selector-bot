import json
# from pathlib import Path



def get_token(tokenPath = "token/token.json"):
    # assert 
    tokenJson = {"TOKEN": ""}
    try:
        with open(tokenPath, "r") as token_file:
            tokenJson = json.load(token_file)
        return tokenJson
    except FileNotFoundError as e:
        print(e)
        return tokenJson


if __name__ == "__main__":
    tokenPath = 'token.json'
    get_token(tokenPath)


