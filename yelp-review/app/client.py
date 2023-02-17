"""Script to send request and display response"""
import requests

ENDPOINT_URL = "http://0.0.0.0:8080/infer"

def infer():
    document = r"Was it worth the for a salad and small pizza Absolutely not Bad service. Maybe the guys grandma died I don't know. I want to tell you what really made me mad about the experience. We order the small pizza and salad and the guys could have cared less and took our $ and we sat down. We were looking around and hmm, there's a sign saying x large pizza and large salad only 23. Wow that would have been nice if the guy told us that. I left hungry, mad and unsatisfied. To the owner: teach your employees the value of upselling and telling the specials. Something so small can affect a customers experience negatively. And your salads are severely overpriced Won't go back unless I'm desperate."
    data ={'document': document}
    response = requests.post(ENDPOINT_URL, json = data)
    response.raise_for_status()
    print(response.json())

if __name__ =="__main__":
    infer()