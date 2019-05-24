import time, csv, os
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

opts = Options()
opts.set_headless()
assert opts.headless
browser = Firefox(executable_path = "/Users/Ajay/Downloads/geckodriver",
                  options = opts)
browser2 = Firefox(executable_path = "/Users/Ajay/Downloads/geckodriver",
                  options = opts)
browser.get("https://botcheck.me/?apikey=6ecbebd4661b4746&username=theajayjain#query")
inputForm = browser.find_element_by_class_name("search")


bots = []
not_bots = set()
filepath = "/Users/Ajay/Desktop/Apps/Bot Detection/Finished Files"
for filename in os.listdir(filepath):
    print
    if filename[len(filename) - 4:] == ".csv":
        
        print filename
        with open(filepath + "/" + filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ",")
            for row in readCSV:
                bot = row[0]
                if bot != "user" and bot not in bots:
                    inputForm.clear()
                    inputForm.send_keys(bot)
                    inputForm.send_keys(Keys.ENTER)
                    time.sleep(5)
                    result = browser.find_elements_by_tag_name("p")
                    if result[1].text == "Propaganda Bot like Patterns Classified":
                        print bot
                        with open('/Users/Ajay/Desktop/Apps/Bot Detection/confirmed_bots.csv', 'a') as outfile:
                            writer = csv.writer(outfile)
                            writer.writerow([bot])
                        outfile.close()
                        bots.append(bot)
                    else:
                        url = "https://botsentinel.com/analyze/embedded?handle="
                        url += bot
                        browser2.get(url)
                        time.sleep(10)
                        botOrNot = browser2.find_elements_by_tag_name("span")[2].text
                        if botOrNot == "Problematic" or botOrNot == "Alarming":
                            print bot
                            with open('/Users/Ajay/Desktop/Apps/Bot Detection/confirmed_bots.csv', 'a') as outfile:
                                writer = csv.writer(outfile)
                                writer.writerow([bot])
                            outfile.close()
                            bots.append(bot)
                        else:
                            not_bots.add(bot)
        csvfile.close()
browser.close()
browser2.close()
