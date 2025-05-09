// const titulo = document.querySelector('h1')

// titulo.textContent = "Novo Titulo"

// const div = document.querySelector('#container')

// div.innerHTML = '<p> Novo parágrafo <b>HTML</b> </p>'

// const imagem = document.querySelector('img')

// //imagem.setAttribute('src', 'images/avatar.jpg')
// imagem.src = 'images/avatar.jpg'
// imagem.setAttribute('width', '200px') //Esse aqui precisa amigão
// imagem.alt = 'Avatar Profile'

// const caixa = document.querySelector('.box')
// const botao = document.getElementById('meuBotao')

// botao.addEventListener('click', () => {
//     caixa.classList.toggle('oculta')
// })

// const novoItem = document.createElement('li')
// novoItem.textContent = 'Novo Item'
// const novoItem2 = document.createElement('li')
// novoItem2.textContent = 'Novo Item2'

// document.querySelector('ul').appendChild(novoItem)
// document.querySelector('ul').appendChild(novoItem2)

// localStorage.setItem('nome', 'João Vitor')
// localStorage.setItem('nome2', 'Rafael')


// const nome = localStorage.getItem('nome')
// console.log(nome)

// //localStorage.removeItem('nome2')
// //localStorage.clear()

// const usuario = {nome: 'João Vitor', idade: 18}
// localStorage.setItem('usuario', JSON.stringify(usuario))

// const usuarioRecuperado = JSON.parse(localStorage.getItem('usuario'))
// console.log(usuarioRecuperado)

let tarefas = JSON.parse(localStorage.getItem("tarefas")) || []

function renderizarTarefas() {
    const lista = document.getElementById("lista-tarefas");
    lista.innerHTML = "";
    tarefas.forEach((t, i) => {
      const li = document.createElement("li");
      li.textContent = t;
      lista.appendChild(li);
    });
  }

  renderizarTarefas()

  document.getElementById("form-tarefa").onsubmit = (e) => {
    e.preventDefault(); // não recarrega a página ao submeter
    const input = document.getElementById("input-tarefa");
    tarefas.push(input.value);
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
    input.value = "";
    renderizarTarefas();
  };

  document.getElementById("btn-limpar").onclick = () => {
    tarefas = [];
    localStorage.removeItem("tarefas");
    renderizarTarefas();
  };
