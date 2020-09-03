# -*- coding: UTF-8 -*-

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

# Import system modules
import sys, os

# Initialize Flask
app = Flask(__name__)

# Channel API & Webhook
line_bot_api = LineBotApi('XEQclTuSIm6/pcNNB4W9a2DDX/KAbCBmZS4ltBl+g8q2IxwJyqdtgNNY9KtJJxfkuXbHmSdQPAqRWjAciP2IZgrvLoF3ZH2C2Hg+zZMgoy/xM/RbnoFa2eO9GV2F4E1qmjYxA0FbJm1uZkUms9o+4QdB04t89/1O/w1cDnyilFU=') # Channel Access Token
handler = WebhookHandler('fabfd7538c098fe222e8012e1df65740') # Channel Secret

# Listen to all POST requests from HOST/callback
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

# @app.route("/demo")
# def demo():
#     userid = 'U96df1b7908bfe4d71970d05f344c7694'

#     text_message = TextSendMessage(
#         text='Hello, world!',
#         quick_reply=QuickReply(
#             items=[
#                 QuickReplyButton(action=MessageAction(label="Hello", text="Hello")),
#                 QuickReplyButton(action=MessageAction(label="Bounjour", text="Bounjour")),
#                 QuickReplyButton(action=MessageAction(label="Guten tag", text="Guten tag"))
#            ]
#         )
#     )

#     line_bot_api.push_message(
#         userid,
#         text_message
#     )

# Text message handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Print event metadata
    # print(event)

    # Retreive user metadata
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
    app.run(host='0.0.0.0', port=port)
