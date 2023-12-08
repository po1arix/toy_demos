import requests
from bs4 import BeautifulSoup
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
        input_place = input('请输入要查询的地区(拼音不区分大小写,兰溪请输入lanxi1):')
        input_place = input_place.lower()
        input_day = int(input('请输入要查询的天数(1-40):'))
        use_day = 40
        return input_place + '/' + str(use_day), input_day , input_place 
    def get_weather_dict(self, placehtml, c):
        ddwt = []
        temporary = []
        cnt = 0
        URL = self.url + placehtml
        html = requests.get(URL, headers = self.headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        everything = soup.select(f'body > div.w1100.newday40_top > div.inleft > ul.weaul')
        eve = everything[0].get_text().split('\n')
        
        while '' in eve:
            eve.remove('')
        
        while '查看天气详情' in eve:
            eve.remove('查看天气详情')
        for i in eve:
            if cnt %4 != 0 or cnt == 0:
                temporary.append(i)
            else:
                ddwt.append(temporary)
                temporary = [i]
            cnt += 1
        print(ddwt)
        return ddwt
    def out(self, c, place, d_dwt):
        print(f'以下是{place}未来{c}天内的天气预报（包括今天）')
        print('-----------------')
        cnt = 0
        for i in range(len(d_dwt)):
            if cnt == c:
                break
            cnt += 1
            print(d_dwt[i][0],d_dwt[i][1],'\t',d_dwt[i][2],d_dwt[i][3],sep = '')
        print('-----------------')
        print('查询完毕，感谢使用')
if __name__== "__main__":
    w = Weather()
    placehtml,c,place= w.place_html()
    ddwt = w.get_weather_dict(placehtml, c)
    w.out(c,place,ddwt)








