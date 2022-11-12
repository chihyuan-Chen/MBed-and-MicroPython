#載入函式庫 
import pyb
from pyb import PWM
from pyb import Pin
from pyb import UART

#設定 PWM 初始化
bpwm1 = PWM(1, freq = 2)
bpwm2 = PWM(1, freq = 2)
bpwm3 = PWM(1, freq = 2)
bpwm4 = PWM(1, freq = 2)

#設定 UART 初始化
uart = UART(1, 9600, bits=8, parity=None, stop=1) # initiate UART1

#定義車輛動作
#向前行
def forward():
    bpwm1ch4 = bpwm1.channel(mode = PWM.OUTPUT, pulse_width_percent = 100, pin = Pin.board.A1)
    bpwm2ch5 = bpwm2.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A0)
    bpwm3ch2 = bpwm3.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A3)
    bpwm4ch3 = bpwm4.channel(mode = PWM.OUTPUT, pulse_width_percent = 100, pin = Pin.board.A2)
    pyb.delay(100)

#停止、回復初始狀態
def stop():
    bpwm1ch4 = bpwm1.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A1)
    bpwm2ch5 = bpwm2.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A0)
    bpwm3ch2 = bpwm3.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A3)
    bpwm4ch3 = bpwm4.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A2)
    pyb.delay(100)

#向右修正
def right():
    bpwm1ch4 = bpwm1.channel(mode = PWM.OUTPUT, pulse_width_percent = 100, pin = Pin.board.A1)
    bpwm2ch5 = bpwm2.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A0)
    bpwm3ch2 = bpwm3.channel(mode = PWM.OUTPUT, pulse_width_percent = 70, pin = Pin.board.A3)
    bpwm4ch3 = bpwm4.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A2)
    pyb.delay(100)

#向左修正
def left():
    bpwm1ch4 = bpwm1.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A1)
    bpwm2ch5 = bpwm2.channel(mode = PWM.OUTPUT, pulse_width_percent = 70, pin = Pin.board.A0)
    bpwm3ch2 = bpwm3.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A3)
    bpwm4ch3 = bpwm4.channel(mode = PWM.OUTPUT, pulse_width_percent = 100, pin = Pin.board.A2)
    pyb.delay(100)

#微向右修正
def slow_right():
    bpwm1ch4 = bpwm1.channel(mode = PWM.OUTPUT, pulse_width_percent = 70, pin = Pin.board.A1)
    bpwm2ch5 = bpwm2.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A0)
    bpwm3ch2 = bpwm3.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A3)
    bpwm4ch3 = bpwm4.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A2)
    pyb.delay(100)

#微向左修正
def slow_left():
    bpwm1ch4 = bpwm1.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A1)
    bpwm2ch5 = bpwm2.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A0)
    bpwm3ch2 = bpwm3.channel(mode = PWM.OUTPUT, pulse_width_percent = 0, pin = Pin.board.A3)
    bpwm4ch3 = bpwm4.channel(mode = PWM.OUTPUT, pulse_width_percent = 70, pin = Pin.board.A2)
    pyb.delay(100)

while (1):
    # 等待 UART 接收資料
    if uart.any() != 0 :

        # 預設動作為前進
        forward()

        # 讀取資料並暫存至參數"temp"
        temp = uart.read(1)

        #判別資料類別(1:代表向左偏移 2:代表向前傾、向後傾或靜止 3:代表向右偏移)
        if temp == b'1':
            stop()

            #向右修正
            right()
            pyb.delay(300)

            #微向左修正
            slow_left()
            pyb.delay(100)

        elif temp == b'3':
            stop()

            #向左修正
            left()
            pyb.delay(300)

            #微向右修正
            slow_right()
            pyb.delay(100)
    