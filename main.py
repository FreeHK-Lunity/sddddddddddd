def Turn_right():
    CUHK_JC_iCar.car_ctrl_speed(CUHK_JC_iCar.CarState.SPIN_RIGHT, 10)
def Turn_left():
    CUHK_JC_iCar.car_ctrl_speed(CUHK_JC_iCar.CarState.SPIN_LEFT, 10)
def move_forward():
    CUHK_JC_iCar.car_ctrl_speed(CUHK_JC_iCar.CarState.FORWARD, 80)
xeee = 0
husk_appear3 = False
husk_appear2 = False
husk_appear = False
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.OBJECTCLASSIFICATION)

def on_forever():
    global husk_appear, husk_appear2, husk_appear3, xeee
    husk_appear = huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK)
    husk_appear2 = huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK)
    husk_appear3 = huskylens.is_appear(3, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK)
    xeee = 999
    if husk_appear == True and husk_appear2 == False or husk_appear3 == False:
        xeee = 1
    elif husk_appear2 == True and husk_appear == False:
        xeee = 2
    elif husk_appear3 == True and husk_appear == False:
        xeee = 3
    else:
        pass
    if xeee == 1:
        basic.show_icon(IconNames.SCISSORS)
    if xeee == 2:
        Turn_right()
        move_forward()
        basic.show_icon(IconNames.HEART)
    if xeee == 3:
        Turn_left()
        move_forward()
        basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
