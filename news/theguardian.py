from constants import *
import constants


def getNews(link, c):

    def getDriver():
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=options,
                                  executable_path=constants.driverPath)
        driver.get(link)
        return driver

    def disposer():
        driver.quit()

    def getHeader():
        return driver.find_elements_by_css_selector("h1")[0].text

    def getParagraphs():
        paragraph = driver.find_elements_by_css_selector("p")
        if len(paragraph) == 0:
            print("NOT A NEWS PAGE")
        return paragraph
    try:
        driver = getDriver()
        header = getHeader()
        paragraph = getParagraphs()
        sParagraph: str = ""
        for item in paragraph:
            if item.text != "" and item.text != "Already have an account? Log in here" and item.text != "There are no Independent Premium comments yet - be the first to add your thoughts":
                sParagraph += (item.text)
        disposer()
        save(header, sParagraph, c, link)
    except Exception as e:
        print(e)


def save(header, paragraph, c, link):
    writer = "LINK:" + link + "\nTITLE: " + header + "\n" + paragraph
    if len(paragraph) > 10:
        with open(constants.path + "guardian/" + str(c) + ".txt", "a+", encoding="utf-8") as f:
            f.write(writer)
            print("saved: " + constants.path + "guardian/" + str(c) + ".txt")
