import requests
from dotenv import load_dotenv
import os

load_dotenv()



token= os.getenv("GITHUB_TOKEN")
URL="https://api.github.com/graphql"
username="aadyasingh2"
query=f"""query{{
            user(login:"{username}"){{
                contributionsCollection
                {{
                    contributionCalendar
                  {{
                        totalContributions,
                        weeks
                        {{
                            contributionDays
                            {{
                                date,contributionCount
                            }}
                        }}
                    }}
                }}
            }}
        }}"""
response=requests.post(URL,json={"query":query},headers={'Authorization':"Bearer "+token})
print(response.json())
graphdata=response.json()['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
