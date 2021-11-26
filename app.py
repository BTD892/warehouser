# coding=utf-8
from flask import Flask, redirect, request, jsonify, session, send_from_directory,send_file
from Works.works_method import WorksMethod, AudioWorkMethod, ArticleWorkMethod
from Users.users_method import UserMethod
import os
import time
import wave
import contextlib

app = Flask(__name__)
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'


@app.route('/alwaysRight/reg', methods=["POST"])  # need put in
def register():
    getData = request.get_json()
    phone = getData.get('phone')
    username = getData.get('username')
    print(phone + "want to register")
    session['phone']=phone
    result = UserMethod.register(phone, username)
    if not result:
        return jsonify(msg="user Phone has Existed !")
    return jsonify(msg="user Phone Put in !")


@app.route('/alwaysRight/setInfoByUserId', methods=["POST"])  # need put in
def setInfoByUserId():
    print("Someone wanna set Information")
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
        UserMethod.update_country(phone, country)
    if province:
        UserMethod.update_province(phone, province)
    if city:
        UserMethod.update_city(phone, city)
    if gender:
        UserMethod.update_gender(phone, gender)
    if language:
        UserMethod.update_language(phone, language)
    return jsonify(msg="User Info put in !")


@app.route('/alwaysRight/logIn', methods=["POST"])
def login():
    getData = request.get_json()
    phone = getData.get("phone")
    print("Someone wanna login!!!")
    session['phone'] = phone
    return jsonify(msg="session login ! ")


@app.route('/alwaysRight/logOut', methods=["POST"])
def logOut():
    session.clear()
    print("Someone wanna logout!!!")
    return jsonify(msg="session erase ! ")


@app.route('/alwaysRight/checkLogin', methods=["POST"])
def checkLogin():
    message = 1
    print("Let's check login")
    if not bool(session):
        message = 0
    return jsonify(msg=message)


@app.route('/alwaysRight/getRandomTextId', methods=["POST"])
def getRandomTextId():
    getData = request.get_json()
    cnt = getData.get("cnt") # get random TotalWork
    # getWork = WorkMethod.get_random_work()
    cnt = int(cnt)
    getWork = list()
    while(cnt>0):
        work = WorksMethod.get_random_text()
        getWork.append(work)
        cnt -= 1
    print("Fetch Some WorkId!!!")
    return jsonify(randomWork=getWork)


@app.route('/alwaysRight/getRandomText', methods=["POST"])
def getRandomText():
    getData = request.get_json()
    workid = getData.get("workid")
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = session['phone']
    UserMethod.view_work(phone, workid)
    getWork = WorksMethod.get_random_text(workid)
    print("Fetch Some WorkContent!!!")
    return jsonify(randomWork=getWork)


@app.route('/alwaysRight/getRandomAudio', methods=["POST"])
def getRandomAudio():
    print("Someone wanna get Audio!!!")
    getData = request.get_json()
    cnt = getData.get("cnt")
    getWork = WorksMethod.get_Audiowork(int(cnt))
    return jsonify(randomWork=getWork)


@app.route('/alwaysRight/getAudioEvent',methods=["POST"])
def getAudioEvent():
    print("Knowing Someone has listened some audios!!!")
    getData = request.get_json()
    workid = getData.get("workid")
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = session['phone']
    UserMethod.view_work(phone, workid)
    return jsonify(msg="I have known that what you have listened")


# @app.route('/alwaysRight/getUserInfo', methods=["POST"])
# def getUserData():
#     func()
#     return jsonify()
@app.route('/alwaysRight/addMarks', methods=["POST"])
def addMarks():
    getData = request.get_json()
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = session['phone']
    workid = getData.get("workid")
    UserMethod.add_marks(phone, workid)
    return jsonify(msg="Mark Successfully")


@app.route('/alwaysRight/deleteMark', methods=["POST"])
def deleteMarks():
    getData = request.get_json()
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = session['phone']
    workid = getData.get("workid")
    UserMethod.add_marks(phone, workid)
    return jsonify(msg="Mark Successfully")


@app.route('/alwaysRight/deleteMark', methods=["POST"])
def deleteHistory():
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = session['phone']
    UserMethod.clear_history(phone)
    return jsonify(msg="Clear Successfully")


@app.route('/alwaysRight/getUserHistory', methods=["POST"])
def getUserHistory():
    getData = request.get_json()
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = getData.get("phone")
    id = UserMethod.phone2userid(phone)
    userData = UserMethod.view_history(str(id))
    print("Someone get History")
    return jsonify(history=userData)


@app.route('/alwaysRight/getUserLikeById', methods=["POST"])
def getUserLikeById():
    getData = request.get_json()
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = getData.get("phone")
    id = UserMethod.phone2userid(phone)
    userData = UserMethod.view_mark(str(id))
    print("Someone get Mark")
    return jsonify(Mark=userData)


# @app.route('/alwaysRight/changeUserIcon')
# def changeicon():
#     getData = request.get_json()
#     filePath = getData.get("filePath")
@app.route('/alwaysRight/saveUserIcon', methods=["POST"])  # need put in
def saveUserIcon():
    Icon = request.files.get('Icon')
    if not bool(session):
        return jsonify(msg="You haven't logined")
    phone = session.get('phone')
    path = os.getcwd()+"\\static\\Icon\\"
    IconName = Icon.filename
    filePath = path + IconName
    UserMethod.update_icon(phone, filePath)
    Icon.save(filePath)
    return jsonify(msg='save !')


@app.route('/alwaysRight/getSomethingByUrl', methods=["POST"])  # need test
def index():
    filePath = request.get_json().get("url")
    try:
        return send_file(filePath)
    except:
        return '<h1>该文件不存在或无法下载</h1>'


@app.route('/alwaysRight/uploadAudio4Score', methods=["POST"])
def upload4Score():
    print("Someone get Score")
    audio = request.files.get('audio')
    path = os.getcwd()+"\\static\\audio\\"
    audioName = audio.filename
    filePath = path + str(time.time()) + audioName
    audio.save(filePath)
    # thisAudioId = func()  # save id
    # thisAudioId2Score = func()  # save score
    # thisAudioId = WorksMethod.publish_public_work(audioName, filePath, userId, fileType)
    fname = '.\\static\\Audio\\mintest3.wav'
    with contextlib.closing(wave.open(fname, 'r')) as f:
        framse = f.getnframes()
        rate = f.getframerate()
        duration = framse / float(rate)
    text = AudioWorkMethod.translate_work(filePath)
    score = WorksMethod.make_comment(text)*0.5 + duration*10 + len(text)*10
    if score <= 500:
        thisAudioId2Score = "SSS"
    elif 500 < score <= 1000:
        thisAudioId2Score = "SS"
    elif 1000 < score <= 3000:
        thisAudioId2Score = "S"
    elif 3000 < score <= 10000:
        thisAudioId2Score = "A"
    else:
        thisAudioId2Score = "B"
    data = {
        'score': thisAudioId2Score
    }
    return jsonify(data)


@app.route('/alwaysRight/uploadAudio4text', methods=["POST"])
def upload4text():
    print("Someone get Text")
    audio = request.files.get('audio')
    path = os.getcwd()+"\\static\\audio\\"
    audioName = audio.filename
    filePath = path + str(time.time()) + audioName
    userId = "2"
    fileType = "0"
    # 插入时必须得有用户Id
    audio.save(filePath)
    # thisAudioId = WorksMethod.publish_public_work(audioName, filePath, userId, fileType)  # save id
    thisAudioId2Text = AudioWorkMethod.translate_work(filePath)  # save score
    # WorkMethod.make_score(id)
    data = {
        'text': thisAudioId2Text
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
