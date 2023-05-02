huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_OBJECT_RECOGNITION)
basic.showString("" + ("" + huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)))
let husk_appear = huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)
let husk_appear2 = huskylens.isAppear(2, HUSKYLENSResultType_t.HUSKYLENSResultBlock)
let husk_appear3 = huskylens.isAppear(3, HUSKYLENSResultType_t.HUSKYLENSResultBlock)
let xeee = 999
if (husk_appear == true && husk_appear2 == false || husk_appear3 == false) {
    xeee = 1
} else if (husk_appear2 == true && husk_appear == false) {
    xeee = 2
} else if (husk_appear3 == true && husk_appear == false) {
    xeee = 3
} else {
    
}

function Turn_right() {
    CUHK_JC_iCar.carCtrlSpeed(CUHK_JC_iCar.CarState.SpinRight, 10)
}

function Turn_left() {
    CUHK_JC_iCar.carCtrlSpeed(CUHK_JC_iCar.CarState.SpinLeft, 10)
}

function move_forward() {
    CUHK_JC_iCar.carCtrlSpeed(CUHK_JC_iCar.CarState.Forward, 80)
}

if (xeee == 1) {
    basic.showIcon(IconNames.Scissors)
}

if (xeee == 2) {
    Turn_right()
    move_forward
}

if (xeee == 3) {
    Turn_left()
    move_forward
}

basic.forever(function on_forever() {
    
})
