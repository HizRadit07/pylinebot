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
            TextSendMessage(text="hello user\nchatbot here"))
    elif ('apa kabar' or 'gimana kabarnya') in msg:
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text="baik kok hehe"))
    elif 'test bot master' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="test ready, greetings Dαybreak-"))
    #easter egg functions, lol
    #dalam ITB messages
    #luar ITB messages
    elif '9' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di daerah Cisitu\n\n1.	Nama tempat fotokopi	: Alifia Fotocopy & Digital Printing\nNama Jalan		: Jalan Cisitu Lama No 42 Dago, Kecamatan Coblong,Bandung,Jawa Barat\nYang dijual		: Jasa Fotocopy,printing, ATK, laminating,jilid\nJam operasi		: \nSenin - Sabtu : 07.00 – 22.00\nMinggu : 10.00 – 22.00\nLink Gmaps		: https://goo.gl/maps/pJFHVczpXbnNsEYp6"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Mohon maaf, message belum dapat dimengerti\nSilakan masukan angka atau nama sesuai pilihan dibawah ini\n\nDalam ITB\n1. GKUB\n2. Labtek 5\n3. GKUT\n4. Labtek 8\n5. Labtek biru\n6. SBM\n7. ITB Press\n8. Gedung PAU\n\nLuar ITB\n9. Cisitu\n10. Dipatiukur(DU)\n11. Tubagus Ismail (Tubis)\n\nTerimakasih sudah menggunakan layanan chatbot ini"))
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
