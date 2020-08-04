import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('LbHx7WcclcnKZEXObf/61gLinA2aXMG8+6wBYSA8D1OhCipAeM6W4yO+QTpvTs4kdC4g8RasrB7JWnI9xUYEc8h9MjhMmTI5L2I+8syR2B1Zb27JYM1AvBRz+MDb0Grjtea7XLMi+xMxW2ItGrrcEwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3f370e84e86ff86735234ed09c6d1fbf')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Here's all the messages will be handled and processed by the program """
    
    msg = (event.message.text).lower()
    
    if 'hello' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="hello user"))
    elif 'apa kabar' in msg:
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text="baik kok hehe"))
    elif '1' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='1.	Nama tempat fotokopi	: Rindu Dago Digital Printing   Alamat			: Jl. Tubagus Ismail Raya No.1, Lebakgede, Kecamatan Coblong, Kota Bandung, Jawa Barat 40132    Yang dijual		: Jasa fotokopi, print foto,print laser, ID Card, ATK, hard cover, soft cover, jilid ring, laminating   Jam operasi		: 24 Jam    Link google maps	: https://www.google.com/maps/dir//fotokopi+tubagus+ismail/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x2e68e6f924ae1f07:0x2702d20bd94addf3?sa=X&ved=2ahUKEwiewJ7dgv7qAhUQU30KHT_5CW8Q9RcwAHoECAYQCg'))                         
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))
    #fungsi apakabar dan hello test
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
