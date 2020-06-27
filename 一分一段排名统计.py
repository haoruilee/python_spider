#61518407 李浩瑞
#2019湖北文科 655~542段 一分一段统计json
import pandas as pd
import json
def excel_to_json(path):
    '''
    本函数可将指定excel转为json格式并返回
    变量说明：
    path: Excel文件路径
    Wenke_dict:文科一分一段统计json
    '''
    xlsx_file = path
    fulldata = pd.read_excel(xlsx_file)#将数据读取为dataframe格式
    temp=dict()#中间变量记录一分一段
    for i in range(len(fulldata)):
        temp[str(fulldata.loc[i][0])]=float(fulldata.loc[i][1])
    Wenke_dict={"2019":{"湖北":{"文科":temp}}}
    return Wenke_dict

if __name__ == '__main__':
    Wenke_dict=excel_to_json("Hubei_W_1.xlsx")#由于提供数据为图片格式，故手工记录了一分一段统计Excel
    with open('排名.json', 'w', encoding='utf8') as f:#指定uft-8编码保存
        json.dump(Wenke_dict, f,indent=4,ensure_ascii=False)#四行缩进，保证中文编码
    print("Successfully save 排名.json")
