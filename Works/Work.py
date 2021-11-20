# coding=utf-8
# 调用实例

# 添加作品信息
# JSON OK
# Work.insertWork(workName,workContent,workType = "")

# 获取单个作品信息
# JSON OK
# Work.getSingleWorkInfo(workId)

# 获取全部作品信息
# JSON OK
# Work.getWorkInfo()

# 更新作品名称
# JSON OK
# Work.updateWorkName(workId,newWorkName)

# 更新作品内容
# JSON OK
# Work.updateWorkContent(workId,newWorkContent)

# 更新作品分类
# JSON OK
# Work.updateWorkType(workId,newWorkType)

# 删除作品信息
# JSON OK
# Work.deleteWork(workId)

# 获取用户的作品
# JSON OK
# Work.getUserWork(workId)

import pymysql
import Type
from Works.WorkComment import WorkComment
import json


class Work:

    # 获取单个作品信息
    def getSingleWorkInfo(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work WHERE WorkId = \"" + workId + "\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            results = results[0]
            result = {}
            jsonData = []
            result["workId"] = results[0]
            result["workName"] = results[1]
            result["workContent"] = results[2]
            result["workType"] = Work.getWorkTypeName(workId)
            result["userId"] = results[4]
            result["fileType"] = results[5]
            jsonData.append(result)
            return jsonData
        except:
            return False
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 获取全部作品
    def getWorkInfo():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result["workId"] = row[0]
                result["workName"] = row[1]
                result["workContent"] = row[2]
                result["workType"] = row[3]
                result["userId"] = row[4]
                result["fileType"] = row[5]
                jsonData.append(result)
            print(jsonData)
            return jsonData
        except:
            return False
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 添加作品信息
    def insertWork(workName,workContent,userId,fileType,workType = ""):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "INSERT INTO Work(workName,workContent,userId,workType,fileType) VALUES('%s','%s','%s','%s','%s');"% \
        (workName,workContent,userId,workType,fileType);
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getWorkInfo()
            return results
        except Exception as e:
            print(e)
            return False

    # 更改作品名称
    def updateWorkName(workId,newWorkName):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workName = \""+newWorkName+"\" WHERE workId = \""+workId+"\";";
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getSingleWorkInfo(workId)
            return results
        except:
            return False

    # 更改作品内容
    def updateWorkContent(workId,newWorkContent):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workContent = \""+newWorkContent+"\" WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getSingleWorkInfo(workId)
            return results
        except:
            return False

    # 更改作品分类
    def updateWorkType(workId,newWorkType):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workType = \""+newWorkType+"\" WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getSingleWorkInfo(workId)
            return results
        except:
            return False

    # 删除作品
    def deleteWork(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "DELETE FROM Work WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getWorkInfo()
            return results
        except:
            return False

    # 获取用户的作品
    def getUserWork(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work WHERE userId = \""+userId+"\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result["workId"] = row[0]
                result["workName"] = row[1]
                result["workContent"] = row[2]
                result["workType"] = row[3]
                result["userId"] = row[4]
                jsonData.append(result)
            return jsonData
        except:
            return False

    # 获取作品名
    def getWorkName(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT workName FROM Work WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            results = results[0]
            results = results[0]
            return results
        except:
            return False

    # 获取作品内容
    def getWorkContent(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT workContent FROM Work WHERE workId = \"" + workId + "\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            results = results[0]
            results = results[0]
            return results
        except:
            return False

    # 获取作品类名
    def getWorkTypeName(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT workType FROM Work WHERE workId = \"" + workId + "\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            typeId = results[0]
            typeId = typeId[0]
            typeName = Type.Type.getTypeName(typeId)
            return typeName
        except:
            return False


if __name__ == "__main__":
    Work.insertWork("test1", "abcdefghijklmn", "2", "1")
