from flask import Flask,request,abort,send_file,render_template
import requests
import json
import threading
import time

Channel_secret = 'Input_Channel_secret'
Channel_access_token = 'Input_Channel_access_token'
Confirmed = ""
Recovered = ""
Deaths = ""
NewConfirmed = ""
NewRecovered = ""
NewDeaths = ""
UpdateDate = ""


app = Flask(__name__,template_folder="templates")


@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        print("----------")
        print("payload ->", payload)
        print("----------")

        Reply_token = payload['events'][0]['replyToken']
        print("Reply_token ", Reply_token)

        type_message = payload['events'][0]['message']['type']
        print("type_message ", type_message)

        messageID = payload['events'][0]['message']['id']
        print("messageID ", messageID)

        if type_message == 'text':
            message = payload['events'][0]['message']['text']
            if "test" in message:
                Reply_messasge = 'ทดสอบ'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "ทดสอบ" in message:
                Reply_messasge = 'ทดสอบ'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "ok" in message:
                Reply_messasge = 'ok'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "Dev" in message:
                Reply_messasge = 'Dev by Sarawut.'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "dev" in message:
                Reply_messasge = 'Dev by Sarawut.'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "hi" in message:
                Reply_messasge = 'สวัสดี'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "สวัสดี" in message:
                Reply_messasge = 'สวัสดี'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "Hi" in message:
                Reply_messasge = 'สวัสดี'
                ReplyMessage(Reply_token, Reply_messasge)
            elif "richmenu" in message:
                ReplyMessageRichmenu()
            elif "flex" in message:
                Reply_messasge = 'Hello'
                ReplyMessageFlex(Reply_token, Reply_messasge)
            elif "bubble" in message:
                Reply_messasge = 'Hello'
                ReplyMessageBubble(Reply_token, Reply_messasge)
            elif "carousel" in message:
                ReplyMessageCarousel(Reply_token)
            elif "img" in message:
                ReplyMessageImg(Reply_token)
            else:
                Reply_messasge = 'Bot ยังไม่สามารถตอบกลับได้ในขณะนี้ ขอบคุณที่เข้ามาคุยกันน่ะครับ'
                ReplyMessage(Reply_token, Reply_messasge)

        if type_message == 'image':
            Reply_messasge = 'test image'
            ReplyMessage(Reply_token, Reply_messasge)

        if type_message == 'video':
            Reply_messasge = 'test video'
            ReplyMessage(Reply_token, Reply_messasge)

        if type_message == 'audio':
            Reply_messasge = 'test audio'
            ReplyMessage(Reply_token, Reply_messasge)

        if type_message == 'file':
            Reply_messasge = 'test file'
            ReplyMessage(Reply_token, Reply_messasge)

        if type_message == 'location':
            Reply_messasge = 'test location'
            ReplyMessage(Reply_token, Reply_messasge)

        return request.json, 200

    elif request.method == 'GET':
        return 'this is method GET!!!', 200

    else:
        abort(400)


@app.route('/')
def hello():
    return 'Hello World', 200


@app.route("/covid19")
def covid19():
    global Confirmed, Recovered, Deaths, NewConfirmed, NewRecovered, NewDeaths, UpdateDate
    ConfirmedH = str(Confirmed)
    RecoveredH = str(Recovered)
    DeathsH = str(Deaths)
    NewConfirmedH = str(NewConfirmed)
    NewRecoveredH = str(NewRecovered)
    NewDeathsH = str(NewDeaths)
    UpdateDateH = "ข้อมูลอัพเดทเมื่อ " + str(UpdateDate)
    return render_template('covid-19.html', version="Bata version 0.1 ", data1=ConfirmedH, data2=RecoveredH, data3=DeathsH, data4=NewConfirmedH, data5=NewRecoveredH, data6=NewDeathsH, data7=UpdateDateH)


def ReplyMessage(Reply_token, TextMessage):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "text",
            "text": TextMessage
        }]
    }

    data = json.dumps(data)  ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200


def ReplyMessageImg(Reply_token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token,
        "type": "message",
        "mode": "active",
        "timestamp": 1462629479859,
        "source": {
            "type": "user",
            "userId": "U1426a8a1f449359b117f7b9274f3b6b3"
        },
        "message": {
            "id": "325708",
            "type": "image",
            "originalContentUrl": "https://linefriends.com/img/bangolufsen/img_og.jpg",
            "previewImageUrl": "https://linefriends.com/img/bangolufsen/img_og.jpg",
            "contentProvider": {
                "type": "line"
            }
        }
    }

    data = json.dumps(data)  ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200


def ReplyMessageFlex(Reply_token, TextMessage):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "flex",
            "altText": "this is a flex message",
            "contents": {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": TextMessage
                        }
                    ]
                }
            }
        }],
    }

    data = json.dumps(data)  ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200


def ReplyMessageCarousel(Reply_token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "carousel",
                "contents": [
                    {
                        "type": "bubble",
                        "direction": "ltr",
                        "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "OK 1",
                                        "text": "ok"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "type": "bubble",
                        "direction": "ltr",
                        "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "OK 2",
                                        "text": "ทดสอบ"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "type": "bubble",
                        "direction": "ltr",
                        "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "OK 3",
                                        "text": "test"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }],
    }

    data = json.dumps(data)  ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200


def ReplyMessageBubble(Reply_token, TextMessage):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token,
        "messages": [
            {
                "type": "flex",
                "altText": "Flex Message",
                "contents": {
                    "type": "bubble",
                    "direction": "ltr",
                    "footer": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "OK",
                                    "text": "ok"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }

    data = json.dumps(data)  ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200


def ReplyMessageRichmenu():
    LINE_API = 'https://api.line.me/v2/bot/richmenu'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "size": {
            "width": 2500,
            "height": 1686
        },
        "selected": False,
        "name": "LINE Developers Info",
        "chatBarText": "Tap to open",
        "areas": [
            {
                "bounds": {
                    "x": 34,
                    "y": 24,
                    "width": 169,
                    "height": 193
                },
                "action": {
                    "type": "uri",
                    "uri": "https://developers.line.biz/en/news/"
                }
            },
            {
                "bounds": {
                    "x": 229,
                    "y": 24,
                    "width": 207,
                    "height": 193
                },
                "action": {
                    "type": "uri",
                    "uri": "https://www.line-community.me/"
                }
            },
            {
                "bounds": {
                    "x": 461,
                    "y": 24,
                    "width": 173,
                    "height": 193
                },
                "action": {
                    "type": "flex",
                    "altText": "LINE Developers Site More Options",
                    "contents": {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "devSiteImageUrl",
                            "size": "full",
                            "margin": "none",
                            "gravity": "top",
                            "aspectRatio": "1200:630"
                        }
                    }
                }
            }
        ]
    }

    data = json.dumps(data)  ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200



def thread_callback1():
    global Confirmed,Recovered,Deaths,NewConfirmed,NewRecovered,NewDeaths,UpdateDate
    while True:
        URL_API = 'https://covid19.th-stat.com/api/open/today'
        r = requests.get(url=URL_API)
        data = r.json()

        Confirmed = data["Confirmed"]
        Recovered = data["Recovered"]
        Deaths = data["Deaths"]
        NewConfirmed = data["NewConfirmed"]
        NewRecovered = data["NewRecovered"]
        NewDeaths = data["NewDeaths"]
        UpdateDate = data["UpdateDate"]

        # print(data)
        time.sleep(60)


thr1 = threading.Thread(target=thread_callback1)
thr1.start()



if __name__ == '__main__':
    app.run(port=200)     #localhost:200/
    # app.run(debug=True)     #localhost:5000/