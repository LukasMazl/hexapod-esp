LEFT_FRONT_LEG_CODE = "left.front.leg"
LEFT_MID_LEG_CODE = "left.mid.leg"
LEFT_BACK_LEG_CODE = "left.back.leg"

RIGTH_FRONT_LEG_CODE = "righ.front.leg"
RIGTH_MID_LEG_CODE = "righ.mid.leg"
RIGTH_BACK_LEG_CODE = "righ.back.leg"

BODY_SERVO_CODE = "body.servo"
ARM_SERVO_CODE = "arm.servo"
FINGER_SERVO_CODE = "finger.servo.code"

SERVO_CONFIGURATION = {
    LEFT_FRONT_LEG_CODE: {
        BODY_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 90,
            "max": 180,
            "reversed": False
        },
        ARM_SERVO_CODE: {
            "on_pca": True,
            "channel": 1,
            "min": 0,
            "max": 160,
            "reversed": False
        },
        FINGER_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 120,
            "reversed": False
        }
    },
    LEFT_MID_LEG_CODE: {
        BODY_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 100,
            "reversed": False
        },
        ARM_SERVO_CODE: {
            "on_pca": True,
            "channel": 1,
            "min": 0,
            "max": 140,
            "reversed": False
        },
        FINGER_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 170,
            "reversed": False
        },
    },
    LEFT_BACK_LEG_CODE: {
        BODY_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 100,
            "reversed": False
        },
        ARM_SERVO_CODE: {
            "on_pca": True,
            "channel": 1,
            "min": 0,
            "max": 140,
            "reversed": False
        },
        FINGER_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 170,
            "reversed": False
        }
    },
    RIGTH_FRONT_LEG_CODE: {
        BODY_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 90,
            "max": 180,
            "reversed": False
        },
        ARM_SERVO_CODE: {
            "on_pca": True,
            "channel": 1,
            "min": 0,
            "max": 160,
            "reversed": False
        },
        FINGER_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 120,
            "reversed": False
        }
    },
    RIGTH_MID_LEG_CODE: {
        BODY_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 100,
            "reversed": False
        },
        ARM_SERVO_CODE: {
            "on_pca": True,
            "channel": 1,
            "min": 0,
            "max": 140,
            "reversed": False
        },
        FINGER_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 170,
            "reversed": False
        }
    },
    RIGTH_BACK_LEG_CODE: {
        BODY_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 100,
            "reversed": False
        },
        ARM_SERVO_CODE: {
            "on_pca": True,
            "channel": 1,
            "min": 0,
            "max": 140,
            "reversed": False
        },
        FINGER_SERVO_CODE: {
            "on_pca": True,
            "channel": 0,
            "min": 0,
            "max": 170,
            "reversed": False
        }
    }
}


# SERVO_0_DOLE  90 - 180
# SERVO_1_RAMENO  0 - 160
# SERVO_2_RUKA 0 - 120
# SERVO_3_DOLE 0 - 100
# SERVO_4_RAMENO 0 - 140
# SERVO_5_RUKA 0 - 170
# SERVO_6_DOLE  0 - 170
# SERVO_7_RAMENO  0 - 180
# SERVO_8_RUKA 0 - 150
# SERVO_9_DOLE  20 - 140
# SERVO_10_RAMENO  0 - 120
# SERVO_11_RUKA 20 - 140
# SERVO_12_DOLE  80 - 180
# SERVO_13_RAMENO  0 - 120
# SERVO_14_RUKA DODELAT

# SERVO_15_DOLE  40 - 140
# SERVO_16_RAMENO  20 - 180
# SERVO_17_RUKA 30 - 160
