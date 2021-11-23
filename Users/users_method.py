# coding=utf-8
# 调用实例

# 返回用户的浏览历史记录
# UserMethod.view_history(userid)

# 返回用户的收藏记录
# UserMethod.view_mark()

# 用户添加作品至收藏,并返回更新后的收藏记录
# UerMethod.add_mark(userId, workId)

# 用户删除收藏作品，并返回更新后的收藏记录
# UserMethod.delete_mark(userId, workId)

# 用户浏览作品后添加至历史记录
# UserMethod.view_work(userId, workId)
from Users.user import User
from Works.Work import Work
import json


class UserMethod:

    def register(phoneNumber, userName, profilePicture = ''):
        # 插入用户信息
        user = User.insertUserInfo(userName, phoneNumber)
        return user
        # 注册用户

    def update_icon(userId, newProfilePicture):
        User.updateprofilePicture(userId, newProfilePicture)

    def update_username(phone, new_username):
        result = User.updateUserName(phone, new_username)
        return result

    def update_country(phone, new_country):
        pass

    def update_province():
        pass

    def update_city():
        pass

    def update_gender():
        pass

    def update_language():
        pass

    def view_work(userId, workId):
        # 添加用户历史浏览记录
        new_history = User.insertuserSearchRecord(userId, workId)
        # 仍需获取work信息
        print(type(new_history))
        return new_history
        # 浏览作品

    def publish_work():
        pass
        # 发布作品

    def view_history(userId):
        # 获取用户历史浏览记录
        result = User.getUserSearchRecord(userId)
        print(result)
        now_history = list()
        for work in result:
            uid = work.get("userId")
            print(uid)
            user = User.getSingleUserInfo(str(uid))
            print(user)
            username = user[0].get("userName")
            work["username"] = username
            now_history.append(work)
        return now_history
        # 查看历史

    def view_mark(UserId):
        # 获取用户收藏信息
        result = User.getuserMarks(UserId)
        print(result)
        now_marks = list()
        for work in result:
            uid = work.get("userId")
            print(uid)
            user = User.getSingleUserInfo(str(uid))
            print(user)
            username = user[0].get("userName")
            work["username"] = username
            now_marks.append(work)
        return now_marks
        # 查看收藏

    def delete_mark(userId, workId):
        # 删除用户收藏记录
        new_marks = User.deleteuserMarks(userId,workId)
        return new_marks
        # 删除收藏

    def delete_history(userId, workId):
        # 删除用户历史浏览记录
        new_history = User.deleteuserSearchRecord(userId, workId)
        return new_history
        # 删除历史

    def add_mark(userId, workId):
        # 添加用户收藏记录
        new_mark = User.insertuserMarks(userId,workId)
        return new_mark
        # 添加收藏
