import json
from dotenv import load_dotenv

def load_env():
    load_dotenv()

def save_review(review: str,filename:str="rebiew.json"):
    if filename.endswith(".json"):
        with open(filename,"w",encoding="utf-8") as f:
            json.dump({"review":review},f,indent=2)
    else:
        with open(filename, "w",encoding="utf-8") as f:
            f.write(review)