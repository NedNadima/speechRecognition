import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative","si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ['no', 'negative', 'nope', 'get the fuck out']

    def discover(self,text):
        if "what" in text and " name" in text:
            if "my" in text:
                self.respond('You have not told me your name yet')
            else:
                self.respond("My name is Pie Commander. How are you?")
        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)


    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)

