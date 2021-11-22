# coding=utf-8
from flask import Flask, redirect, request, jsonify, session, send_from_directory
from Works.works_method import WorksMethod, AudioWorkMethod, ArticleWorkMethod
from Users.users_method import UserMethod
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'


@app.route('/alwaysRight/reg', methods=["POST"])  # need put in
def register():
    getData = request.get_json()
    phone = getData.get('phone')
    username = getData.get('username')
    session['phone']=phone
    result = UserMethod.register(phone, username)
    print(result)
    return jsonify(msg="user Phone Put in !")


@app.route('/alwaysRight/setInfoByUserId', methods=["POST"])  # need put in
def setInfoByUserId():
    ingore = 1
    getData = request.get_json()
    phone = session['phone']
    nickName = getData.get("nickName")
    country = getData.get("country")
    province = getData.get("province")
    city = getData.get("city")
    gender = getData.get("gender")
    language = getData.get("language")
    if nickName:
        UserMethod.update_username(phone, nickName)
    if country:
        ingore = 1
    if province:
        ingore = 1
    if city:
        ingore = 1
    if gender:
        ingore = 1
    if language:
        ingore = 1

    return jsonify(msg="User Info put in !")


@app.route('/alwaysRight/logIn', methods=["POST"])
def login():
    getData = request.get_json()
    phone = getData.get("phone")
    session['phone'] = phone
    return jsonify(msg="session login ! ")


@app.route('/alwaysRight/logOut', methods=["POST"])
def logOut():
    session.clear()
    return jsonify(msg="session erase ! ")


@app.route('/alwaysRight/checkLogin', methods=["POST"])
def checkLogin():
    message = 1
    phone = session['phone']
    if not phone:
        message = 0

    return jsonify(msg=message)


@app.route('/alwaysRight/getRandomWork', methods=["POST"])
def getRandomWork():
    getWork = WorksMethod.get_random_work() # get random TotalWork
    # getWork = WorkMethod.get_random_work()
    return jsonify(randomWork=getWork)


# @app.route('/alwaysRight/getUserInfo', methods=["POST"])
# def getUserData():
#     func()
#
#     return jsonify()
@app.route('/alwaysRight/getUserHistory', methods=["POST"])
def getUserHistory():
    getData = request.get_json()
    id = getData.get("id")
    userData = UserMethod.view_history(str(id))
    return jsonify(randomWork=userData)


@app.route('/alwaysRight/getUserLikeById', methods=["POST"])
def getUserLikeById():
    getData = request.get_json()
    print(getData)
    id = getData.get("id")
    userData = UserMethod.view_mark(id)
    return jsonify(randomWork=userData)


# @app.route('/alwaysRight/changeUserIcon')
# def changeicon():
#     getData = request.get_json()
#     filePath = getData.get("filePath")
@app.route('/alwaysRight/saveUserIcon')  # need put in
def saveUserIcon():
    Icon = request.files.get('Icon')
    id = session.get('phone')
    path = ".\\static\\Icon\\"
    IconName = Icon.filename
    filePath = path + IconName
    Icon.save(filePath)
    return jsonify(msg='save !')


@app.route('/alwaysRight/getSomethingByUrl', methods=["POST"])  # need test
def getSomethingByUrl():
    getData = request.get_json()
    url = getData.get("url")

    return send_from_directory(url,  'black-diamond-suit_2666.png')


@app.route('/alwaysRight/uploadAudio4Score', methods=["POST"])
def upload4Score():
    audio = request.files.get('audio')
    path = ".\\static\\audio\\"
    audioName = audio.filename
    filePath = path + audioName
    userId = "2"
    print(type(userId))
    # 插入时必须有用户id
    audio.save(filePath)
    print(audioName)
    fileType = "0"
    # thisAudioId = func()  # save id
    # thisAudioId2Score = func()  # save score
    thisAudioId = WorksMethod.publish_public_work(audioName, filePath, userId, fileType)
    text = AudioWorkMethod.translate_work(filePath)
    score = WorksMethod.make_comment(str(thisAudioId), text)
    if score <= 500:
        thisAudioId2Score = "SSS"
    elif 500 < score <= 1000:
        thisAudioId2Score = "SS"
    data = {
        'id': thisAudioId,
        'score': thisAudioId2Score
    }
    return jsonify(data)


@app.route('/alwaysRight/uploadAudio4text', methods=["POST"])
def upload4text():
    audio = request.files.get('audio')
    path = ".\\static\\audio\\"
    audioName = audio.filename
    filePath = path + audioName
    userId = "2"
    fileType = "0"
    # 插入时必须得有用户Id
    print(filePath)
    audio.save(filePath)
    thisAudioId = WorksMethod.publish_public_work(audioName, filePath, userId, fileType)  # save id
    thisAudioId2Text = AudioWorkMethod.translate_work(filePath)  # save score
    # WorkMethod.make_score(id)
    data = {
        'id': thisAudioId,
        'text': thisAudioId2Text
    }
    return jsonify(data)


# def func():
#     return 1
#
#
# @app.route('/alwaysRight/dialect2Mandarin', methods=["POST"])
# def trans():
#     audio = request.files.get('audio')
#     res = func(audio)
#
#     return jsonify(data=res)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
