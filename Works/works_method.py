# coding = utf-8
from Works.webport import translate
import random
from Users.user import User
from Works.Work import Work
from Works.WorkComment import WorkComment
from Works.makescore import get_score


class WorksMethod:

    def delete_work(workid):
        result = Work.deleteWork(workid)
        return result

    def get_random_text():
        # 先获取一个作品id，再通过作品id获取作品信息
        tail = Work.getTextcnt()
        work_id = random.randint(0, tail-1)
        work_name = Work.getWorkName(str(10000+work_id))
        work_authorid = Work.getWorkAuthor(str(10000+work_id))
        work_authorname = User.getUsername(str(work_authorid))
        result = dict()
        result["name"] = work_name
        result["id"] = 10000+work_id
        result["author"] = work_authorname
        return result
        # 获取推送文

    def get_work_content(workid):
        work = Work.getSingleWorkInfo(str(workid))
        return work

    def get_Audiowork(cnt):
        result = list()
        tail = Work.getAudiocnt()
        while cnt>0:
            work_id = random.randint(0, tail-1)
            work = Work.getSingleWorkInfo(str(20000+work_id))[0]
            author_id = work["userId"]
            author_name = User.getUsername(str(author_id))
            work["author"] = author_name
            result.append(work)
            cnt -= 1
        return result

    def make_comment(text):
        # 获取随机数
        score = get_score(text)
        # 将分数和id存入表中
        return score
        # 给对应作品评分，并存入数据库中

    def search_work(workid):
        result = Work.getSingleWorkInfo(workid)
        return result
        # 搜索作品

    # 插入作品
    def publish_public_work(workName, workContent, userId, fileType, workType = ""):
        results = Work.insertWork(workName, workContent, userId, fileType, workType)
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
