

const element2 = document.querySelector('.square2')

let dragging2 = false

// Начальные координаты
let startX2 = 0
let startY2 = 10

// Событие при перетаскивании элемента
element2.addEventListener('mousedown', (e) => {
  dragging2 = true

  startX2 = e.pageX - Number.parseInt(element2.style.left || 0)
  startY2 = e.pageY - Number.parseInt(element2.style.top || 0)
})

// Обрабатываем событие перемещения мыши по <body>
document.body.addEventListener('mousemove', (e) => {
  // Элемент не перетаскивают
  if (!dragging2) return

  // Элемент перетаскивают
  element2.style.top = `${e.pageY - startY2}px`
  element2.style.left = `${e.pageX - startX2}px`
})

// Отпускаем мышь
document.body.addEventListener('mouseup', () => {
  dragging2 = false
})