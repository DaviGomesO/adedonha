document.addEventListener('DOMContentLoaded', function () {
  const timerElement = document.getElementById('timer')
  const mensagem_tempo = document.getElementById('temporizador')

  let tempo = 5

  function updateTimer() {
    timerElement.innerHTML = tempo.toString()
    tempo--

    if (tempo >= 0) {
      setTimeout(updateTimer, 1000)
    } else {
      mensagem_tempo.style.display = 'none'
    }
  }

  const link_sortear = document.getElementById('link-sortear')

  link_sortear.addEventListener('click', function () {
    mensagem_tempo.style.display = 'flex'
    updateTimer()
  })
})
