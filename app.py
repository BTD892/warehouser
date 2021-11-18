# coding=utf-8
from flask import Flask, redirect, request, jsonify
from Works.works_method import WorksMethod, AudioWorkMethod, ArticleWorkMethod
from Users.users_method import UserMethod
import os

app = Flask(__name__)


@app.route('/alwaysRight/reg', methods=["POST"])
def reg():
    getData = request.get_json()
    nickName = getData.get("nickName")
    country = getData.get("country")
    province = getData.get("province")
    city = getData.get("city")
    gender = getData.get("gender")
    language = getData.get("language")
    avatarUrl = getData.get("avatarUrl")

    userData = {
        'nickName': nickName,
        'country': country,
        'province': province,
        'city': city,
        'gender': gender,
        'language': language,

    }
    return jsonify(msg="ok")


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


@app.route('/alwaysRight/getUserLikeById', methods=["POST"])
def getUserLikeById():
    getData = request.get_json()
    print(getData)
    id = getData.get("id")
    userData = UserMethod.view_mark(id)

    return jsonify(randomWork=userData)


@app.route('/alwaysRight/uploadAudio4Score', methods=["POST"])
def upload4Score():
    audio = request.files.get('audio')
    path = ".\\static\\audio\\"
    audioName = audio.filename
    filePath = path + audioName
    userId = 2
    print(type(userId))
    # 插入时必须有用户id
    audio.save(filePath)
    print(audioName)
    # thisAudioId = func()  # save id
    # thisAudioId2Score = func()  # save score
    thisAudioId = WorksMethod.publish_public_work(audioName, filePath, userId)
    thisAudioId2Score = WorksMethod.make_comment(str(thisAudioId))
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
    userId = 2
    # 插入时必须得有用户Id
    print(filePath)
    audio.save(filePath)
    thisAudioId = WorksMethod.publish_public_work(audioName, filePath, userId)  # save id
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
