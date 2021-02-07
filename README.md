# SMS-Wikibot
This is a simple little project I threw together to learn about building SMS bots. The goal here is to allow people to read quick summaries of Wikipedia articles on their cell phones, even without an Internet connection.

## Setup
If you want to use this bot yourself, clone this repository and deploy it to a new Heroku app. Then, create an account and a number on Twilio. Under this new number, you can set a webhook to HTTP POST with the link to your heroku app. After doing so, simply text your Twilio number a command to see if it worked. I will update this guide in the future, but for now, [here](https://www.twilio.com/blog/build-a-sms-chatbot-with-python-flask-and-twilio) is a more general tutorial for setting up Twilio SMS bots with Flask apps.

## Commands
```
help
- Sends list of commands and how to use them.

search 'topic'
- Sends list of articles related to 'topic'
- (Omit single quotes when using command)

page 'topic'
- Sends summary of the article named 'topic'
- (again, omit quotes in use)

random
- Sends the user to a random article, still a bit buggy as I'm using the wikipedia api's builtin random function.
```

## Contributing
Feel free to add anything to this project with a pull request. I'm cool with whatever ideas you may have, as this project is more of a learning experience than anything for me.
