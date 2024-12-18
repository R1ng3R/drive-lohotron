

const element1 = document.querySelector('.square1')

let dragging1 = false

// Начальные координаты
let startX1 = 0
let startY1 = 0

// Событие при перетаскивании элемента
element1.addEventListener('mousedown', (e) => {
  dragging1 = true

  startX1 = e.pageX - Number.parseInt(element1.style.left || 0)
  startY1 = e.pageY - Number.parseInt(element1.style.top || 0)
})

// Обрабатываем событие перемещения мыши по <body>
document.body.addEventListener('mousemove', (e) => {
  // Элемент не перетаскивают
  if (!dragging1) return

  // Элемент перетаскивают
  element1.style.top = `${e.pageY - startY1}px`
  element1.style.left = `${e.pageX - startX1}px`
})

// Отпускаем мышь
document.body.addEventListener('mouseup', () => {
  dragging1 = false

  x1 = document.getElementById("x1")
  y1 = document.getElementById("y1")
  x1.value = parseInt(element1.style.left, 10)
  y1.value = parseInt(element1.style.top, 10)

  x2 = document.getElementById("x2")
  y2 = document.getElementById("y2")
  x2.value = parseInt(element2.style.left, 10)
  y2.value = parseInt(element2.style.top, 10) +  10

  x3 = document.getElementById("x3")
  y3 = document.getElementById("y3")
  x3.value = parseInt(element3.style.left)
  y3.value = parseInt(element3.style.top, 10) +  20

  x4 = document.getElementById("x4")
  y4 = document.getElementById("y4")
  x4.value = parseInt(element4.style.left)
  y4.value = parseInt(element4.style.top, 10) +  30

  x5 = document.getElementById("x5")
  y5 = document.getElementById("y5")
  x5.value = parseInt(element5.style.left)
  y5.value = parseInt(element5.style.top, 10) +  40

  x6 = document.getElementById("x6")
  y6 = document.getElementById("y6")
  x6.value = parseInt(element6.style.left)
  y6.value = parseInt(element6.style.top, 10) +  50
})