from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import cv2
import pandas as pd


xFinal = []
yFinal = []

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


def fromLink(driver, link):    
    driver.get(link)
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
    

def getLinks(driver):
    driver.get("https://www.whoscored.com/Players/137015/Fixtures/James-Maddison")
    
    links = []
    for i in range(1, 50):
        link = driver.find_element_by_xpath('//*[@id="player-fixture"]/tbody/tr[' + str(i) + ']/td[4]/a')
        competition = driver.find_element_by_xpath('//*[@id="player-fixture"]/tbody/tr[' + str(i) + ']/td[1]/span/a')
        away_team = driver.find_element_by_xpath('//*[@id="player-fixture"]/tbody/tr[' + str(i) + ']/td[5]/a')
        
        if (competition.get_attribute('text') != "EFLC" and away_team.get_attribute('text') == "Norwich"):
            links.append(link.get_attribute('href'))

    return links

    
    

    
if __name__ == "__main__":

    chop = webdriver.ChromeOptions()
    chop.add_extension('AdBlock_v3.31.2.crx')
    driver = webdriver.Chrome('chromedriver.exe')

    links = getLinks(driver)

    for URL in links:
        fromLink(driver, URL)

    


    pd.DataFrame(xFinal).T.to_csv('xPoints.csv', index=False, header=None)
    pd.DataFrame(yFinal).T.to_csv('yPoints.csv', index=False, header=None)


    #driver.close()

    