# WhoScored-shot-locations

## Introduction
Using Selenium python and OpenCV to extract shot locations from [here](https://www.whoscored.com/).

## How to run the code

```
python shot.py
```

The code is currently written to obtain data for James Maddison of Norwich City. In order to change the player, 
  - The initial link to the player's fixture page must be passed as a parameter to the driver.get() function
  - 'if (name.get_attribute('title') == "James Maddison"):' - This snippet of code in the fromLink_home() and fromLink_away() functions        should be modified with the required player's name.
  
  The code will be modified later, so as to simply provide the player's name instead of making any changes to the code.
