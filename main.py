def Turn_right():
    CUHK_JC_iCar.car_ctrl_speed(CUHK_JC_iCar.CarState.SPIN_RIGHT, 10)
def Turn_left():
    CUHK_JC_iCar.car_ctrl_speed(CUHK_JC_iCar.CarState.SPIN_LEFT, 10)
def move_forward():
    CUHK_JC_iCar.car_ctrl_speed(CUHK_JC_iCar.CarState.FORWARD, 80)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_OBJECT_RECOGNITION)
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
if xeee == 3:
    Turn_left()
    move_forward()

def on_forever():
    pass
basic.forever(on_forever)
