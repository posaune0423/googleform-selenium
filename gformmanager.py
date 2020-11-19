import time
from selenium import webdriver
from pyautogui import write



class Gformmanager(webdriver.Chrome):

    def get_inputs(self):
        return self.find_elements_by_class_name('quantumWizTextinputPaperinputInput')


    def get_options(self):
        return self.find_elements_by_class_name('quantumWizMenuPaperselectOption')


    def get_checkboxes(self):
        return self.find_elements_by_class_name('freebirdFormviewerComponentsQuestionCheckboxChoice')


    def select_option_by_index(self, index):

        time.sleep(0.2)
	    # Put this where the program's supposed to select an option
        for _ in range(index):
            write(['down'])
        write(['enter'])


    def _next(self):
        nextbtn = self.find_elements_by_class_name('appsMaterialWizButtonEl')[1]
        nextbtn.click()
