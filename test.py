# # uvicorn test:app --reload
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/test/{name}")
# async def test(name: str):
#     return {"message": f"Hello {name}"}

import requests
from bs4 import BeautifulSoup

# 目标网址
url = 'http://www.cwl.gov.cn/ygkj/wqkjgg/ssq/'

# 发送HTTP GET请求获取网页内容
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到包含中奖号码的表格
    table = soup.find('table', {'class': 'kj_tab'})

    # 找到表格中的所有行
    rows = table.find_all('tr')

    # 遍历表格的每一行，跳过表头
    for row in rows[1:]:
        # 获取每一行的所有单元格
        cells = row.find_all('td')

        # 提取日期和中奖号码
        date = cells[0].text.strip()
        red_balls = [cell.text.strip() for cell in cells[1:7]]
        blue_ball = cells[7].text.strip()

        # 打印结果
        print(f'日期: {date}, 红球: {", ".join(red_balls)}, 蓝球: {blue_ball}')
else:
    print('无法访问网站')