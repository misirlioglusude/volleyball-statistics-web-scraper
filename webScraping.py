from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

website = 'https://auprosports.com/volleyball/stats/'

# Download and install ChromeDriver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get(website)

# Initialize lists to store data
rank = []
athlete_list = []
auTotalPoints = []
setsPlayed = []
kills = []
killsPerSet = []
attackErrors = []
attackAttempts = []
attackPercentage = []
assists = []
assistsPerSet = []
settingErrors = []
serviceAces = []
serviceErrors = []
serviceAcesPerSet = []
totalReceptionAttempts = []
receptionErrors = []
positiveReceptionPct = []
digs = []
digsPerSet = []
blocks = []
blocksPerSet = []
blockAssists = []

try:
    # Wait until the button is present in the DOM and visible
    choose_league_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="block-stats-root"]/div[1]/div[2]/div/div[1]/div'))
    )
    choose_league_button.click()

    # Wait for the matches to load and find them
    matches = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
    )

    for match in matches:
        try:
            rank.append(match.find_element(By.XPATH, './td[1]').text)
            athlete = match.find_element(By.XPATH, './td[2]').text
            athlete_list.append(athlete)
            auTotalPoints.append(match.find_element(By.XPATH, './td[3]').text)
            setsPlayed.append(match.find_element(By.XPATH, './td[4]').text)
            kills.append(match.find_element(By.XPATH, './td[5]').text)
            killsPerSet.append(match.find_element(By.XPATH, './td[6]').text)
            attackErrors.append(match.find_element(By.XPATH, './td[7]').text)
            attackAttempts.append(match.find_element(By.XPATH, './td[8]').text)
            attackPercentage.append(match.find_element(By.XPATH, './td[9]').text)
            assists.append(match.find_element(By.XPATH, './td[10]').text)
            assistsPerSet.append(match.find_element(By.XPATH, './td[11]').text)
            settingErrors.append(match.find_element(By.XPATH, './td[12]').text)
            serviceAces.append(match.find_element(By.XPATH, './td[13]').text)
            serviceErrors.append(match.find_element(By.XPATH, './td[14]').text)
            serviceAcesPerSet.append(match.find_element(By.XPATH, './td[15]').text)
            totalReceptionAttempts.append(match.find_element(By.XPATH, './td[16]').text)
            receptionErrors.append(match.find_element(By.XPATH, './td[17]').text)
            positiveReceptionPct.append(match.find_element(By.XPATH, './td[18]').text)
            digs.append(match.find_element(By.XPATH, './td[19]').text)
            digsPerSet.append(match.find_element(By.XPATH, './td[20]').text)
            blocks.append(match.find_element(By.XPATH, './td[21]').text)
            blocksPerSet.append(match.find_element(By.XPATH, './td[22]').text)
            blockAssists.append(match.find_element(By.XPATH, './td[23]').text)
        except Exception as e:
            print(f"Error processing match: {e}")

    print(athlete_list)

finally:
    # Close the browser
    driver.quit()

# Create DataFrame and save to CSV
df = pd.DataFrame({
    'rank': rank,
    'athlete_list': athlete_list,
    'auTotalPoints': auTotalPoints,
    'setsPlayed': setsPlayed,
    'kills': kills,
    'killsPerSet': killsPerSet,
    'attackErrors': attackErrors,
    'attackAttempts': attackAttempts,
    'attackPercentage': attackPercentage,
    'assists': assists,
    'assistsPerSet': assistsPerSet,
    'settingErrors': settingErrors,
    'serviceAces': serviceAces,
    'serviceErrors': serviceErrors,
    'serviceAcesPerSet': serviceAcesPerSet,
    'totalReceptionAttempts': totalReceptionAttempts,
    'receptionErrors': receptionErrors,
    'positiveReceptionPct': positiveReceptionPct,
    'digs': digs,
    'digsPerSet': digsPerSet,
    'blocks': blocks,
    'blocksPerSet': blocksPerSet,
    'blockAssists': blockAssists,
})

df.replace('‚Äì', '', inplace=True)

try:
    df.to_csv('/Users/sude/Projects/volleyball_data.csv', index=False, encoding='utf-8-sig')
    print("CSV file successfully created.")
except Exception as e:
    print(f"Error saving CSV file: {e}")

print(df)