from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_autoinstaller
import pyperclip

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

BUTTON_1_LOCATOR_BY_XPATH = "//button[1]"
BUTTON_2_LOCATOR_BY_XPATH = "//button[2]"
BUTTON_3_LOCATOR_BY_XPATH = "//button[3]"
BUTTON_4_LOCATOR_BY_XPATH = "//button[4]"

INPUT_TEXT_LOCATOR_BY_XPATH = "//textarea[@id='text_input']" 
OUTPUT_TEXT_LOCATOR_BY_XPATH = "//div[@id='text_output']"

BUTTON_1_DEFAULT_OUTPUT_TEXT = '''еяиееауоои
ияеоауаыееи
оеоиееуиеи
аиоыиоыуееи

ауияоеиаа'''
BUTTON_2_DEFAULT_OUTPUT_TEXT = '''еяи ее ауо ои
ияе оа уаые еи
о еои е еу и е и
аи оы и оы уееи

ауи яоеи аа'''

BUTTON_3_DEFAULT_OUTPUT_TEXT = '''еяи ее ауо ои,
ияе оа уаые еи.
о еои е еу и е и
аи оы и оы уееи.

ауи яоеи аа''' 

CUSTOM_INPUT_TEXT = '''
Во поле. берёзка стояла,
Во поле кудрявая-была!
?
'''

BUTTON_1_CUSTOM_OUTPUT_TEXT = '''
ооееёаояа
ооеуяаяыа
'''

BUTTON_2_CUSTOM_OUTPUT_TEXT = '''
о ое еёа ояа
о ое уяаяыа
'''

BUTTON_3_CUSTOM_OUTPUT_TEXT = '''
о ое. еёа ояа,
о ое уяая-ыа!
?
'''

ALL_BUTTONS_EMPTY_OUTPUT = ""


current_options = webdriver.ChromeOptions() 
current_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=current_options)
driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
sleep(1)
button_1 = driver.find_element_by_xpath(BUTTON_1_LOCATOR_BY_XPATH)
button_2 = driver.find_element_by_xpath(BUTTON_2_LOCATOR_BY_XPATH)
button_3 = driver.find_element_by_xpath(BUTTON_3_LOCATOR_BY_XPATH)
button_4 = driver.find_element_by_xpath(BUTTON_4_LOCATOR_BY_XPATH)
input_text = driver.find_element_by_xpath(INPUT_TEXT_LOCATOR_BY_XPATH)
output_text = driver.find_element_by_xpath(OUTPUT_TEXT_LOCATOR_BY_XPATH)

def test_all_buttons_are_present_in_maximized_mode():
    driver.maximize_window()
    print(driver.get_window_size())

    assert button_1.is_displayed
    assert button_2.is_displayed
    assert button_3.is_displayed
    assert button_4.is_displayed

def test_1_button_default_text():
    '''Tests the button 1 with default input text'''
    button_1.click()
    assert output_text.text.replace('\n',"") == BUTTON_1_DEFAULT_OUTPUT_TEXT.replace('\n',"")    

def test_2_button_default_text():
    '''Tests the button 2 with default input text'''
    button_2.click()
    assert output_text.text.replace('\n',"") == BUTTON_2_DEFAULT_OUTPUT_TEXT.replace('\n',"")

def test_3_button_default_text():
    '''Tests the button 3 with default input text'''
    button_3.click()
    assert output_text.text.replace('\n',"") == BUTTON_3_DEFAULT_OUTPUT_TEXT.replace('\n',"")    

def test_1_button_custom_input():
    '''Tests the button 1 with custom input text'''
    input_text.clear()
    input_text.send_keys(CUSTOM_INPUT_TEXT)
    button_1.click()
    assert output_text.text.replace('\n',"") == BUTTON_1_CUSTOM_OUTPUT_TEXT.replace('\n',"")

def test_2_button_custom_input():
    '''Tests the button 2 with custom input text'''
    button_2.click()
    assert output_text.text.replace('\n',"") == BUTTON_2_CUSTOM_OUTPUT_TEXT.replace('\n',"")

def test_3_button_custom_input():
    '''Tests the button 3 with custom input text'''
    button_3.click()
    assert output_text.text.replace('\n',"") == BUTTON_3_CUSTOM_OUTPUT_TEXT.replace('\n',"")

def test_1_button_empty_input():
    '''Tests the button 1 with empty input'''
    input_text.clear()
    button_1.click()
    assert output_text.text == ALL_BUTTONS_EMPTY_OUTPUT 

def test_2_button_empty_input():
    '''Tests the button 2 with empty input'''
    input_text.clear()
    button_2.click()
    assert output_text.text == ALL_BUTTONS_EMPTY_OUTPUT 

def test_3_button_empty_input():
    '''Tests the button 3 with empty input'''
    input_text.clear()
    button_3.click()
    assert output_text.text == ALL_BUTTONS_EMPTY_OUTPUT                

def test_4_button_output_text_is_selected():
    '''Tests the button 4 with custom input text'''
    input_text.clear()
    input_text.send_keys("АаБбВв -- ЭэЮюЯя")
    #Select data
    button_1.click()
    button_4.click()
    #Copy the text selection to a clipboard]
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    text_from_clipboard = pyperclip.paste()
    #Verify the text has been copied
    assert text_from_clipboard.replace('\n',"") == "ааээююяя" 

def test_all_buttons_are_present_in_narrow_mode():
    '''Tests all 4 buttons presence on the narrow size window'''
    driver.set_window_position(0, 0)
    driver.set_window_size(480,320)

    assert button_1.is_displayed
    assert button_2.is_displayed
    assert button_3.is_displayed
    assert button_4.is_displayed

    driver.quit()