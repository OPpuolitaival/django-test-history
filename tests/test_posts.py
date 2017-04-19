"""
Easy script for testing purpose
"""
from urllib import request
import json

for i in range(10):
    data = dict()
    data["job_name"] = "Test job _{}".format(i)
    data["job_url"] = "#".format(i)
    data["test_results"] = [
        {
            'case_name': 'test_xx',
            'duration': '12'
        },
        {
            'case_name': 'test_yy',
            'duration': '13'
        }
    ]

    req = request.Request(
        "http://127.0.0.1:8000/api/",
        data=json.dumps(data).encode('utf8'),
        headers={'content-type': 'application/json'}
    )
    resp = request.urlopen(req)
