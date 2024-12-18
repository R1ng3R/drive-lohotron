

const element6 = document.querySelector('.square6')

let dragging6 = false

// Начальные координаты
let startX6 = 0
let startY6 = 30

// Событие при перетаскивании элемента
element6.addEventListener('mousedown', (e) => {
  dragging6 = true

  startX6 = e.pageX - Number.parseInt(element6.style.left || 0)
  startY6 = e.pageY - Number.parseInt(element6.style.top || 0)
})

// Обрабатываем событие перемещения мыши по <body>
document.body.addEventListener('mousemove', (e) => {
  // Элемент не перетаскивают
  if (!dragging6) return

  // Элемент перетаскивают
  element6.style.top = `${e.pageY - startY6}px`
  element6.style.left = `${e.pageX - startX6}px`
})

// Отпускаем мышь
document.body.addEventListener('mouseup', () => {
  dragging6 = false
})