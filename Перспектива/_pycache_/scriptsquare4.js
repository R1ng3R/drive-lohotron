

const element4 = document.querySelector('.square4')

let dragging4 = false

// Начальные координаты
let startX4 = 0
let startY4 = 30

// Событие при перетаскивании элемента
element4.addEventListener('mousedown', (e) => {
  dragging4 = true

  startX4 = e.pageX - Number.parseInt(element4.style.left || 0)
  startY4 = e.pageY - Number.parseInt(element4.style.top || 0)
})

// Обрабатываем событие перемещения мыши по <body>
document.body.addEventListener('mousemove', (e) => {
  // Элемент не перетаскивают
  if (!dragging4) return

  // Элемент перетаскивают
  element4.style.top = `${e.pageY - startY4}px`
  element4.style.left = `${e.pageX - startX4}px`
})

// Отпускаем мышь
document.body.addEventListener('mouseup', () => {
  dragging4 = false
})