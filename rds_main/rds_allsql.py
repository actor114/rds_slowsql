#!/usr/bin/env python
#coding=utf-8
#pip3 install aliyun-python-sdk-core
#pip3  install -i https://pypi.douban.com/simple aliyun-python-sdk-core
##pip3  install -i https://pypi.douban.com/simple aliyun-python-sdk-rds
#pip install aliyun-python-sdk-core -i https://pypi.douban.com/simple

from aliyunsdkcore.client import AcsClient
from aliyunsdkrds.request.v20140815.DescribeSQLLogRecordsRequest import DescribeSQLLogRecordsRequest
config_all = dict(
    accessKeyId="LTAI2Eb7I2wbO1N3",
    accessSecret="VNjtyoXhn6wW5z22MOCtgyhbXnXNfA",
    location="cn-hangzhou",
)
accessKeyId = config_all.get("accessKeyId")
accessSecret = config_all.get("accessSecret")
location = config_all.get("location")

client = AcsClient(accessKeyId, accessSecret, location)

request = DescribeSQLLogRecordsRequest()
request.set_accept_format('json')


def get_all_sql(start_time="2019-04-19T04:00:00Z", end_time="2019-04-19T04:15:00Z"):
    """
    设置开始时间和结束时间'
    :param start_time:
    :param end_time:
    :return:
    """
    request.set_StartTime(start_time)
    request.set_EndTime(end_time)


    '''设置rds数据库实例'''
    request.set_DBInstanceId("rm-bp14nh2kezk95125d")

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    # print(str(response, encoding='utf-8'))
    print(str(response))

    rsp = str(response)
    return rsp

