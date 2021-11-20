# coding = utf-8
from Works.webport import translate
import random
from Works.Work import Work
from Works.WorkComment import WorkComment


class WorksMethod:

    def delete_work(workid):
        result = Work.deleteWork(workid)
        return result

    def get_random_work():
        # 先获取一个作品id，再通过作品id获取作品信息
        tail = len(Work.getWorkInfo())
        work_id = random.randint(0, tail-1)
        result = Work.getSingleWorkInfo(str(10000+work_id))
        return result

        # 获取推送文

    def make_comment(workid):
        # 获取随机数
        score = random.randint(1, 100)
        # 将分数和id存入表中
        result = WorkComment.insertWorkComment(workid, str(score))
        return result
        # 给对应作品评分，并存入数据库中

    def search_work(workid):
        result = Work.getSingleWorkInfo(workid)
        return result
        # 搜索作品

    # 插入作品
    def publish_public_work(workName, workContent, userId, fileType, workType = ""):
        results = Work.insertWork(workName, workContent, userId, fileType, workType)
        print(results)
        result = results[len(results)-1]
        return result['workId']


class AudioWorkMethod(WorksMethod):
    def translate_work(audiofile):
        s = list(audiofile)
        length = len(s)
        s[length - 1] = 'm'
        s[length - 2] = 'c'
        s[length - 3] = 'p'
        new_path = ''.join(s)
        result = translate(audiofile, new_path)
        return result


class ArticleWorkMethod(WorksMethod):
    def get_work_length():
        pass
