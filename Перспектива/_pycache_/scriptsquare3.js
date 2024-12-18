const element3 = document.querySelector('.square3')

let dragging3 = false

// Начальные координаты
let startX3 = 0
let startY3 = 0

// Событие при перетаскивании элемента
element3.addEventListener('mousedown', (e) => {
  dragging3 = true

  startX3 = e.pageX - Number.parseInt(element3.style.left || 0)
  startY3 = e.pageY - Number.parseInt(element3.style.top || 0)
})

// Обрабатываем событие перемещения мыши по <body>
document.body.addEventListener('mousemove', (e) => {
  // Элемент не перетаскивают
  if (!dragging3) return

  // Элемент перетаскивают
  element3.style.top = `${e.pageY - startY3}px`
  element3.style.left = `${e.pageX - startX3}px`
})

// Отпускаем мышь
document.body.addEventListener('mouseup', () => {
  dragging3 = false
})