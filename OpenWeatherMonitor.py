import datetime
import threading

import customtkinter as ctk
import requests
from PIL import Image

# -------------------------------------------------------------------------------------------------------------------- #

city = str
api = str
index_one = 1
index_two = 1
index_three = 1
index_four = 1
index_five = 1
index_six = 1
index_seven = 0
index_eight = 0
index_nine = 0
index_ten = 0
index_eleven = 0
index_twelve = 0


# ----- A set of functions that does stuff --------------------------------------------------------------------------- #

def transition_animator():
    def color_change_one():

        global index_one

        if index_one == 1:
            FRAME_LEFT.configure(fg_color='#242424')
            FRAME_LEFT.after(15, color_change_one)
        elif index_one == 2:
            FRAME_LEFT.configure(fg_color='#252525')
            FRAME_LEFT.after(15, color_change_one)
        elif index_one == 3:
            FRAME_LEFT.configure(fg_color='#262626')
            FRAME_LEFT.after(15, color_change_one)
        elif index_one == 4:
            FRAME_LEFT.configure(fg_color='#272727')
            FRAME_LEFT.after(15, color_change_one)
        elif index_one == 5:
            FRAME_LEFT.configure(fg_color='#282828')
            FRAME_LEFT.after(15, color_change_one)
        elif index_one == 6:
            FRAME_LEFT.configure(fg_color='#292929')
            FRAME_LEFT.after(15, color_change_one)
        elif index_one == 7:
            FRAME_LEFT.configure(fg_color='#2A2A2A')
            FRAME_LEFT.after(15, color_change_one)
        elif index_one == 8:
            FRAME_LEFT.configure(fg_color='#2B2B2B')
            FRAME_LEFT.after(15, color_change_one)
        else:
            SYMBOL_FRAME.place(
                x=62.5,
                y=380
            )
            WEATHER_SYMBOL_LABEL.pack()
            WEATHER_DESCRIPTION_LABEL.place(
                x=64,
                y=575
            )
            FRAME_LEFT.after(125, color_change_two)

        index_one += 1

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    def color_change_two():

        global index_two

        if index_two == 1:
            FRAME_CENTER.configure(fg_color='#242424')
            FRAME_CENTER.after(15, color_change_two)
        elif index_two == 2:
            FRAME_CENTER.configure(fg_color='#252525')
            FRAME_ONE.configure(fg_color='#252525')
            FRAME_TWO.configure(fg_color='#252525')
            FRAME_THREE.configure(fg_color='#252525')
            FRAME_FOUR.configure(fg_color='#252525')
            FRAME_FIVE.configure(fg_color='#252525')
            FRAME_CENTER.after(15, color_change_two)
        elif index_two == 3:
            FRAME_CENTER.configure(fg_color='#262626')
            FRAME_ONE.configure(fg_color='#262626')
            FRAME_TWO.configure(fg_color='#262626')
            FRAME_THREE.configure(fg_color='#262626')
            FRAME_FOUR.configure(fg_color='#262626')
            FRAME_FIVE.configure(fg_color='#262626')
            FRAME_CENTER.after(15, color_change_two)
        elif index_two == 4:
            FRAME_CENTER.configure(fg_color='#272727')
            FRAME_ONE.configure(fg_color='#272727')
            FRAME_TWO.configure(fg_color='#272727')
            FRAME_THREE.configure(fg_color='#272727')
            FRAME_FOUR.configure(fg_color='#272727')
            FRAME_FIVE.configure(fg_color='#272727')
            FRAME_CENTER.after(15, color_change_two)
        elif index_two == 5:
            FRAME_CENTER.configure(fg_color='#282828')
            FRAME_ONE.configure(fg_color='#282828')
            FRAME_TWO.configure(fg_color='#282828')
            FRAME_THREE.configure(fg_color='#282828')
            FRAME_FOUR.configure(fg_color='#282828')
            FRAME_FIVE.configure(fg_color='#282828')
            FRAME_CENTER.after(15, color_change_two)
        elif index_two == 6:
            FRAME_CENTER.configure(fg_color='#292929')
            FRAME_ONE.configure(fg_color='#292929')
            FRAME_TWO.configure(fg_color='#292929')
            FRAME_THREE.configure(fg_color='#292929')
            FRAME_FOUR.configure(fg_color='#292929')
            FRAME_FIVE.configure(fg_color='#292929')
            FRAME_CENTER.after(15, color_change_two)
        elif index_two == 7:
            FRAME_CENTER.configure(fg_color='#2A2A2A')
            FRAME_ONE.configure(fg_color='#2A2A2A')
            FRAME_TWO.configure(fg_color='#2A2A2A')
            FRAME_THREE.configure(fg_color='#2A2A2A')
            FRAME_FOUR.configure(fg_color='#2A2A2A')
            FRAME_FIVE.configure(fg_color='#2A2A2A')
            FRAME_CENTER.after(15, color_change_two)
        elif index_two == 8:
            FRAME_CENTER.configure(fg_color='#2B2B2B')
            FRAME_ONE.configure(fg_color='#2B2B2B')
            FRAME_TWO.configure(fg_color='#2B2B2B')
            FRAME_THREE.configure(fg_color='#2B2B2B')
            FRAME_FOUR.configure(fg_color='#2B2B2B')
            FRAME_FIVE.configure(fg_color='#2B2B2B')
            FRAME_CENTER.after(15, color_change_two)
        else:
            FRAME_CENTER.after(125, color_change_three)

        index_two += 1

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    def color_change_three():

        global index_three
        if index_three == 1:
            FRAME_RIGHT.configure(fg_color='#242424')
            FRAME_RIGHT.after(15, color_change_three)
        elif index_three == 2:
            FRAME_RIGHT.configure(fg_color='#252525')
            FRAME_RIGHT.after(15, color_change_three)
        elif index_three == 3:
            FRAME_RIGHT.configure(fg_color='#262626')
            FRAME_RIGHT.after(15, color_change_three)
        elif index_three == 4:
            FRAME_RIGHT.configure(fg_color='#272727')
            FRAME_RIGHT.after(15, color_change_three)
        elif index_three == 5:
            FRAME_RIGHT.configure(fg_color='#282828')
            FRAME_RIGHT.after(15, color_change_three)
        elif index_three == 6:
            FRAME_RIGHT.configure(fg_color='#292929')
            FRAME_RIGHT.after(15, color_change_three)
        elif index_three == 7:
            FRAME_RIGHT.configure(fg_color='#2A2A2A')
            FRAME_RIGHT.after(15, color_change_three)
        elif index_three == 8:
            FRAME_RIGHT.configure(fg_color='#2B2B2B')
            FRAME_RIGHT.after(15, color_change_three)
        else:
            FRAME_RIGHT.after(12, sub_color_change)
        index_three += 1

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    def sub_color_change():

        def color_changer(arg):

            global index_four
            global index_five

            if index_four == 1:
                arg.configure(fg_color='#2B2B2B')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 2:
                arg.configure(fg_color='#2C2C2C')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 3:
                arg.configure(fg_color='#2D2D2D')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 4:
                arg.configure(fg_color='#2E2E2E')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 5:
                arg.configure(fg_color='#2F2F2F')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 6:
                arg.configure(fg_color='#303030')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 7:
                arg.configure(fg_color='#313131')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 8:
                arg.configure(fg_color='#323232')
                arg.after(12, sub_color_change)
                index_four += 1
            elif index_four == 9:
                arg.configure(fg_color='#333333')
                arg.after(12, sub_color_change)
                index_four += 1
            else:
                index_five += 1
                index_four = 1
                sub_color_change()

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        if index_five == 1:
            SUB_FRAME_ONE.pack(pady=25)
            color_changer(SUB_FRAME_ONE)
        elif index_five == 2:
            SUB_FRAME_TWO.pack(pady=25)
            color_changer(SUB_FRAME_TWO)
        elif index_five == 3:
            SUB_FRAME_THREE.pack(pady=25)
            color_changer(SUB_FRAME_THREE)
        elif index_five == 4:
            SUB_FRAME_FOUR.pack(pady=25)
            color_changer(SUB_FRAME_FOUR)
        elif index_five == 5:
            SUB_FRAME_FIVE.pack(pady=25)
            color_changer(SUB_FRAME_FIVE)
        else:
            frame_left_widgets()

    # ---------------------------------------------------------------------------------------------------------------- #

    color_change_one()


# -------------------------------------------------------------------------------------------------------------------- #


def frame_left_widgets():
    global index_six

    # ---------------------------------------------------------------------------------------------------------------- #

    def width_changer_one():

        global index_seven
        global index_six
        if index_seven <= 200:
            ENTRY_CITY.configure(width=index_seven)
            index_seven += 20
            ENTRY_CITY.after(14, width_changer_one)
        else:
            index_six += 1
            index_seven = 0
            FRAME_LEFT.after(125, frame_left_widgets)

    def width_changer_two():

        global index_seven
        global index_six
        if index_seven <= 200:
            ENTRY_API.configure(width=index_seven)
            index_seven += 20
            ENTRY_API.after(14, width_changer_two)
        else:
            index_six += 1
            index_seven = 0
            FRAME_LEFT.after(200, frame_left_widgets)

    # ---------------------------------------------------------------------------------------------------------------- #

    if index_six == 1:
        FRAME_CENTER.after(125, lambda: APP_NAME_TOP.place(x=46, y=50))
        FRAME_CENTER.after(350, lambda: APP_NAME_BOTTOM.place(x=100, y=100))
        index_six += 1
        FRAME_CENTER.after(650, frame_left_widgets)

    elif index_six == 2:
        ENTRY_CITY.place(
            x=50,
            y=170
        )
        width_changer_one()
    elif index_six == 3:
        ENTRY_API.place(
            x=50,
            y=220
        )
        width_changer_two()
    else:
        BUTTON.place(
            x=80,
            y=285
        )
        index_six = 1
        FRAME_CENTER.after(350, frame_center_widgets)


# -------------------------------------------------------------------------------------------------------------------- #


def focus_out_func_two(event):
    if ENTRY_API.get() == '':
        ENTRY_CITY.focus()
    else:
        pass


# ---------------------------------------------------------------------------------------------------------------------#


def frame_center_widgets():
    def width_changer_one():

        global index_seven
        global index_six
        if index_seven <= 405:
            TEMPERATURE_BAR.configure(width=index_seven)
            index_seven += 45
            TEMPERATURE_BAR.after(14, width_changer_one)
        else:
            index_six += 1
            index_seven = 0
            FRAME_CENTER.after(75, frame_center_widgets)

    def width_changer_two():

        global index_seven
        global index_six
        if index_seven <= 405:
            REAL_FEEL_BAR.configure(width=index_seven)
            index_seven += 45
            REAL_FEEL_BAR.after(14, width_changer_two)
        else:
            index_six += 1
            index_seven = 0
            FRAME_CENTER.after(75, frame_center_widgets)

    def width_changer_three():

        global index_seven
        global index_six
        if index_seven <= 405:
            HUMIDITY_BAR.configure(width=index_seven)
            index_seven += 45
            HUMIDITY_BAR.after(14, width_changer_three)
        else:
            index_six += 1
            index_seven = 0
            FRAME_CENTER.after(75, frame_center_widgets)

    def width_changer_four():

        global index_seven
        global index_six
        if index_seven <= 405:
            PRESSURE_BAR.configure(width=index_seven)
            index_seven += 45
            PRESSURE_BAR.after(14, width_changer_four)
        else:
            index_six += 1
            index_seven = 0
            FRAME_CENTER.after(75, frame_center_widgets)

    def width_changer_five():

        global index_seven
        global index_six
        if index_seven <= 405:
            WIND_SPEED_BAR.configure(width=index_seven)
            index_seven += 45
            WIND_SPEED_BAR.after(14, width_changer_five)
        else:
            pass

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   #

    if index_six == 1:
        TEMPERATURE_BAR.place(
            x=50,
            y=125
        )
        TEMPERATURE_BAR.set(0)
        width_changer_one()
    elif index_six == 2:
        REAL_FEEL_BAR.place(
            x=50,
            y=235
        )
        REAL_FEEL_BAR.set(0)
        width_changer_two()
    elif index_six == 3:
        HUMIDITY_BAR.place(
            x=50,
            y=345
        )
        HUMIDITY_BAR.set(0)
        width_changer_three()
    elif index_six == 4:
        PRESSURE_BAR.place(
            x=50,
            y=455
        )
        PRESSURE_BAR.set(0)
        width_changer_four()
    else:
        WIND_SPEED_BAR.place(
            x=50,
            y=565
        )
        WIND_SPEED_BAR.set(0)
        width_changer_five()


# -------------------------------------------------------------------------------------------------------------------- #


def button_func():
    global city
    global api
    city = ENTRY_CITY.get()
    api = ENTRY_API.get()

    # ---------------------------------------------------------------------------------------------------------------- #
    try:
        BASE_URL_ONE = "http://api.openweathermap.org/data/2.5/weather?"
        FINAL_URL_ONE = BASE_URL_ONE + "appid=" + api + "&q=" + city
        weather_data_current = requests.get(FINAL_URL_ONE).json()

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        temperature_description = weather_data_current['weather'][0]['description']
        temperature_main = weather_data_current['weather'][0]['main']
        temperature = round((weather_data_current['main']['temp'] - 273.15), 1)
        feels_like = round((weather_data_current['main']['feels_like'] - 273.15), 1)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        humidity = weather_data_current['main']['humidity']

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        pressure = weather_data_current['main']['pressure']

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        wind_speed = round(weather_data_current['wind']['speed'], 1)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        check_symbol = weather_data_current['weather'][0]['icon']
        define_symbol = check_symbol[2]

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        temperature_label_variable.set(f'{temperature} °C')
        temperature_sub_label_variable.set(value='Actual Temperature')

        real_feel_label_variable.set(f'{feels_like} °C')
        real_feel_sub_label_variable.set(value='Real Feel')

        humidity_label_variable.set(f'{humidity} %')
        humidity_sub_label_variable.set(value='Humidity')

        pressure_label_variable.set(f'{pressure} hPa')
        pressure_sub_label_variable.set(value='Atmospheric Pressure')

        wind_speed_label_variable.set(f'{wind_speed} m/s')
        wind_speed_sub_label_variable.set(value='Wind Speed')

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        def symbol_placer_and_bar_progressor():

            CURRENT_WEATHER_LABEL.place(x=320, y=635)

            def symbol_placer():

                if temperature_main == 'Thunderstorm':
                    WEATHER_SYMBOL_LABEL.configure(image=THUNDERSTORM_SYMBOL)


                elif temperature_main == 'Drizzle':
                    WEATHER_SYMBOL_LABEL.configure(image=DRIZZLE_SYMBOL)


                elif temperature_main == 'Rain':

                    if temperature_description == ['light rain', 'moderate rain', 'heavy intensity rain',
                                                   'very heavy rain', 'extreme rain']:

                        if define_symbol == 'd':
                            WEATHER_SYMBOL_LABEL.configure(image=RAIN_SYMBOL_DAY)
                        else:
                            WEATHER_SYMBOL_LABEL.configure(image=RAIN_SYMBOL_NIGHT)

                    elif temperature_description == 'freezing rain':
                        WEATHER_SYMBOL_LABEL.configure(image=FREEZING_RAIN_SYMBOL)

                    else:
                        WEATHER_SYMBOL_LABEL.configure(image=SHOWER_RAIN_SYMBOL)


                elif temperature_main == 'Snow':
                    WEATHER_SYMBOL_LABEL.configure(image=SNOW_SYMBOL)


                elif temperature_description in ['mist', 'smoke', 'haze', 'sand/dust whirls', 'fog', 'sand', 'dust',
                                                 'volcanic ash', 'squalls', 'tornado']:
                    WEATHER_SYMBOL_LABEL.configure(image=ATMOSPHERE_SYMBOL)


                elif temperature_main == 'Clear':

                    if define_symbol == 'd':
                        WEATHER_SYMBOL_LABEL.configure(image=CLEAR_SKY_SYMBOL_DAY)

                    else:
                        WEATHER_SYMBOL_LABEL.configure(image=CLEAR_SKY_SYMBOL_NIGHT)


                elif temperature_main == 'Clouds':

                    if temperature_description == 'few clouds':
                        if define_symbol == 'd':
                            WEATHER_SYMBOL_LABEL.configure(image=FEW_CLOUDS_SYMBOL_DAY)
                        else:
                            WEATHER_SYMBOL_LABEL.configure(image=FEW_CLOUDS_SYMBOL_NIGHT)

                    elif temperature_description == 'scattered clouds':
                        WEATHER_SYMBOL_LABEL.configure(image=SCATTERED_CLOUDS_SYMBOL)

                    else:
                        WEATHER_SYMBOL_LABEL.configure(image=OVERCAST_CLOUDS_SYMBOL)

            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

            def bar_progressor():

                def bar_progressor_one():
                    global index_eight
                    if index_eight < (temperature / 100):
                        TEMPERATURE_BAR.set(index_eight)
                        index_eight += 0.01
                        FRAME_CENTER.after(10, bar_progressor_one)
                    else:
                        pass

                def bar_progressor_two():
                    global index_nine
                    if index_nine < (feels_like / 100):
                        REAL_FEEL_BAR.set(index_nine)
                        index_nine += 0.01
                        FRAME_CENTER.after(10, bar_progressor_two)
                    else:
                        pass

                def bar_progressor_three():
                    global index_ten
                    if index_ten < (humidity / 100):
                        HUMIDITY_BAR.set(index_ten)
                        index_ten += 0.01
                        FRAME_CENTER.after(10, bar_progressor_three)
                    else:
                        pass

                def bar_progressor_four():
                    global index_eleven
                    if index_eleven < (pressure / 10000):
                        PRESSURE_BAR.set(index_eleven)
                        index_eleven += 0.01
                        FRAME_CENTER.after(10, bar_progressor_four)
                    else:
                        pass

                def bar_progressor_five():
                    global index_twelve
                    if index_twelve < (wind_speed / 100):
                        WIND_SPEED_BAR.set(index_twelve)
                        index_twelve += 0.01
                        FRAME_CENTER.after(10, bar_progressor_five)
                    else:
                        pass

                def bar_progressor_six():
                    global index_eight
                    if index_eight > (temperature / 100):
                        TEMPERATURE_BAR.set(index_eight)
                        index_eight -= 0.01
                        FRAME_CENTER.after(10, bar_progressor_six)
                    else:
                        pass

                def bar_progressor_seven():
                    global index_nine
                    if index_nine > (feels_like / 100):
                        REAL_FEEL_BAR.set(index_nine)
                        index_nine -= 0.01
                        FRAME_CENTER.after(10, bar_progressor_seven)
                    else:
                        pass

                def bar_progressor_eight():
                    global index_ten
                    if index_ten > (humidity / 100):
                        HUMIDITY_BAR.set(index_ten)
                        index_ten -= 0.01
                        FRAME_CENTER.after(10, bar_progressor_eight)
                    else:
                        pass

                def bar_progressor_nine():
                    global index_eleven
                    if index_eleven > (pressure / 10000):
                        PRESSURE_BAR.set(index_eleven)
                        index_eleven -= 0.01
                        FRAME_CENTER.after(10, bar_progressor_nine)
                    else:
                        pass

                def bar_progressor_ten():
                    global index_twelve
                    if index_twelve > (wind_speed / 100):
                        WIND_SPEED_BAR.set(index_twelve)
                        index_twelve -= 0.01
                        FRAME_CENTER.after(10, bar_progressor_ten)
                    else:
                        pass

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

                bar_progressor_one()
                bar_progressor_two()
                bar_progressor_three()
                bar_progressor_four()
                bar_progressor_five()
                bar_progressor_six()
                bar_progressor_seven()
                bar_progressor_eight()
                bar_progressor_nine()
                bar_progressor_ten()

            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

            symbol_placer()
            bar_progressor()

        # ------------------------------------------------------------------------------------------------------------ #

        def thread_initiator():
            threading.Thread(target=symbol_placer_and_bar_progressor).start()

        # ------------------------------------------------------------------------------------------------------------ #

        thread_initiator()

        # ------------------------------------------------------------------------------------------------------------ #

        WEATHER_DESCRIPTION_VARIABLE.set(temperature_description)

        # ------------------------------------------------------------------------------------------------------------ #

        BASE_URL_TWO = "http://api.openweathermap.org/data/2.5/forecast?"
        FINAL_URL_TWO = BASE_URL_TWO + "appid=" + api + "&q=" + city
        weather_data_forecast = requests.get(FINAL_URL_TWO).json()

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        list_one_date = str(weather_data_forecast['list'][0]['dt_txt'])
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        year_one = int(list_one_date[:4])
        month_one = int(list_one_date[5:7])
        day_one = int(list_one_date[8:10])
        my_date_one = datetime.date(year_one, month_one, day_one)
        weekday_one = my_date_one.strftime('%A')
        one_var.set(weekday_one)
        one_var_day.set(day_one)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        list_one_temp = round((weather_data_forecast['list'][0]['main']['temp'] - 273.15), 1)
        list_one_feels_like = weather_data_forecast['list'][0]['main']['feels_like']
        list_one_humidity = weather_data_forecast['list'][0]['main']['humidity']
        list_one_speed = weather_data_forecast['list'][0]['wind']['speed']
        one_var_temperature.set(f'{list_one_temp} °C')

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        list_two_date = str(weather_data_forecast['list'][5]['dt_txt'])
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        year_two = int(list_two_date[:4])
        month_two = int(list_two_date[5:7])
        day_two = int(list_two_date[8:10])
        my_date_two = datetime.date(year_two, month_two, day_two)
        weekday_two = my_date_two.strftime('%A')
        two_var.set(weekday_two)
        two_var_day.set(day_two)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        list_two_temp = round((weather_data_forecast['list'][5]['main']['temp'] - 273.15), 1)
        list_two_feels_like = weather_data_forecast['list'][5]['main']['feels_like']
        list_two_humidity = weather_data_forecast['list'][5]['main']['humidity']
        list_two_speed = weather_data_forecast['list'][5]['wind']['speed']
        two_var_temperature.set(f'{list_two_temp} °C')

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        list_three_date = str(weather_data_forecast['list'][13]['dt_txt'])
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        year_three = int(list_three_date[:4])
        month_three = int(list_three_date[5:7])
        day_three = int(list_three_date[8:10])
        my_date_three = datetime.date(year_three, month_three, day_three)
        weekday_three = my_date_three.strftime('%A')
        three_var.set(weekday_three)
        three_var_day.set(day_three)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        list_three_temp = round((weather_data_forecast['list'][13]['main']['temp'] - 273.15), 1)
        list_three_feels_like = weather_data_forecast['list'][13]['main']['feels_like']
        list_three_humidity = weather_data_forecast['list'][13]['main']['humidity']
        list_three_speed = weather_data_forecast['list'][13]['wind']['speed']
        three_var_temperature.set(f'{list_three_temp} °C')

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        list_four_date = str(weather_data_forecast['list'][21]['dt_txt'])
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        year_four = int(list_four_date[:4])
        month_four = int(list_four_date[5:7])
        day_four = int(list_four_date[8:10])
        my_date_four = datetime.date(year_four, month_four, day_four)
        weekday_four = my_date_four.strftime('%A')
        four_var.set(weekday_four)
        four_var_day.set(day_four)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        list_four_temp = round((weather_data_forecast['list'][21]['main']['temp'] - 273.15), 1)
        list_four_feels_like = weather_data_forecast['list'][21]['main']['feels_like']
        list_four_humidity = weather_data_forecast['list'][21]['main']['humidity']
        list_four_speed = weather_data_forecast['list'][21]['wind']['speed']
        four_var_temperature.set(f'{list_four_temp} °C')

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        list_five_date = str(weather_data_forecast['list'][29]['dt_txt'])
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        year_five = int(list_five_date[:4])
        month_five = int(list_five_date[5:7])
        day_five = int(list_five_date[8:10])
        my_date_five = datetime.date(year_five, month_five, day_five)
        weekday_five = my_date_five.strftime('%A')
        five_var.set(weekday_five)
        five_var_day.set(day_five)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        list_five_temp = round((weather_data_forecast['list'][29]['main']['temp'] - 273.15), 1)
        list_five_feels_like = weather_data_forecast['list'][29]['main']['feels_like']
        list_five_humidity = weather_data_forecast['list'][29]['main']['humidity']
        list_five_speed = weather_data_forecast['list'][29]['wind']['speed']
        five_var_temperature.set(f'{list_five_temp} °C')

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        if day_one >= 10:
            sub_label_one_day.place(
                x=32,
                y=42
            )
        if day_two >= 10:
            sub_label_two_day.place(
                x=32,
                y=42
            )
        if day_three >= 10:
            sub_label_three_day.place(
                x=32,
                y=42
            )
        if day_four >= 10:
            sub_label_four_day.place(
                x=32,
                y=42
            )
        if day_five >= 10:
            sub_label_five_day.place(
                x=32,
                y=42
            )

        # ------------------------------------------------------------------------------------------------------------ #

    except KeyError:

        if weather_data_current['cod'] == 401:
            ENTRY_API.configure(border_color='red')
            ENTRY_API.after(200, lambda: ENTRY_API.configure(border_color='#631B69'))
            if ENTRY_CITY.get() == '':
                ENTRY_CITY.configure(border_color='red')
                ENTRY_CITY.after(200, lambda: ENTRY_CITY.configure(border_color='#631B69'))
            else:
                pass
        elif weather_data_current['cod'] == '404' or '400':
            ENTRY_CITY.configure(border_color='red')
            ENTRY_CITY.after(200, lambda: ENTRY_CITY.configure(border_color='#631B69'))
        else:
            pass


# ----- Main Window -------------------------------------------------------------------------------------------------  #


ctk.set_appearance_mode("dark")
ROOT = ctk.CTk()
ROOT.geometry('1250x800')
ROOT.title('Open Weather Monitor')
ROOT.iconbitmap('ROOT-Icon.ico')
ROOT.resizable(False, False)

# -------------------------------------------------------------------------------------------------------------------- #

FRAME_LEFT = ctk.CTkFrame(
    ROOT,
    width=300,
    height=700,
    fg_color='#242424'
)
FRAME_LEFT.pack(
    side='left',
    expand=True
)
FRAME_LEFT.pack_propagate(False)

FRAME_CENTER = ctk.CTkFrame(
    ROOT,
    width=500,
    height=700,
    fg_color='#242424'
)
FRAME_CENTER.pack(
    side='left',
    expand=True
)
FRAME_CENTER.pack_propagate(False)

FRAME_RIGHT = ctk.CTkFrame(
    ROOT,
    width=300,
    height=700,
    fg_color='#242424'
)
FRAME_RIGHT.pack(
    side='right',
    expand=True
)
FRAME_RIGHT.pack_propagate(False)

SUB_FRAME_ONE = ctk.CTkFrame(
    FRAME_RIGHT,
    width=250,
    height=90,
    fg_color='#2B2B2B'
)
SUB_FRAME_TWO = ctk.CTkFrame(
    FRAME_RIGHT,
    width=250,
    height=90,
    fg_color='#2B2B2B'
)
SUB_FRAME_THREE = ctk.CTkFrame(
    FRAME_RIGHT,
    width=250,
    height=90,
    fg_color='#2B2B2B'
)
SUB_FRAME_FOUR = ctk.CTkFrame(
    FRAME_RIGHT,
    width=250,
    height=90,
    fg_color='#2B2B2B'
)
SUB_FRAME_FIVE = ctk.CTkFrame(
    FRAME_RIGHT,
    width=250,
    height=90,
    fg_color='#2B2B2B'
)

# ---------------------------------------------------------------------------------------------------------------------#

one_var = ctk.StringVar()
sub_label_one = ctk.CTkLabel(
    SUB_FRAME_ONE,
    textvariable=one_var,
    font=('Nunito', 18, 'bold')
)
sub_label_one.place(
    x=14,
    y=8
)

two_var = ctk.StringVar()
sub_label_two = ctk.CTkLabel(
    SUB_FRAME_TWO,
    textvariable=two_var,
    font=('Nunito', 18, 'bold')
)
sub_label_two.place(
    x=14,
    y=8
)

three_var = ctk.StringVar()
sub_label_three = ctk.CTkLabel(
    SUB_FRAME_THREE,
    textvariable=three_var,
    font=('Nunito', 18, 'bold')
)
sub_label_three.place(
    x=14,
    y=8
)

four_var = ctk.StringVar()
sub_label_four = ctk.CTkLabel(
    SUB_FRAME_FOUR,
    textvariable=four_var,
    font=('Nunito', 18, 'bold')
)
sub_label_four.place(
    x=14,
    y=8
)

five_var = ctk.StringVar()
sub_label_five = ctk.CTkLabel(
    SUB_FRAME_FIVE,
    textvariable=five_var,
    font=('Nunito', 18, 'bold')
)
sub_label_five.place(
    x=14,
    y=8
)

# -------------------------------------------------------------------------------------------------------------------- #

one_var_day = ctk.StringVar()
sub_label_one_day = ctk.CTkLabel(
    SUB_FRAME_ONE,
    textvariable=one_var_day,
    font=('Nunito', 32, 'bold'),
    text_color='#BC33C7'
)
sub_label_one_day.place(
    x=40,
    y=42
)

two_var_day = ctk.StringVar()
sub_label_two_day = ctk.CTkLabel(
    SUB_FRAME_TWO,
    textvariable=two_var_day,
    font=('Nunito', 32, 'bold'),
    text_color='#BC33C7'
)
sub_label_two_day.place(
    x=40,
    y=42
)

three_var_day = ctk.StringVar()
sub_label_three_day = ctk.CTkLabel(
    SUB_FRAME_THREE,
    textvariable=three_var_day,
    font=('Nunito', 32, 'bold'),
    text_color='#BC33C7'
)
sub_label_three_day.place(
    x=40,
    y=42
)

four_var_day = ctk.StringVar()
sub_label_four_day = ctk.CTkLabel(
    SUB_FRAME_FOUR,
    textvariable=four_var_day,
    font=('Nunito', 32, 'bold'),
    text_color='#BC33C7'
)
sub_label_four_day.place(
    x=40,
    y=42
)

five_var_day = ctk.StringVar()
sub_label_five_day = ctk.CTkLabel(
    SUB_FRAME_FIVE,
    textvariable=five_var_day,
    font=('Nunito', 32, 'bold'),
    text_color='#BC33C7'
)
sub_label_five_day.place(
    x=40,
    y=42
)

# -------------------------------------------------------------------------------------------------------------------- #

one_var_temperature = ctk.StringVar()
sub_label_one_temperature = ctk.CTkLabel(
    SUB_FRAME_ONE,
    textvariable=one_var_temperature,
    font=('Nunito', 26, 'bold'),
    text_color='#CD38D9',
    width=130,
    anchor=ctk.SE
)
sub_label_one_temperature.place(
    x=105,
    y=32
)

two_var_temperature = ctk.StringVar()
sub_label_two_temperature = ctk.CTkLabel(
    SUB_FRAME_TWO,
    textvariable=two_var_temperature,
    font=('Nunito', 26, 'bold'),
    text_color='#CD38D9',
    width=130,
    anchor=ctk.SE
)
sub_label_two_temperature.place(
    x=105,
    y=32
)

three_var_temperature = ctk.StringVar()
sub_label_three_temperature = ctk.CTkLabel(
    SUB_FRAME_THREE,
    textvariable=three_var_temperature,
    font=('Nunito', 26, 'bold'),
    text_color='#CD38D9',
    width=130,
    anchor=ctk.SE
)
sub_label_three_temperature.place(
    x=105,
    y=32
)

four_var_temperature = ctk.StringVar()
sub_label_four_temperature = ctk.CTkLabel(
    SUB_FRAME_FOUR,
    textvariable=four_var_temperature,
    font=('Nunito', 26, 'bold'),
    text_color='#CD38D9',
    width=130,
    anchor=ctk.SE
)
sub_label_four_temperature.place(
    x=105,
    y=32
)

five_var_temperature = ctk.StringVar()
sub_label_five_temperature = ctk.CTkLabel(
    SUB_FRAME_FIVE,
    textvariable=five_var_temperature,
    font=('Nunito', 26, 'bold'),
    text_color='#CD38D9',
    width=130,
    anchor=ctk.SE,
)
sub_label_five_temperature.place(
    x=105,
    y=32
)

# -------------------------------------------------------------------------------------------------------------------- #

APP_NAME_TOP = ctk.CTkLabel(
    FRAME_LEFT,
    text='WEATHER',
    font=('Nunito', 40, 'bold'),
    text_color='white'
)
APP_NAME_BOTTOM = ctk.CTkLabel(
    FRAME_LEFT,
    text='MONITOR',
    font=('Nunito', 20, 'bold'),
    text_color='#BC33C7'
)

# -------------------------------------------------------------------------------------------------------------------- #

ENTRY_CITY = ctk.CTkEntry(
    FRAME_LEFT,
    placeholder_text='City Name',
    width=0,
    height=30,
    text_color='white',
    border_color='#631B69',
    border_width=2,
    font=('Nunito', 12, 'bold'),
    corner_radius=20,
)
ENTRY_CITY.bind('<Down>', lambda event: ENTRY_API.focus())
ENTRY_CITY.bind('<Return>', lambda event: ENTRY_API.focus())

ENTRY_API = ctk.CTkEntry(
    FRAME_LEFT,
    placeholder_text='API key',
    width=0,
    height=30,
    text_color='white',
    border_color='#631B69',
    border_width=2,
    font=('Nunito', 12, 'bold'),
    corner_radius=20,
)
ENTRY_API.configure(show='*')
ENTRY_API.bind('<Up>', lambda event: ENTRY_CITY.focus())
ENTRY_API.bind('<BackSpace>', focus_out_func_two)

# -------------------------------------------------------------------------------------------------------------------- #

BUTTON = ctk.CTkButton(
    FRAME_LEFT,
    text='Fetch',
    command=button_func,
    corner_radius=20,
    fg_color='#631B69',
    hover=False
)

# -------------------------------------------------------------------------------------------------------------------- #

FRAME_ONE = ctk.CTkFrame(
    FRAME_CENTER,
    width=150,
    height=40,
    fg_color='#242424'
)
FRAME_ONE.place(
    x=297,
    y=77
)
FRAME_ONE.pack_propagate(False)

temperature_label_variable = ctk.StringVar()
temperature_label = ctk.CTkLabel(
    FRAME_ONE,
    textvariable=temperature_label_variable,
    font=('Nunito', 25, 'bold'),
    text_color='white'
)
temperature_label.pack(anchor=ctk.SE)

temperature_sub_label_variable = ctk.StringVar()
temperature_sub_label = ctk.CTkLabel(
    FRAME_CENTER,
    textvariable=temperature_sub_label_variable,
    font=('Nunito', 14, 'bold')
)
temperature_sub_label.place(
    x=50,
    y=85
)

TEMPERATURE_BAR = ctk.CTkProgressBar(
    FRAME_CENTER,
    width=0,
    height=12,
    corner_radius=50,
    progress_color='purple',
    mode='determinate'
)

# -------------------------------------------------------------------------------------------------------------------- #

FRAME_TWO = ctk.CTkFrame(
    FRAME_CENTER,
    width=150,
    height=40,
    fg_color='#242424'
)
FRAME_TWO.place(
    x=297,
    y=187
)
FRAME_TWO.pack_propagate(False)

real_feel_label_variable = ctk.StringVar()
real_feel_label = ctk.CTkLabel(
    FRAME_TWO,
    textvariable=real_feel_label_variable,
    font=('Nunito', 25, 'bold'),
    text_color='white'
)
real_feel_label.pack(anchor=ctk.SE)

real_feel_sub_label_variable = ctk.StringVar()
real_feel_sub_label = ctk.CTkLabel(
    FRAME_CENTER,
    textvariable=real_feel_sub_label_variable,
    font=('Nunito', 14, 'bold')
)
real_feel_sub_label.place(
    x=50,
    y=195
)

REAL_FEEL_BAR = ctk.CTkProgressBar(
    FRAME_CENTER,
    width=0,
    height=12,
    corner_radius=50,
    progress_color='purple',
    mode='determinate'
)

# -------------------------------------------------------------------------------------------------------------------- #

FRAME_THREE = ctk.CTkFrame(
    FRAME_CENTER,
    width=150,
    height=40,
    fg_color='#242424'
)
FRAME_THREE.place(
    x=297,
    y=297
)
FRAME_THREE.pack_propagate(False)

humidity_label_variable = ctk.StringVar()
humidity_label = ctk.CTkLabel(
    FRAME_THREE,
    textvariable=humidity_label_variable,
    font=('Nunito', 25, 'bold'),
    text_color='white'
)
humidity_label.pack(anchor=ctk.SE)

humidity_sub_label_variable = ctk.StringVar()
humidity_sub_label = ctk.CTkLabel(
    FRAME_CENTER,
    textvariable=humidity_sub_label_variable,
    font=('Nunito', 14, 'bold')
)
humidity_sub_label.place(
    x=50,
    y=305
)

HUMIDITY_BAR = ctk.CTkProgressBar(
    FRAME_CENTER,
    width=0,
    height=12,
    corner_radius=50,
    progress_color='purple',
    mode='determinate'
)

# -------------------------------------------------------------------------------------------------------------------- #

FRAME_FOUR = ctk.CTkFrame(
    FRAME_CENTER,
    width=150,
    height=40,
    fg_color='#242424'
)
FRAME_FOUR.place(
    x=297,
    y=407
)
FRAME_FOUR.pack_propagate(False)

pressure_label_variable = ctk.StringVar()
pressure_label = ctk.CTkLabel(
    FRAME_FOUR,
    textvariable=pressure_label_variable,
    font=('Nunito', 25, 'bold'),
    text_color='white'
)
pressure_label.pack(anchor=ctk.SE)

pressure_sub_label_variable = ctk.StringVar()
pressure_sub_label = ctk.CTkLabel(
    FRAME_CENTER,
    textvariable=pressure_sub_label_variable,
    font=('Nunito', 14, 'bold')
)
pressure_sub_label.place(
    x=50,
    y=415
)

PRESSURE_BAR = ctk.CTkProgressBar(
    FRAME_CENTER,
    width=0,
    height=12,
    corner_radius=50,
    progress_color='purple',
    mode='determinate'
)

# -------------------------------------------------------------------------------------------------------------------- #

FRAME_FIVE = ctk.CTkFrame(
    FRAME_CENTER,
    width=150,
    height=40,
    fg_color='#242424'
)
FRAME_FIVE.place(
    x=297,
    y=517
)
FRAME_FIVE.pack_propagate(False)

wind_speed_label_variable = ctk.StringVar()
wind_speed_label = ctk.CTkLabel(
    FRAME_FIVE,
    textvariable=wind_speed_label_variable,
    font=('Nunito', 25, 'bold'),
    text_color='white'
)
wind_speed_label.pack(anchor=ctk.SE)

wind_speed_sub_label_variable = ctk.StringVar()
wind_speed_sub_label = ctk.CTkLabel(
    FRAME_CENTER,
    textvariable=wind_speed_sub_label_variable,
    font=('Nunito', 14, 'bold')
)
wind_speed_sub_label.place(
    x=50,
    y=525
)

WIND_SPEED_BAR = ctk.CTkProgressBar(
    FRAME_CENTER,
    width=0,
    height=12,
    corner_radius=50,
    progress_color='purple',
    mode='determinate'
)

CURRENT_WEATHER_LABEL = ctk.CTkLabel(
    FRAME_CENTER,
    text='Current Statistics',
    text_color='white',
    font=('Nunito', 16, 'bold')
)
# -------------------------------------------------------------------------------------------------------------------- #

FEW_CLOUDS_SYMBOL_DAY = ctk.CTkImage(
    light_image=Image.open('Cloud-Sun.png'),
    dark_image=Image.open('Cloud-Sun.png'),
    size=(256, 256)
)
FEW_CLOUDS_SYMBOL_NIGHT = ctk.CTkImage(
    light_image=Image.open('Cloud-Moon.png'),
    dark_image=Image.open('Cloud-Moon.png'),
    size=(210, 210)
)
SCATTERED_CLOUDS_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Scattered-Clouds.png'),
    dark_image=Image.open('Scattered-Clouds.png'),
    size=(256, 256)
)
BROKEN_CLOUDS_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Broken-Clouds.png'),
    dark_image=Image.open('Broken-Clouds.png'),
    size=(256, 256)
)
OVERCAST_CLOUDS_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Broken-Clouds.png'),
    dark_image=Image.open('Broken-Clouds.png'),
    size=(210, 210)
)

CLEAR_SKY_SYMBOL_DAY = ctk.CTkImage(
    light_image=Image.open('Sun.png'),
    dark_image=Image.open('Sun.png'),
    size=(256, 256)
)
CLEAR_SKY_SYMBOL_NIGHT = ctk.CTkImage(
    light_image=Image.open('Moon.png'),
    dark_image=Image.open('Moon.png'),
    size=(256, 256)
)

ATMOSPHERE_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Mist.png'),
    dark_image=Image.open('Mist.png'),
    size=(256, 256)
)

SNOW_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Weather-Snow.png'),
    dark_image=Image.open('Weather-Snow.png'),
    size=(256, 256)
)

RAIN_SYMBOL_DAY = ctk.CTkImage(
    light_image=Image.open('Rain-Sun.png'),
    dark_image=Image.open('Rain-Sun.png'),
    size=(256, 256)
)
RAIN_SYMBOL_NIGHT = ctk.CTkImage(
    light_image=Image.open('Rain-Moon.png'),
    dark_image=Image.open('Rain-Moon.png'),
    size=(210, 210)
)
SHOWER_RAIN_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Shower-Rain.png'),
    dark_image=Image.open('Shower-Rain.png'),
    size=(256, 256)
)
FREEZING_RAIN_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Weather-Snow.png'),
    dark_image=Image.open('Weather-Snow.png'),
    size=(256, 256)
)

DRIZZLE_SYMBOL = ctk.CTkImage(
    light_image=Image.open('Shower-Rain.png'),
    dark_image=Image.open('Shower-Rain.png'),
    size=(256, 256)
)

THUNDERSTORM_SYMBOL = ctk.CTkImage(
    light_image=Image.open('ThunderStorm.png'),
    dark_image=Image.open('ThunderStorm.png'),
    size=(256, 256)
)

SYMBOL_FRAME = ctk.CTkFrame(
    FRAME_LEFT,
    width=175,
    height=175
)
SYMBOL_FRAME.pack_propagate(False)

WEATHER_SYMBOL_LABEL = ctk.CTkLabel(
    SYMBOL_FRAME,
    width=175,
    height=175,
    text='',
    anchor='center'
)
WEATHER_SYMBOL_LABEL.pack_propagate(False)

WEATHER_DESCRIPTION_VARIABLE = ctk.StringVar()
WEATHER_DESCRIPTION_LABEL = ctk.CTkLabel(
    FRAME_LEFT,
    width=175,
    height=50,
    textvariable=WEATHER_DESCRIPTION_VARIABLE,
    font=('Nunito', 22, 'bold')
)
WEATHER_DESCRIPTION_LABEL.pack_propagate(False)

# -------------------------------------------------------------------------------------------------------------------- #

transition_animator()

# -------------------------------------------------------------------------------------------------------------------- #

ROOT.mainloop()
