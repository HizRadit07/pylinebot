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
            print(msg)
    elif ('apa kabar' in msg) or ('gimana kabarnya' in msg):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text="baik kok hehe"))
    elif 'test bot master' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="test ready, greetings Dαybreak-"))
    elif msg=="9001":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="ITS OVER 9000!!!!!!!!!!!!!!"))
    #easter egg functions, lol
    #dalam ITB messages
    elif (msg=='1') or (msg=='GKUB') or (msg=='gkub') or (msg=='Gkub'):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text="List tempat fotokopi di GKUB\n\n1. GKUB LT 1\nJUAL LENGKAP\njam operasional: 9.00-16.00\n\n2. GKUB LT 1\nJUAL LENGKAP\nJam operasional: 09.00-17.00"))
    elif (msg=='2'):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text="List tempat fotokopi di Labtek V\n\n1. LABTEK V LT 1 (DEKAT SEKRE HMIF 1)\nHANYA FOTOKOPI PRINT\nJam operasional: 09.00-15.00"))
    elif (msg=='3') or (msg=='GKUT') or (msg=='Gkut') or (msg=='gkut'):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text="List tempat fotokopi di GKUT\n\n1. GKUT LT 1\nJUAL LENGKAP\nJam operasional: 09.00 - 15.00"))
    elif (msg=='4'):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text="List tempat fotokopi di LABTEK VIII\n\n1. LABTEK VIII LT BASEMENT\nHANYA FOTOKOPI, PRINT\nJam operasional: 09.00-15.00"))
    elif (msg=='5') or (msg=='Labtek biru') or (msg=='labtek biru'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di Labtek biru\n\n1. LABTEK BIRU LT 1\nJUAL LENGKAP\nJam operasional: 09.00-16.00"))
    elif (msg=='6') or (msg=='sbm') or (msg=='SBM') or (msg=='Sbm'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di SBM\n\n1. SBM LT 2\nJUAL LENGKAP\nJam operasional: 09.00-15.00"))
    elif (msg=='7') or (msg=='ITB Press') or (msg=='Itb press') or (msg=='itb press'):
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di ITB Press\n\n1. ITB Press (Di belakang perpustakaan)\nHanya Fotokopi\nJam operasional: 09.00-17.00\nLink google maps: https://goo.gl/maps/mVAZPxmtv5sXtdGF7"))
    elif (msg=='8') or (msg=='PAU') or (msg=='pau') or (msg=='Pau' ) or (msg=='Gedung PAU' ) or (msg=='gedung PAU' ) or (msg=='Gedung pau' ) or (msg=='gedung pau'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di Gedung PAU\n\n1. GEDUNG PAU LT 1 (BAGIAN DEPAN)\nHANYA FOTOKOPI,PRINT\nJam operasional: 09.00-15.00"))
    #luar ITB messages
    elif (msg=='9') or (msg=='cisitu') or (msg=='Cisitu'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di daerah Cisitu\n\n1.	Nama tempat fotokopi	: Alifia Fotocopy & Digital Printing\nNama Jalan		: Jalan Cisitu Lama No 42 Dago, Kecamatan Coblong,Bandung,Jawa Barat\nYang dijual		: Jasa Fotocopy,printing, ATK, laminating,jilid\nJam operasi		: \nSenin - Sabtu : 07.00 – 22.00\nMinggu : 10.00 – 22.00\nLink Gmaps		: https://goo.gl/maps/pJFHVczpXbnNsEYp6\n\n2.    Nama tempat fotokopi	: Putri Copy Centre\nNama Jalan		: Jl. Cisitu Lama No.32, Dago, Kecamatan Coblong, Kota Bandung, Jawa Barat 40135\nYang dijual		: ATK,Jasa printing,fotocopy,Jilid,Laminating,Scaning,Cetak Foto\nJam operasi		: \nSenin - Sabtu : 07.00 – 22.00\nMinggu : 10.00 – 21.00\nLink Gmaps		: https://goo.gl/maps/GpM5iWL5PKBCw43E6\n\n3.   Nama tempat fotokopi	: Edo Copy Centre\nNama Jalan		: Jl. Cisitu Lama No.37, Dago, Kecamatan Coblong, Kota Bandung, Jawa Barat 40135\nYang dijual		: ATK, Print Foto, Print dan Fotocopy,Laminating,Jilid\nJam operasi		: \nSenin - Sabtu : 07.00 – 22.00\nMinggu : 10.00 – 22.00\nLink Gmaps		: https://goo.gl/maps/eqiZK3duCGGR5QoNA"))
    elif (msg=='10') or (msg=='DU') or (msg=='Du') or (msg=='du') or (msg=='Dipatiukur') or (msg=='dipatiukur'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di daerah Dipatiukur (DU)\n\n1. Nama tempat fotokopi	: Jaya Abadi Photocopy\nNama jalan		: Jl. Dipati Ukur No.269, Lebakgede, Kecamatan Coblong, Kota Bandung, Jawa Barat 40132\nYang dijual		: Jasa fotokopi, mencetak dokumen, ATK, hard cover, soft cover, jilid ring, laminating\nJam operasi		: \nSenin s.d Kamis buka 24 jam\nJumat 24.00 – 11.00 dan 13.00 – 23.59 \nSabtu 12.00 – 19.00\nMinggu 08.00 – 12.00\nLink google maps	: https://goo.gl/maps/YW4JZ8sSnAP6KVY87\n\n2.   Nama tempat fotokopi	: Cahaya Abadi Fotocopy, Penjilidan & Digital Printing\nNama jalan		: Jl. Dipati Ukur No.122D, Lebakgede, Kecamatan Coblong, Kota Bandung, Jawa Barat 40132\nYang dijual		: Print, scan, fotokopi, penjilidan, dll.\nJam operasi		: Senin s.d Minggu buka 24 jam\nLink google maps	: https://goo.gl/maps/yPuU8ZZwNKDJSXnVA\n\n3.	Nama tempat fotokopi	: Gugum Offset\nNama jalan		: Jl. Dipati Ukur No.42 /60, Lebakgede, Kecamatan Coblong, Bandung, Jawa Barat 40132\nYang dijual		: Print, fotokopi, penjilidan, dll.\nJam operasi		: Senin s.d Minggu pukul 08.00 – 21.00\nLink google maps	: https://goo.gl/maps/NfagCS1RsKRc9mn6A"))
    elif (msg=='11') or (msg=='Tubis') or (msg=='tubis') or (msg=='Tubagus Ismail') or (msg=='tubagus ismail') or (msg=='Tubagus ismail'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List tempat fotokopi di daerah Tubagus Ismail (Tubis)\n\n1.   Nama tempat fotokopi	: Rindu Dago Digital Printing & Copier\nAlamat			: Jl. Tubagus Ismail Raya No.1, Lebakgede, Kecamatan Coblong, Kota Bandung, Jawa Barat 40132\nYang dijual		: Jasa fotokopi, print foto,print laser, ID Card, ATK, hard cover, soft cover, jilid ring, laminating\nJam operasi		: 24 Jam\nLink google maps	: https://www.google.com/maps/dir//fotokopi+tubagus+ismail/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x2e68e6f924ae1f07:0x2702d20bd94addf3?sa=X&ved=2ahUKEwiewJ7dgv7qAhUQU30KHT_5CW8Q9RcwAHoECAYQCg\n\n2.	Nama tempat fotokopi	: Batara\nAlamat			: Jl. Tubagus Ismail Bawah, Lebakgede, Kecamatan Coblong, Kota Bandung, Jawa Barat 40132\nYang dijual		: Jasa fotokopi, print foto, ATK, jilid ring, laminating\nJam operasi		: 08.00-21.00 WIB\nLink google maps	: https://www.google.com/maps/dir//fotokopi+di+tubagus+ismail/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x2e68e6544cbae1a1:0xb3260f8914f18543?sa=X&ved=2ahUKEwjT6omug_7qAhWLSH0KHQmhBooQ9RcwAHoECAUQCA\n\n3.	Nama tempat fotokopi	: Salsabila - 99\nAlamat			: Jl. Tubagus Ismail Raya No.44, Sekeloa, Kecamatan Coblong, Kota Bandung, Jawa Barat 40134\nYang dijual		: Jasa fotokopi, print foto, ATK, jilid ring, laminating\nJam operasi		: 08.00-20.00 WIB\nLink google maps	: https://www.google.com/maps/dir/-6.2469977,106.8532384/Salsabila+-+99,+Jl.+Tubagus+Ismail+Raya+No.44,+Sekeloa,+Kecamatan+Coblong,+Kota+Bandung,+Jawa+Barat+40134/@-6.5219234,106.6492494,9z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x2e68e6ffa53ba211:0x295e62cb6d62dcaa!2m2!1d107.6192492!2d-6.8848563"))
    elif (msg=='cari') or (msg=='Cari'):
                line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Silakan masukan ANGKA atau NAMA TEMPAT sesuai pilihan dibawah ini\n\nDalam ITB\n1. GKUB\n2. Labtek 5\n3. GKUT\n4. Labtek 8\n5. Labtek biru\n6. SBM\n7. ITB Press\n8. Gedung PAU\n\nLuar ITB\n9. Cisitu\n10. Dipatiukur(DU)\n11. Tubagus Ismail (Tubis)\n\nTerimakasih sudah menggunakan layanan chatbot ini"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Mohon maaf, message belum dapat dimengerti\nSilakan masukan ANGKA atau NAMA TEMPAT sesuai pilihan dibawah ini\n\nDalam ITB\n1. GKUB\n2. Labtek V\n3. GKUT\n4. Labtek VIII\n5. Labtek biru\n6. SBM\n7. ITB Press\n8. Gedung PAU\n\nLuar ITB\n9. Cisitu\n10. Dipatiukur(DU)\n11. Tubagus Ismail (Tubis)\n\nTerimakasih sudah menggunakan layanan chatbot ini"))
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
