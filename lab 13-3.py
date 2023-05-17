class TV:
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volume = volume
        print('tv state:',str(self.power),',channel:', str(self.channel), ',volume:',str(self.volume))

    def turnon(self):
        self.power = True
        print('tv state:', str(self.power), ',channel:', str(self.channel), ',volume:', str(self.volume))
    def turnoff(self):
        self.power = False
        self.volume = 0
        self.channel = 0
        print('tv state:', str(self.power), ',channel:', str(self.channel), ',volume:', str(self.volume))

    def setVolume(self,a):
        if self.power:
            self.volume = a
            print('tv state:', str(self.power), ',channel:', str(self.channel), ',volume:', str(self.volume))
        else:
            self.volume = 0
            print('tv state:', str(self.power), ',channel:', str(self.channel), ',volume:', str(self.volume))

    def setChannel(self,a):
        if self.power:
            self.channel = a
            print('tv state:', str(self.power), ',channel:', str(self.channel), ',volume:', str(self.volume))
        else:
            self.channel = 0
            print('tv state:', str(self.power), ',channel:', str(self.channel), ',volume:', str(self.volume))
tv1 = TV(power=False, channel=0, volume=0)
while True :
    strTVOn = "TV on"
    strTVOff = "TV off"
    strSetCh = "Set ch"
    strSetVol = "Set vol"
    selOpt = input("Select Function: %s, %s, %s x, %s x: " %(strTVOn, strTVOff, strSetCh, strSetVol))
    x = int(input('x:'))
    if selOpt =="TV on":
        tv1.turnon()
    elif selOpt == "TV off":
        tv1.turnoff()
    elif selOpt == "Set ch":
        tv1.setChannel(x)
    elif selOpt == "Set vol":
        tv1.setVolume(x)
