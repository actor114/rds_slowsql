import json
import datetime
import os,sys
from rds_allsql import get_all_sql
PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, PROJECT_ROOT)


if __name__ == "__main__":
    now = datetime.datetime.now()
    new_time = now + datetime.timedelta(hours=-8)
    start_time = now + datetime.timedelta(hours=-8, minutes=-5)
    _format = '%Y-%m-%dT%H:%M:%SZ'
    start_time_str = start_time.strftime(_format)
    end_time_str = new_time.strftime(_format)
    allsql = get_all_sql(start_time_str, end_time_str)

    trs = json.loads(allsql)['Items']['SQLRecord']
    new_list = []
    for item in trs:
        try:
            ExecuteTime,sqltext,DBName,TotalExecutionTimes = \
                item.get("ExecuteTime"),\
                item.get("SQLText"),\
                item.get("DBName"), \
                item.get("TotalExecutionTimes")

            sqllist = [ExecuteTime,sqltext,DBName,TotalExecutionTimes]
            new_list.append(sqllist)
        except Exception as e:
            print("all sql print finish....",e)

    print(new_list)

    with open('rdssql.txt', 'a') as f:
        for line in new_list:
            f.write(str(line) + '\n')
