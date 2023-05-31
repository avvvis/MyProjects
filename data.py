import requests as r
import json as j

question_data = r.get("https://opentdb.com/api.php?amount=10&type=boolean").json()
question_data = question_data["results"]
