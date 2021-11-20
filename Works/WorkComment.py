# coding=utf-8
# 作品评分

# 调用实例

# 获取作品评分表
# WorkComment.getWorkComment()

# 获取作品评分
# WorkComment.getSingleWorkComment(workId)

# 添加作品评分
# WorkComment.insertWorkComment(workId,workScore)

# 删除作品评分
# WorkComment.deleteWorkComment(workId)

# 修改作品评分
# WorkComment.updateWorkComment(workId,workScore)

import pymysql
import json


class WorkComment:

    # 获取作品评分表
    def getWorkComment():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM WorkComment"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result['workId'] = row[0]
                result['workScore'] = row[1]
                jsonData.append(result)
        except:
            return False
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 获取作品评分
    def getSingleWorkComment(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT workScore FROM WorkComment WHERE workId = \""+workId+"\"";
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            results = results[0]
            workScore = results[0]
            return workScore
        except:
            print("Error: unable to fetchall userPrefer")
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 添加作品评分
    def insertWorkComment(workId,workScore):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "INSERT INTO WorkComment(workId,workScore) VALUES(\""+workId+"\",\""+workScore+"\")";
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = WorkComment.getWorkComment()
            return results
        except Exception as e:
            print(e)
            return False

    # 删除作品评分
    def deleteWorkComment(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "DELETE FROM WorkComment WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = WorkComment.getWorkComment(workId)
            return results
        except:
            return False

    # 修改作品评分
    def updateWorkComment(workId,workScore):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE WorkComment SET workScore = \""+workScore+"\" WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = WorkComment.getSingleWorkComment(workId)
            return results
        except:
            return False
