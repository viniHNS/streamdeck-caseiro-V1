import board
import busio
import displayio
import terminalio
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_sh1107
from i2cdisplaybus import I2CDisplayBus
import simpleio  
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

touch_pin = digitalio.DigitalInOut(board.GP29)  
touch_pin.direction = digitalio.Direction.INPUT                                    
touch_pin.pull = digitalio.Pull.DOWN

confirm_pin = digitalio.DigitalInOut(board.GP14)  
confirm_pin.direction = digitalio.Direction.INPUT
confirm_pin.pull = digitalio.Pull.DOWN

BUZZER_PIN = board.GP16  

# Nomes dos botões
messages = ["Atumalaca", "Bla Bla", "Nossaaa", "Discord", "Steam", "Som Corsa", "Bombardilo", "Caramba", "Controle tv", "Let me Now", "Medo"]

key_mapping = [
    Keycode.KEYPAD_ONE,         # "Atumalaca"   -> Num1
    Keycode.KEYPAD_TWO,         # "Bla Bla"     -> Num2
    Keycode.KEYPAD_THREE,       # "Nossaaa"     -> Num3
    Keycode.KEYPAD_FOUR,        # "Discord"     -> Num4
    Keycode.KEYPAD_FIVE,        # "Steam"       -> Num5
    Keycode.KEYPAD_SIX,         # "Som Corsa"   -> Num6
    Keycode.KEYPAD_SEVEN,       # "Bombardilo"  -> Num7
    Keycode.KEYPAD_EIGHT,       # "Caramba"     -> Num8
    Keycode.KEYPAD_NINE,        # "Controle TV" -> Num9
    Keycode.KEYPAD_MINUS,       # "Let me Now"  -> Num-
    Keycode.KEYPAD_ASTERISK,    # "Medo"        -> Num*
]

current_message = 0

displayio.release_displays()
i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=128, height=128, rotation=90, display_offset=0
)

main = displayio.Group()
display.root_group = main

text_label = label.Label(terminalio.FONT, text=messages[current_message], color=0xFFFFFF, scale=2)

def center_text():
    text_width = len(text_label.text) * 6 * 2  # 6px largura base por carácter * escala 2
    text_label.x = (136 - text_width) // 2
    text_label.y = 60  

def play_beep():
    simpleio.tone(BUZZER_PIN, 2000, 0.04)

def play_confirm_beep():
    simpleio.tone(BUZZER_PIN, 1500, 0.1)
    time.sleep(0.05)
    simpleio.tone(BUZZER_PIN, 1800, 0.1)

center_text()
main.append(text_label)

last_touch_state = False
last_press_time = 0
debounce_time = 0.3 

last_confirm_state = False
last_confirm_time = 0
confirm_debounce = 0.3  

long_press_time = 1.0  
button_hold_start = 0  
is_long_press_sent = False  

status_label = label.Label(terminalio.FONT, text="", color=0xFFFFFF, scale=1)
status_label.x = 5
status_label.y = 110
main.append(status_label)

while True:
    current_time = time.monotonic()
    
    current_touch_state = touch_pin.value
    if current_touch_state and not last_touch_state and (current_time - last_press_time) > debounce_time:
        play_beep()
        current_message = (current_message + 1) % len(messages)
        text_label.text = messages[current_message]
        status_label.text = f"Num{current_message + 1}"
        center_text()
        last_press_time = current_time
    
    current_confirm_state = confirm_pin.value
    
    if current_confirm_state and not last_confirm_state:
        button_hold_start = current_time 
        is_long_press_sent = False 
    
    if not current_confirm_state and last_confirm_state and not is_long_press_sent and (current_time - button_hold_start) <= long_press_time:
        play_confirm_beep()
        old_text = status_label.text
        status_label.text = "Enviando..."
        keycode = key_mapping[current_message]
        keyboard.press(keycode)
        time.sleep(0.1)
        keyboard.release(keycode)
        time.sleep(0.5)
        status_label.text = old_text
        last_confirm_time = current_time
    
    if current_confirm_state and (current_time - button_hold_start) > long_press_time and not is_long_press_sent:
        status_label.text = "PARANDO..."
        
        simpleio.tone(BUZZER_PIN, 2000, 0.1)
        time.sleep(0.05)
        simpleio.tone(BUZZER_PIN, 1500, 0.1)
        time.sleep(0.05)
        simpleio.tone(BUZZER_PIN, 1000, 0.1)
        
        keyboard.press(Keycode.KEYPAD_ZERO)
        time.sleep(0.1)
        keyboard.release(Keycode.KEYPAD_ZERO)
        
        is_long_press_sent = True
        
        time.sleep(1.0)
        status_label.text = f"Num{current_message + 1}"
    
    last_touch_state = current_touch_state
    last_confirm_state = current_confirm_state

    time.sleep(0.01)