import pyfiglet,colorama,termcolor,random
from os import system
from requests import get

system('cls')
colorama.init()
print(termcolor.colored(pyfiglet.figlet_format("Italo Jokes"),color="red"))

search = input("Let me tell you a joke, gimme a topic : ")
answer = get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept":"application/json"},
    params={"term": f"{search}", "limit": 10,}
  
)
req = answer.json()
leng = len(req["results"])
final = req["results"]
randomjoke = random.randint(0,leng)
if randomjoke > 1:
    print(f"I've got {leng} jokes about {search} for you. Here's one: ")
    joke = final[randomjoke]
    print(joke["joke"])
elif randomjoke==1:
    print(f"I've got one joke about {search} for you. Here it is: ")
    joke = final[randomjoke]
    print(joke["joke"])
else:
    print("Sorry no jokes for this word")