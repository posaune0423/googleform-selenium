from gformmanager import Gformmanager
import datetime
import time


now = datetime.datetime.now()
today = now.strftime("%Y/%m/%d")

# Inputs Examples
email = 'test@gmail.com'
last_name = '山田'
first_name = '太郎'
identity = '122341'
done_classes = [6, 7]
students_name = '武田太朗、武田武子'
route = 'エストニア->船橋'
travel_expense = 300



gformmanager = Gformmanager()
url = 'https://yourgoogleformpath'

gformmanager.get(url)

time.sleep(1)

######## Page 1 #########

inputs = gformmanager.get_inputs()

input_email = inputs[0]
input_last_name = inputs[1]
input_first_name = inputs[2]
input_id = inputs[3]
input_date = inputs[4]


input_email.send_keys(email)
input_last_name.send_keys(last_name)
input_first_name.send_keys(first_name)
input_id.send_keys(identity)
input_date.send_keys(today)


options = gformmanager.get_options()
option_status = options[0]
option_place = options[3]


# 勤務ステータス
option_status.click()
gformmanager.select_option_by_index(1)


# 勤務校舎
option_place.click()
gformmanager.select_option_by_index(1)

gformmanager._next()


######## Page 2 #########

inputs = gformmanager.get_inputs()
options = gformmanager.get_options()
checkboxes = gformmanager.get_checkboxes()


students_name_input = inputs[0]
option_didchores = options[0]


# select radiobox accordind to the given array
for i in done_classes:
	checkboxes[i - 1].click()


# 生徒氏名
students_name_input.send_keys(students_name)

# 事務作業・ホスティングはしましたか？
option_didchores.click()
gformmanager.select_option_by_index(2)

gformmanager._next()


######## Page 3 #########

options = gformmanager.get_options()

option_didpostiong = options[0]

# ビラ配布を実施しましたか？
option_didpostiong.click()
gformmanager.select_option_by_index(2)

gformmanager._next()

######## Page 4 #########

options = gformmanager.get_options()
option_is_travel_expense_needed = options[0]

# 交通費は発生しましたか？
option_is_travel_expense_needed.click()
gformmanager.select_option_by_index(1)


gformmanager._next()

######## Page 5 #########

inputs = gformmanager.get_inputs()

input_route = inputs[0]
input_travel_expense = inputs[1]

# 経路 & 交通費
input_route.send_keys(route)
input_travel_expense.send_keys(travel_expense)

gformmanager._next()


time.sleep(10)
gformmanager.quit()
