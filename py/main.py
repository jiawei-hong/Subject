from urllib.parse import *
import requests, csv

url = 'https://udb.moe.edu.tw/DetailReportList/%E5%AD%B8%E7%94%9F%E9%A1%9E/StatDepartmentRegistrationRate/Export'
headers = {
    'ASP.NET_SessionId=0qkq5icfv4beqybee3tppo03; _ga=GA1.3.373763083.1588929927; _gid=GA1.3.1580700545.1588929927; __RequestVerificationToken=Gjq6vfR97AYkYZcaNKrUBnq1zbpsVQhbB24O9ZtdTq2en2ZKIfFrEsN8gxZu4oJKcvJUIPSK812v1gH9EEsGvR8XGtNtmV5uTp65cOsKRAQ1; _gat=1',
}
query = 'FileType=csv&Parameter=%7B%22Year%22%3A%5B%5D%2C%22BuildType%22%3A%5B%5D%2C%22UniversityType%22%3A%5B%5D%2C%22UniversityList%22%3A%5B%5D%2C%22DepartmentName%22%3A%22%22%2C%22EduSystem%22%3A%5B%5D%2C%22PageSize%22%3A%2210%22%2C%22PageNumber%22%3A1%7D'
temp = query.split('&')
params = {
    'FileType': temp[0].split('=')[1],
    'Parameter': unquote(temp[1].split('=')[1])
}
req = requests.post(url, headers=headers, data=params)

req_url = 'https://udb.moe.edu.tw/DetailReportList/%E5%AD%B8%E7%94%9F%E9%A1%9E/StatDepartmentRegistrationRate/Download/?fileGuid=a587d367-821c-4d7c-a568-f507c09a727a&filename=%E5%AD%B812-1.%E6%96%B0%E7%94%9F%E8%A8%BB%E5%86%8A%E7%8E%87-%E4%BB%A5%E3%80%8C%E7%B3%BB(%E6%89%80)%E3%80%8D%E7%B5%B1%E8%A8%88.csv'
req_headers = {
    'ASP.NET_SessionId=0qkq5icfv4beqybee3tppo03; _ga=GA1.3.373763083.1588929927; _gid=GA1.3.1580700545.1588929927; __RequestVerificationToken=Gjq6vfR97AYkYZcaNKrUBnq1zbpsVQhbB24O9ZtdTq2en2ZKIfFrEsN8gxZu4oJKcvJUIPSK812v1gH9EEsGvR8XGtNtmV5uTp65cOsKRAQ1',
}

req = requests.get(req_url, headers=req_headers)

with requests.Session():
    download = req.content.decode('utf-8')
    cr = csv.reader(download.splitlines(), delimiter=',')

    with open('data.csv', 'w', encoding='utf-8', newline="") as fp:
        wr = csv.writer(fp)
        for line in list(cr):
            wr.writerow(line[0:])