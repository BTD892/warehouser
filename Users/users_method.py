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

    def phone2userid(phone):
        userid = User.translateToUserId(phone)
        return userid

    def update_icon(phone, newProfilePicture):
        userId = User.translateToUserId(phone)
        result = User.updateprofilePicture(str(userId), newProfilePicture)
        return result

    def update_username(phone, new_username):
        userId = User.translateToUserId(phone)
        result = User.updateUserName(str(userId), new_username)
        return result

    def update_country(phone, new_country):
        userId = User.translateToUserId(phone)
        result = User.updateUserCountry(str(userId), new_country)
        return result

    def update_province(phone, new_province):
        userId = User.translateToUserId(phone)
        result = User.updateUserProvince(str(userId), new_province)
        return result

    def update_city(phone, new_city):
        userId = User.translateToUserId(phone)
        result = User.updateUserCity(str(userId), new_city)
        return result

    def update_gender(phone, new_gender):
        userId = User.translateToUserId(phone)
        result = User.updateUserGender(str(userId), new_gender)
        return result

    def update_language(phone, new_language):
        userId = User.translateToUserId(phone)
        result = User.updateUserLanguage(str(userId), new_language)
        return result

    def view_work(phone, workId):
        # 添加用户历史浏览记录
        userId = User.translateToUserId(phone)
        new_history = User.insertuserSearchRecord(str(userId), str(workId))
        # 仍需获取work信息
        return new_history
        # 浏览作品

    def add_marks(phone, workid):
        userId = User.translateToUserId(phone)
        result = User.insertuserMarks(str(userId), str(workid))
        return result

    def delete_marks(phone, workid):
        userId = User.translateToUserId(phone)
        result = User.deleteuserMarks(str(userId), str(workid))
        return result

    def publish_work():
        pass
        # 发布作品

    def view_history(userId):
        # 获取用户历史浏览记录
        result = User.getUserSearchRecord(userId)
        now_history = list()
        if result is None:
            return now_history
        for work in result:
            uid = work.get("userId")
            user = User.getSingleUserInfo(str(uid))
            username = user[0].get("userName")
            work["author"] = username
            now_history.append(work)
        return now_history
        # 查看历史

    def view_mark(userId):
        # 获取用户收藏信息
        result = User.getUserSearchRecord(userId)
        now_marks = list()
        if result is None:
            return now_marks
        for work in result:
            uid = work.get("userId")
            user = User.getSingleUserInfo(str(uid))
            username = user[0].get("userName")
            work["author"] = username
            now_marks.append(work)
        return now_marks
        # 查看收藏

    def delete_mark(phone, workId):
        # 删除用户收藏记录
        userId = User.translateToUserId(phone)
        new_marks = User.deleteuserMarks(userId,workId)
        return new_marks
        # 删除收藏

    def delete_history(userId, workId):
        # 删除用户历史浏览记录
        userId = User.translateToUserId(phone)
        new_history = User.deleteuserSearchRecord(userId, workId)
        return new_history
        # 删除历史

    def clear_history(phone):
        userId = User.translateToUserId(phone)
        new_history = User.clearuserSearchRecord(userId)
        return new_history

    def add_mark(phone, workId):
        # 添加用户收藏记录
        userId = User.translateToUserId(phone)
        new_mark = User.insertuserMarks(userId,workId)
        return new_mark
        # 添加收藏
