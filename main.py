import json
import requests
import csv
import time

key = 'r5cIjFTH00ER48mmhYQpnsePgvTk6lAJ'
# incase need to load data from file
# with open('sampleJS.json') as f:
#   data = json.load(f)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


for major in range(10):
    for one in range(10):
        for two in range(10):
            for three in range(10):
                for four in range(10):
                    serial = 'sn88' + str(major) + '4' + str(one) + str(two) + str(three) + str(four)
                    print(serial)
                    api_url = 'https://tsdrapi.uspto.gov/ts/cd/casestatus/' + serial + '/info'
                    header = {'USPTO-API-KEY': key}
                    time.sleep(1)
                    response = requests.get(api_url, headers=header)
                    if response:
                        payload = response.json()
                        for data in payload['trademarks']:
                            print("serialNumber", data["status"]['serialNumber'])
                            if data["status"]['filingDate']:
                                print("filingDate", data["status"]['filingDate'])
                            # print(data["status"]['tm5StatusDesc'])
                            # print(data["status"]['tm5StatusDef'])
                            with open('output.csv', 'a') as writeFile:
                                writer = csv.writer(writeFile)
                                writer.writerow([
                                    data["status"]['serialNumber'],
                                    payload,
                                    data["status"]['tm5StatusDesc'],
                                    data["status"]['tm5StatusDef']
                                ])
                    else:
                        pass
