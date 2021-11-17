from Works.webport import translate
import random
from Work import Work
from WorkComment import WorkComment


class WorksMethod:

    def delete_work(self, workid):
        result = Work.deleteWork(workid)
        return result

    def get_random_work(self):
        # 先获取一个作品id，再通过作品id获取作品信息
        tail = len(Work.getWorkInfo())
        work_id = random.randint(1, tail)
        result = Work.getSingleWorkInfo(work_id)
        return result

        # 获取推送文

    def make_comment(self, workid):
        # 获取随机数
        score = random.randint()
        # 将分数和id存入表中
        result = WorkComment.insertWorkComment(workid, score)
        return result
        # 给对应作品评分，并存入数据库中

    def search_work(self, workid):
        result = Work.getSingleWorkInfo(workid)
        return result
        # 搜索作品

    # 插入作品
    def publish_public_work(self,workName, workContent, workType = ""):
        results = Work.insertWork(workName, workContent, workType)
        result = results[len(results)-1]
        return result['workId']


class AudioWorkMethod(WorksMethod):
    def translate_work(self, audiofile):
        result = translate(audiofile)
        return result


class ArticleWorkMethod(WorksMethod):
    def get_work_length(self):
        pass
