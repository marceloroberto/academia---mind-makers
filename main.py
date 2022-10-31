def on_button_pressed_a():
    radio.send_value("Passos", totalPassos)
    radio.send_value("Batim", totalBatimentos)
    basic.show_icon(IconNames.YES)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global totalBatimentos, totalPassos
    totalBatimentos = 0
    totalPassos += 0
    basic.show_icon(IconNames.STICK_FIGURE)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global totalBatimentos
    totalBatimentos += 1
    basic.show_icon(IconNames.YES)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

"""

O que precisamos definir para poder enviar essas informações para outro grupo de rádio específico?

"""

def on_received_value(name, value):
    # Qual é o valor recebido que devemos colocar para adicionar o comparativo de "Passos" ?
    if name == "Passos":
        basic.show_string("IT")
        basic.show_number(value)
        basic.pause(500)
    # Qual é o valor recebido que devemos colocar para adicionar o comparativo de "Passos" ?
    if name == "Batim":
        basic.show_string("FC")
        # Qual valor será necessário encontrar para calcular os batimentos cardíacos x 60?
        basic.show_number(value * 60)
        basic.pause(1000)
        basic.clear_screen()
radio.on_received_value(on_received_value)

def on_gesture_three_g():
    global totalPassos
    totalPassos += 1
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

totalBatimentos = 0
totalPassos = 0
radio.set_group(1)