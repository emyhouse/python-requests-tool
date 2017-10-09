# coding =utf-8
import os
import sys
project_path = os.path.abspath(".")
sys.path.append(project_path)
reload(sys)
sys.setdefaultencoding('utf8')
from requesttool.scripts.client import RequestClient
from requesttool.auth import settings 

if __name__ == "__main__":
    rc = RequestClient(settings.request_url, settings.auth_token)
    rst = rc.get("/api/v2/vm")
    print(rst)

