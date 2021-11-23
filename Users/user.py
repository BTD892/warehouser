# coding =  utf-8
# 使用样例

# 查找单个用户的信息
# JSON OK
# User.getSingleUserInfo(userId)

# 查找全部用户信息
# JSON OK
# User.getUserInfo()

# 插入用户信息
# JSON OK
# User.insertUserInfo(userId,phoneNumber,userName,profilePicture = '',userMarks = '',
# userWorks = '',userSearchRecord = '',userPrefer=''):

# 更换用户头像
# JSON OK
# User.updateprofilePicture(userId,newProfilePicture)

# 更换用户名
# JSON OK
# User.updateUserName(userId,newUserName)

# 更换用户手机号码
# JSON OK
# User.updatephoneNumber(userId,newphoneNumber)

# 获取用户收藏信息
# JSON OK
# User.getuserMarks(userId)

# 添加用户收藏记录
# JSON OK
# User.insertuserMarks(userId,workId)

# 删除用户收藏记录
# JSON OK
# User.deleteuserMarks(userId,workId)

# 获取用户历史浏览记录
# JSON OK
# User.getUserSearchRecord(userId)

# 添加用户历史浏览记录
# JSON OK
# User.insertuserSearchRecord(userId,workId)

# 删除用户历史浏览记录
# JSON OK
# User.deleteuserSearchRecord(userId, workId)

# 获取用户喜好
# JSON OK
# User.getuserPrefer(userId)

# 添加用户喜好
# JSON OK
# User.insertuserPrefer(userId,typeId)

# 删除用户喜好
# JSON OK
# User.deleteuserPrefer(userId,typeId)

import pymysql
import json

from Type.Type import Type
from Works.Work import Work

class User:

    # 获取单个用户信息
    def getSingleUserInfo(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();

        sql = "SELECT * FROM User WHERE UserId = \"" + userId +"\";";
        try:
            # 执行SQL语句
            cursor.execute(sql),
            # 获取所有记录列表
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            results = results[0]
            jsonData = []
            result = {}
            result['userId'] = results[0]
            result['phoneNumber'] = results[1]
            result['userName'] = results[2]
            result['profileName'] = results[3]
            result['userMarks'] = User.getuserMarks(userId)
            result['userWorks'] = Work.getUserWork(userId)
            result['userSearchRecord'] = User.getUserSearchRecord(userId)
            result['userPrefer'] = User.getuserPrefer(userId)
            print
            u'转换为列表字典的原始数据：', jsonData
            jsonData.append(result)
            return jsonData
        except Exception as e:
            print(e)
            return False
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 获取所有用户信息
    def getUserInfo():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM User";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 获取所有用户信息
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result['userId'] = row[0]
                result['phoneNumber'] = row[1]
                result['userName'] = row[2]
                result['profileName'] = row[3]
                result['userMarks'] = row[4]
                result['userWorks'] = row[5]
                result['userSearchRecord'] = row[6]
                result['userPrefer'] = row[7]
                print
                u'转换为列表字典的原始数据：', jsonData
                jsonData.append(result)
            return jsonData
        except:
            return False
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 插入用户信息
    def insertUserInfo(userName,phoneNumber,profilePicture = '',userMarks = None,userWorks = None,userSearchRecord = None,userPrefer=None):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();

        sql =  "INSERT INTO User(userName,phoneNumber,profilePicture,userMarks,userWorks,userSearchRecord,userPrefer) \
        VALUES('%s','%s','%s','%s','%s','%s','%s')"% \
        (userName,phoneNumber,profilePicture,userMarks,userWorks,userSearchRecord,userPrefer);
        try:
            # 执行SQL语句
            cursor.execute(sql);
            # 执行sql语句
            conn.commit();
            cursor.close()
            conn.close()
            results = User.getUserInfo()
            return results
        except:
            return False

    # 更换用户头像
    def updateprofilePicture(userId,newProfilePicture):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET profilePicture = \"" + newProfilePicture + "\" WHERE userId = \"" + userId + "\";";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行mysql语句
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getSingleUserInfo(userId)
            return results
        except:
            return False

    # 更换用户名
    def updateUserName(userId,newUserName):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userName = \""+newUserName+"\""+"WHERE userId = \"" + userId + "\";";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getSingleUserInfo(userId)
            return results
        except:
            print("Error: unable to update userName")

    # 更换用户手机号码
    def updatephoneNumber(userId,newphoneNumber):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();

        sql = "UPDATE User SET phoneNumber = \""+newphoneNumber+"\""+" WHERE userId = \"" + userId + "\";";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            cursor.close()
            conn.close()
            result = User.getSingleUserInfo(userId)
            return result
        except:
            return False

    # 查找用户收藏记录
    def getuserMarks(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT userMarks FROM User WHERE userId = \""+userId+"\";";

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            for row in result:
                userMarks = row[0]
            userMarks = userMarks.split(",")
            for i in userMarks:
                if i == "None":
                    userMarks.remove(i)
            jsonData = []
            for i in userMarks:
                singleWork = {}
                singleWork["workId"] = i
                singleWork["workName"] = Work.getWorkName(i)
                singleWork["workContent"] = Work.getWorkContent(i)
                singleWork["workType"] = Work.getWorkTypeName(i)
                singleWork["userId"] = Work.getWorkAuthor(i)
                jsonData.append(singleWork)
            return jsonData
        except:
            return False
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    def getuserMarks_1(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT userMarks FROM User WHERE userId = \""+userId+"\";";

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            for row in result:
                userMarks = row[0]
            userMarks = userMarks.split(",")
            for i in userMarks:
                if i == "None":
                    userMarks.remove(i)
            return userMarks
        except:
            return False

    # 添加用户收藏记录
    def insertuserMarks(userId,workId):
        userMarks = User.getuserMarks_1(userId)
        print(userMarks)
        userMarks.append(workId)
        print(userMarks)
        str1 = ",".join(userMarks)
        print(str1)
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userMarks = \""+str1+"\" WHERE userId = \""+userId+"\";";
        try:
            cursor.execute(sql)
            conn.commit();
            cursor.close()
            conn.close()
            results = User.getuserMarks(userId)
            return results
        except:
            print("Error: unable to update userMarks")

    # 删除用户收藏记录
    def deleteuserMarks(userId,workId):
        userMarks = User.getuserMarks_1(userId)
        for i in userMarks:
            if i == workId:
                userMarks.remove(i)
        str1 = ",".join(userMarks)
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userMarks = \""+str1+"\" WHERE userId = \""+userId+"\";";
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getuserMarks(userId)
            return results
        except:
            print("Error: unable to update userMarks")

    # 获取用户历史浏览记录
    def getUserSearchRecord(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT userSearchRecord FROM User WHERE userId = \""+userId+"\"";
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            userSearchRecord = results[0]
            userSearchRecord = userSearchRecord[0]
            userSearchRecord = userSearchRecord.split(",")
            for i in userSearchRecord:
                if i == "None":
                    userSearchRecord.remove(i)
            jsonData = []
            for i in userSearchRecord:
                singleWork = {}
                singleWork["workId"] = i
                singleWork["workName"] = Work.getWorkName(i)
                singleWork["workContent"] = Work.getWorkContent(i)
                singleWork["workType"] = Work.getWorkTypeName(i)
                singleWork["userId"] = Work.getWorkAuthor(i)
                jsonData.append(singleWork)
            return jsonData
        except:
            return False
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    def getUserSearchRecord_1(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT userSearchRecord FROM User WHERE userId = \""+userId+"\"";
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            userSearchRecord = results[0]
            userSearchRecord = userSearchRecord[0]
            userSearchRecord = userSearchRecord.split(",")
            for i in userSearchRecord:
                if i == "None":
                    userSearchRecord.remove(i)
            return userSearchRecord
        except:
            print("Error:  unable to get userSearchRecord")

    # 添加用户历史浏览记录
    def insertuserSearchRecord(userId,workId):
        userSearchRecord = User.getUserSearchRecord_1(userId)
        userSearchRecord.append(workId)
        str1 = ",".join(userSearchRecord)
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userSearchRecord = \""+str1+"\" WHERE userId = \""+userId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getUserSearchRecord(userId)
            return results
        except:
            print("Error: unable to update userSearchRecord.")

    # 删除用户浏览记录
    def deleteuserSearchRecord(userId, workId):
        userSearchRecord = User.getUserSearchRecord_1(userId)
        for i in userSearchRecord:
            if i == workId:
                userSearchRecord.remove()
        str1 = ",".join(userSearchRecord)
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userSearchRecord = \"" + str1 + "\" WHERE userId = \"" + userId + "\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getUserSearchRecord(userId)
            return results
        except:
            return False

    # 查看用户喜好
    def getuserPrefer(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT userPrefer FROM User WHERE userId = \""+userId+"\";";
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            userPrefer = results[0]
            userPrefer = userPrefer[0]
            userPrefer = userPrefer.split(",")
            for i in userPrefer:
                if i == "None":
                    userPrefer.remove(i)
            jsonData = []
            for i in userPrefer:
                singleType = {}
                singleType["typeId"] = i
                singleType["typeName"] = Type.Type.getTypeName(i)
                jsonData.append(singleType)
            return jsonData
        except:
            return False

    def getuserPrefer_1(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT userPrefer FROM User WHERE userId = \""+userId+"\";";
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            userPrefer = results[0]
            userPrefer = userPrefer[0]
            userPrefer = userPrefer.split(",")
            for i in userPrefer:
                if i == "None":
                    userPrefer.remove(i)
            return userPrefer
        except:
            return False

    # 添加用户喜好
    def insertuserPrefer(userId,typeId):
        userPrefer = User.getuserPrefer_1(userId)
        userPrefer.append(typeId)
        str1 = ",".join(userPrefer)
        print(userPrefer)
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userPrefer = \""+str1+"\" WHERE userId = \""+userId+"\""
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getuserPrefer(userId)
            return results
        except:
            return False

    # 删除用户喜好
    def deleteuserPrefer(userId,typeId):
        userPrefer = User.getuserPrefer_1(userId)
        for i in userPrefer:
            if i == typeId:
                userPrefer.remove(i)
        str1 = ",".join(userPrefer)
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userPrefer = \""+str1+"\" WHERE userId = \""+userId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getuserPrefer(userId)
            return results
        except:
            return False

    # 删除用户信息
    def deleteuserInfo(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "DELETE FROM User WHERE userId = \""+userId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = User.getUserInfo()
            return results
        except:
            return False
