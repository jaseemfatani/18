if input.temperature() > 0:
    basic.show_string("The temperature is above zero")
    if input.temperature() < 0:
        basic.show_string("The temperature is below zero")
    else:
        basic.show_string("The temperature is zero")