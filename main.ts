input.onButtonPressed(Button.A, function () {
    radio.sendValue("Passos", totalPassos)
    radio.sendValue("Batim", totalBatimentos)
    basic.showIcon(IconNames.Yes)
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    totalBatimentos = 0
    totalPassos = 0
    basic.showIcon(IconNames.StickFigure)
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    totalBatimentos += 1
    basic.showIcon(IconNames.Yes)
    basic.pause(1000)
    basic.clearScreen()
})
// O que precisamos definir para poder enviar essas informações para outro grupo de rádio específico?
radio.onReceivedValue(function (name, value) {
    // Qual é o valor recebido que devemos colocar para adicionar o comparativo de "Passos" ?
    if (name == "Passos") {
        basic.showString("IT")
        basic.showNumber(value)
        basic.pause(500)
        basic.clearScreen()
    }
    // Qual é o valor recebido que devemos colocar para adicionar o comparativo de "Passos" ?
    if (name == "Batim") {
        basic.showString("FC")
        // Qual valor será necessário encontrar para calcular os batimentos cardíacos x 60?
        basic.showNumber(value * 60)
        basic.pause(1000)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.ThreeG, function () {
    totalPassos += 1
})
let totalBatimentos = 0
let totalPassos = 0
radio.setGroup(1)
basic.showIcon(IconNames.Ghost)
basic.pause(500)
basic.showString("Servidor")
