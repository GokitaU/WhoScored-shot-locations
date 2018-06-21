from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import cv2

def getCoord(path):
    image = cv2.imread(path)

    row, col, __ = image.shape
    count = 0

    xList = []
    yList = []

    for i in range(row):
        for j in range(col):
            k = image[i][j]
            if k[0]==224 and k[1]==139:
                pos = (i, j)
                xList.append(pos[0])
                yList.append(pos[1])
                print(xList[count])
                # if ((posList[count][0]-posList[count-1][0])>5) and count > 0:
                #     print(posList[:][0])
                #     avg = sum(posList[:][0])/len(posList)
                #     print (avg)
                #     posList = []
                #     count = 0
                count+=1

    xList[len(xList)-1] = 1000
    xPoints = []
    yPoints = []
    xFinal = []
    yFinal = []
    for i in range (1, len(xList)):
        #print(xList[i], xList[i-1])
        diff = xList[i]-xList[i-1]
        xPoints.append(xList[i-1])
        yPoints.append(yList[i-1])

        #print(diff)
        
        if diff > 5:
            xFinal.append(sum(xPoints)/len(xPoints))
            yFinal.append(sum(yPoints)/len(xPoints))
            xPoints = []
            yPoints = []
            # xPoints.append(xList[i-1])
            # yPoints.append(yList[i-1])
            #Points.append(xList[i-1], yList[i-1])
        #     print(xList[i])


    print(xFinal)
    print(yFinal)

    
    
    








chop = webdriver.ChromeOptions()
chop.add_extension('AdBlock_v3.31.2.crx')

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.whoscored.com/Matches/1193314/Live/England-Championship-2017-2018-Wolverhampton-Wanderers-Norwich")


driver.maximize_window()
driver.execute_script("window.scrollTo(0, 1000)") 
driver.find_element_by_link_text("Chalkboard").click()
content = driver.find_element_by_xpath('//*[@id="chalkboard-stadium"]/div[3]/ul/div[9]/input').click()

time.sleep(10)

pic = pyautogui.screenshot()
pic.save('ShotMap.png')

im = cv2.imread('ShotMap.png')
crop = im[230:598, 344:1011]
cv2.imwrite('Out.png', crop)

getCoord('Out.png')


#driver.close()