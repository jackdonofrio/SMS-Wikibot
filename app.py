from flask import Flask, request
import requests
import wikipedia
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def default():
    return "Default" # I added this so that the Heroku Awake Github Action could keep the app awake
                     # without constantly getting 405 errors from trying to access /bot which only accepts POST

# Todo: break each if statement into a separate function for each command
@app.route('/bot',methods=['POST'])
def wikibot():
    incoming_message = request.values.get('Body','').lower()
    response = MessagingResponse()
    message = response.message()

    if incoming_message.startswith('help'):
        help_message = 'Hey. These are the commands you may use: search topic, page topic, random. ' + \
            'Replace "topic" with the name of the article you\'re looking for.'
        message.body(help_message)

    elif incoming_message.startswith('search '):
        potential_pages = wikipedia.search(incoming_message[incoming_message.index(' ') + 1:].strip())
        message_to_send = 'Pages found: ' + \
            ', '.join(["'" + p + "'" for p in potential_pages]) + '. To access a page, send: page name'
        message.body(message_to_send)
    
    elif incoming_message.startswith('page '):
        page_data = wikipedia.summary(incoming_message[incoming_message.index(' ') + 1:].strip(), sentences=10)
        message.body(page_data) # sends all content on page to user
    
    elif incoming_message.startswith('random'):
        page_title = wikipedia.random()[0]
        page_data = wikipedia.summary(page_title)
        message.body(page_data)

    return str(response)


# TEMPLATE DO NOT DELETE< JUST COMMENT OUT
# @app.route('/bot', methods=['POST'])
# def bot():
#     incoming_msg = request.values.get('Body', '').lower()
#     resp = MessagingResponse()
#     msg = resp.message()
#     responded = False
#     if 'quote' in incoming_msg:
#         # return a quote
#         r = requests.get('https://api.quotable.io/random')
#         if r.status_code == 200:
#             data = r.json()
#             quote = f'{data["content"]} ({data["author"]})'
#         else:
#             quote = 'I could not retrieve a quote at this time, sorry.'
#         msg.body(quote)
#         responded = True
#     if 'cat' in incoming_msg:
#         # return a cat pic
#         msg.media('https://cataas.com/cat')
#         responded = True
#     if not responded:
#         msg.body('I only know about famous quotes and cats, sorry!')
#     return str(resp)
# TEMPLATE DO NOT DELETE < JUST COMMENT OUT


if __name__ == '__main__':
    app.run(debug=True)