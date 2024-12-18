

const element5 = document.querySelector('.square5')

let dragging5 = false

// Начальные координаты
let startX5 = 0
let startY5 = 30

// Событие при перетаскивании элемента
element5.addEventListener('mousedown', (e) => {
  dragging5 = true

  startX5 = e.pageX - Number.parseInt(element5.style.left || 0)
  startY5 = e.pageY - Number.parseInt(element5.style.top || 0)
})

// Обрабатываем событие перемещения мыши по <body>
document.body.addEventListener('mousemove', (e) => {
  // Элемент не перетаскивают
  if (!dragging5) return

  // Элемент перетаскивают
  element5.style.top = `${e.pageY - startY5}px`
  element5.style.left = `${e.pageX - startX5}px`
})

// Отпускаем мышь
document.body.addEventListener('mouseup', () => {
  dragging5 = false
})