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
CSV = []


def check (x, y, Dict):
    for i in Dict.keys():
        res = i+1
        for j in Dict[i]:
            if (abs(x - j[0]) < 10) and (abs(y - j[1]) < 10):
                return i
                
    return res


def getCoordAway(path):
    image = cv2.imread(path)
    flag = 0

    row, col, __ = image.shape
    count = 0

    xList = []
    yList = []
    

    for i in range(row):
        for j in range(col):
            k = image[i][j]
            if k[0]==224 and k[1]==139:
                flag = 1
                pos = (i, j)
                print(pos)
                xList.append(pos)
                yList.append(pos[1])
                count+=1

    
    if (flag == 0):
        return

    
    xList[len(xList)-1] = (1000, 1000)
    sort = sorted(xList, key = lambda k: [k[1], k[0]])
    print(sort)
    xPoints = []
    yPoints = []
    shot = {}
    shot_count = 0
    shot[shot_count]=[]
    for i in range (1, len(xList)):

        print (abs(sort[i][0]-sort[i-1][0]))
        print (abs(sort[i][1]-sort[i-1][1]))

        if ((abs(sort[i][0]-sort[i-1][0]) < 10) and (abs(sort[i][1]-sort[i-1][1]) < 10)):
            xPoints.append(sort[i-1][0])
            yPoints.append(sort[i-1][1])
            shot[shot_count].append((sort[i-1][0], sort[i-1][1]))
            print(shot)
        
        else: 
            shot[shot_count].append((sort[i-1][0], sort[i-1][1]))
            shot_count = check(sort[i][0], sort[i][1], shot)
            #shot_count+=1

            if shot_count not in shot.keys():
                shot[shot_count] = []
            # xFinal.append(sum(xPoints)/len(xPoints))
            # yFinal.append(sum(yPoints)/len(xPoints))
            # xPoints = []
            # yPoints = []
            print(shot)



    final = []
   
    for i in shot.keys():
        if shot[i] and (len(shot[i])>5):
            xsum = 0
            ysum = 0
            for j in shot[i]:
                xsum = xsum + j[0]
                ysum = ysum + j[1]
            avg = (xsum/len(shot[i]), ysum/len(shot[i]))
            CSV.append(avg)
            final.append(avg)
            print(final)        
    # print(xFinal)
    # print(yFinal)
    

def getCoordHome(path):
    image = cv2.imread(path)
    flag = 0

    row, col, __ = image.shape
    count = 0

    xList = []
    yList = []
    

    for i in range(row):
        for j in range(col):
            k = image[i][j]
            if k[0]==20 and k[1]==91:
                flag = 1
                pos = (i, j)
                print(pos)
                xList.append(pos)
                yList.append(pos[1])
                count+=1

    
    if (flag == 0):
        return

    
    xList[len(xList)-1] = (1000, 1000)
    sort = sorted(xList, key = lambda k: [k[1], k[0]])
    print(sort)
    xPoints = []
    yPoints = []
    shot = {}
    shot_count = 0
    shot[shot_count]=[]
    for i in range (1, len(xList)):

        print (abs(sort[i][0]-sort[i-1][0]))
        print (abs(sort[i][1]-sort[i-1][1]))

        if ((abs(sort[i][0]-sort[i-1][0]) < 10) and (abs(sort[i][1]-sort[i-1][1]) < 10)):
            xPoints.append(sort[i-1][0])
            yPoints.append(sort[i-1][1])
            shot[shot_count].append((sort[i-1][0], sort[i-1][1]))
            print(shot)
        
        else: 
            shot[shot_count].append((sort[i-1][0], sort[i-1][1]))
            shot_count = check(sort[i][0], sort[i][1], shot)
            #shot_count+=1

            if shot_count not in shot.keys():
                shot[shot_count] = []
            # xFinal.append(sum(xPoints)/len(xPoints))
            # yFinal.append(sum(yPoints)/len(xPoints))
            # xPoints = []
            # yPoints = []
            print(shot)



    final = []
   
    for i in shot.keys():
        if shot[i] and (len(shot[i])>5):
            xsum = 0
            ysum = 0
            for j in shot[i]:
                xsum = xsum + j[0]
                ysum = ysum + j[1]
            avg = (xsum/len(shot[i]), ysum/len(shot[i]))
            CSV.append(avg)
            final.append(avg)
                    
    print(final)
    
    # print(xFinal)
    # print(yFinal)
    

def fromLink_away(driver, link):    
    driver.get(link)
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 1000)") 
    driver.find_element_by_link_text("Chalkboard").click()

    for i in range(1,15):
        name = driver.find_element_by_xpath('//*[@id="chalkboard-stadium"]/div[3]/ul/div[' + str(i) + ']/div[1]/span[2]')
        if (name.get_attribute('title') == "James Maddison"):
            pos = i
            break

    content = driver.find_element_by_xpath('//*[@id="chalkboard-stadium"]/div[3]/ul/div[' + str(pos) + ']/input').click()

    time.sleep(10)

    pic = pyautogui.screenshot()
    pic.save('ShotMap.png')

    im = cv2.imread('ShotMap.png')
    crop = im[230:598, 344:1011]
    cv2.imwrite('Out.png', crop)

    getCoordAway('Out.png')

def fromLink_home(driver, link):    
    driver.get(link)
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 1000)") 
    driver.find_element_by_link_text("Chalkboard").click()

    for i in range(1,15):
        name = driver.find_element_by_xpath('//*[@id="chalkboard-stadium"]/div[1]/ul/div[' + str(i) + ']/div[1]/span[2]')
        if (name.get_attribute('title') == "James Maddison"):
            pos = i
            break

    content = driver.find_element_by_xpath('//*[@id="chalkboard-stadium"]/div[1]/ul/div[' + str(pos) + ']/input').click()

    time.sleep(10)

    pic = pyautogui.screenshot()
    pic.save('ShotMap.png')

    im = cv2.imread('ShotMap.png')
    crop = im[230:598, 344:1011]
    cv2.imwrite('Out.png', crop)

    getCoordHome('Out.png')
    

def getLinks(driver):
    driver.get("https://www.whoscored.com/Players/137015/Fixtures/James-Maddison")
    
    away_links = []
    home_links = []

    for i in range(1, 50):
        link = driver.find_element_by_xpath('//*[@id="player-fixture"]/tbody/tr[' + str(i) + ']/td[4]/a')
        competition = driver.find_element_by_xpath('//*[@id="player-fixture"]/tbody/tr[' + str(i) + ']/td[1]/span/a')
        away_team = driver.find_element_by_xpath('//*[@id="player-fixture"]/tbody/tr[' + str(i) + ']/td[5]/a')
        #mins_played = driver.find_element_by_xpath('//*[@id="player-fixture"]/tbody/tr[' + str(i) + ']/td[8]')

        # dur = (mins_played.get_attribute('text'))
        # print(dur)
        
        if (competition.get_attribute('text') != "EFLC" and away_team.get_attribute('text') == "Norwich"):
            away_links.append(link.get_attribute('href'))

        if (competition.get_attribute('text') != "EFLC" and away_team.get_attribute('text') != "Norwich"):
            home_links.append(link.get_attribute('href'))


    return away_links, home_links

    
    

    
if __name__ == "__main__":

    chop = webdriver.ChromeOptions()
    chop.add_extension('AdBlock_v3.31.2.crx')
    driver = webdriver.Chrome('chromedriver.exe')

    away_links, home_links = getLinks(driver)

    for URL in away_links:
        fromLink_away(driver, URL)

    for URL in home_links:
        fromLink_home(driver, URL)

    pd.DataFrame(CSV).T.to_csv('shots.csv', index=False, header=None)


    # pd.DataFrame(xFinal).T.to_csv('xPoints.csv', index=False, header=None)
    # pd.DataFrame(yFinal).T.to_csv('yPoints.csv', index=False, header=None)


    #driver.close()

    