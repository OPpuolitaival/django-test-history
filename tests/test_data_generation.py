"""
Idea is that this file execute randomly failing test cases and send results in rest-api
"""
import pytest
import os

this_folder = os.path.dirname(os.path.realpath(__file__))

params = list()
params.append('--junit-xml={}'.format(os.path.join(this_folder, 'result.xml')))
params.append('--junit-prefix=test.something')
params.append(os.path.join(this_folder, 'randomly_failing_tests.py'))

print(params)
pytest.main(params)

data = dict()

# Parse and send the file
import xml.etree.ElementTree as ET
import json

tree = ET.parse('result.xml')
root = tree.getroot()
data['suite'] = dict()
data['tests'] = list()
for name, value in root.items():
    data['suite'][name] = value

for test_case in root:
    temp = dict()
    for name, value in test_case.items():
        temp[name] = value
    for other in test_case:
        if 'failure' == other.tag:
            temp['stacktrace'] = str(other.text)
            temp['reason'] = str(other.attrib)
        else:
            temp[other.tag] = str(other.attrib)
    data['tests'].append(temp)

print(json.dumps(data, indent=2))


# TODO: Send file to the system
