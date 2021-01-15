# -*- coding: UTF-8 -*-
# Import system modules
import sys, os

# Import 3rd-Party Dependencies
from flask import (
    Flask, escape, request, redirect, url_for
)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# Import local modules
import env

#-----------------------------------------------------------#
#                   Channel API & Webhook                   #
#-----------------------------------------------------------#
config = env.get_server_config()
line_bot_api = LineBotApi(config["line-bot-api"]) # Channel Access Token
handler = WebhookHandler(config["webhook-handler"]) # Channel Secret

#-----------------------------------------------------------#
#                      Initialize Flask                     #
#-----------------------------------------------------------#
app = Flask(__name__)

#-----------------------------------------------------------#
#                          Callback                         #
#-----------------------------------------------------------#
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

#-----------------------------------------------------------#
#                    Text message handler                   #
#-----------------------------------------------------------#
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Retrieve user metadata
    user_id = event.source.user_id
    user_msg = event.message.text

    # Log user metadata
    print(f'User: {user_id}')
    print(f'Message: {user_msg}')

    resp = bot.converse(user_msg)

    # Reply user
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=resp)
    )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(
        host='0.0.0.0', 
        port=port,
        debug=True 
    )
