#Variables
speedCmS = 0
def run(speed_km_h: float, horas) -> float:
    # TODO
    global speedCmS
    speedCmS = speed_km_h * (100000 / horas)
    return speedCmS


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(speedCmS)