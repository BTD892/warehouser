# coding=utf-8
import json
import urllib


def get_score(text):
    '''
    请求百度AI DNN语言模型，判断语句的通顺度
    '''
    assess_token = '24.5eedc404bc1507860e6d02f745f35ca6.2592000.1640162812.282335-25210626'
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn?access_token=' + str(assess_token)
    data = {"text": text}
    data = json.dumps(data).encode('GBK')
    request = urllib.request.Request(url, data)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request).read()
    result = str(response, encoding="gbk")
    f_result = json.loads(result)
    print(f_result)
    ff_result = f_result.get("ppl")
    # 可以自定义想要的结果
    #     filter_str = re.compile('ppl": (.*)')
    #     value = re.findall(filter_str,str(response))
    #     return float(str(value)[2:-4])
    return ff_result