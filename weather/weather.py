'''
小天才留言：不要尝试用多个request，包括但不限于写多个r，写循环多次r
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
class Weather:
    def __init__(self):
        self.url = 'https://www.tianqi.com/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

    def place_html(self):
        print('输入拼音查询天气，列如')
        print('hangzhou')
        print('xiaoshan')
        print('yuhang')
        print('……')
        input_place = input('请输入要查询的地区(拼音不区分大小写):')
        input_place = input_place.lower()
        input_day = int(input('请输入要查询的天数(1-40):'))
        use_day = 40
        return input_place + '/' + str(use_day), input_day , input_place
    
    def get_weather_dict(self, placehtml, c):
        ddwt = []
        temporary = []
        cnt = 0
        # for i in range(1, int(c)+1):
        URL = self.url + placehtml
        html = requests.get(URL, headers = self.headers)
        soup = BeautifulSoup(html.text, 'html.parser')
            # date = soup.select(f'body > div.w1100.newday40_top > div.inleft > ul.weaul > li:nth-child({str(i)}) > a > div.weaul_q.weaul_qblue > span.fl')
            # day  = soup.select(f'body > div.w1100.newday40_top > div.inleft > ul.weaul > li:nth-child({str(i)}) > a > div.weaul_q.weaul_qblue > span.fr')
            # weather = soup.select(f'body > div.w1100.newday40_top > div.inleft > ul.weaul > li:nth-child({str(i)}) > a > div:nth-child(3)')
            # temperature = soup.select(f'body > div.w1100.newday40_top > div.inleft > ul.weaul > li:nth-child({str(i)}) > a > div:nth-child(4)')
        everything = soup.select(f'body > div.w1100.newday40_top > div.inleft > ul.weaul')
        eve = everything[0].get_text().split('\n')
        # 删除eve中的空元素
        while '' in eve:
            eve.remove('')
        while '查看天气详情' in eve:
            eve.remove('查看天气详情')

        for i in eve:
            if cnt %4 != 0 or cnt == 0:
                temporary.append(i)
                # print(i.get_text())
            else:
                ddwt.append(temporary)
                temporary = [i]
            cnt += 1
        # for i in everything:    
        #     lis.append(i.get_text())
        #     print(i.get_text())
            #     print('-----------------')
            # print(lis)
            # ddwt.append([date, day, weather, temperature])
            
            # break        
        print(ddwt)
        return ddwt
    
    # def data_process(self, data):
    #     dict = {}
    #     for i in range(0,len(data),4):
    #         dict[data[i]] = [data[i+1], data[i+2], data[i+3]]
    #     return dict    
        # dict = {}
        # date = []
        # day = []
        # weather = []
        # temperature = []
        # for i in range(len(data)):
        #     date.append(data[i][0].get_text())
        #     day.append(data[i][1].get_text())
        #     weather.append(data[i][2].get_text())
        #     temperature.append(data[i][3].get_text())
        # for date in date:
        #     dict[date] = [day, weather, temperature]
        # with pd.ExcelWriter('天.xlsx') as writer:
        #     df = pd.DataFrame(dict).to_excel(writer, sheet_name = 'weather')
        #     df.to_excel(writer, sheet_name = 'weather', index = False)
        #     writer.close()
    def out(self, c, place, d_dwt):
        print(f'以下是{place}未来{c}天内的天气预报（包括今天）')
        print('-----------------')
        cnt = 0
        for i in range(len(d_dwt)):
            if cnt == c:
                break
            cnt += 1
            print(d_dwt[i][0],d_dwt[i][1],'\t',d_dwt[i][2],d_dwt[i][3],sep = '')
        print('查询完毕，感谢使用')
if __name__== "__main__":
    w = Weather()
    placehtml,c,place= w.place_html()
    ddwt = w.get_weather_dict(placehtml, c)
    w.out(c,place,ddwt)








