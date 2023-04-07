'''
Program:
	该程序可以协助识别网址中的不同部分，以便加快爬虫项目的开发。
History:
	2023/4/6	Shane	First release
'''

def tools_checkDif(url1, url2):
    '''对比两个网址，并输出其网址差异的地方'''
    k = 0
    for i in url1:
        for j in url2:
            if i == j:
                k += 1
                #相同值剔除
                modUrl1.pop(k)     #pop需要传入int型变量
                modUrl2.pop(k)
                break
            else:
                #如果出现不同值，检测到数值相同时为止
                sameFlag = 0
                print(f'i:{i}\nj:{j}')
    #打印修改后的列表
    print (f'{modUrl1}')
    print (f'{modUrl2}')

if __name__ == '__main__':
    url1 = 'happy1'
    url2 = 'happ22'
    modUrl1 = list(url1)
    modUrl2 = list(url2)

