# Created by: Scarlett Gao
# Created on: Sep 2017
# Created for: ICS3U

import ui

def calculate_temperature_Fahrenheit(temperature_Celsius):
    # calculate_temperature_Fahrenheit
    
    temperature_Fahrenheit = (1.8)*(temperature_Celsius)+32
    view['temperature_Fahrenheit_answer_label'].text = 'The anwser is: ' + str(temperature_Fahrenheit)

def calculate_button_touch_up_inside(sender):
    # input
    temperature_Celsius = int(view['temperature_Celsius_textbox'].text)
    calculate_temperature_Fahrenheit(temperature_Celsius)

view = ui.load_view()
view.present('full_screen')
