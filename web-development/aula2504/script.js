// Tipos de array

/*  
const tarefas = ['Estudar js', 'Criar projeto', 'Preparar apresentacao', 'Revisar codigo']
console.table(tarefas)
 
const categorias = new Array('Trabalho','Estudo','Pessoal','Projetos')
console.table(categorias)
 
const propriedades = Array.of('baixa', 'media', 'alta')
console.table(propriedades)
 
const letras = Array.from('Daniel')
console.table(letras)
*/

// -------------------------------------------------------------------------------------------

// Alterando valores nos indices do array

/*
const tarefas = ['Estudar js', 'Criar projeto', 'Preparar apresentacao', 'Revisar codigo']
console.table(tarefas)
console.log(tarefas[0]);
 
tarefas[1] = 'Criar projeto novo'
console.table(tarefas)
 
tarefas.push('Relizar testes') // .push adiciona o elemento ao fim do array
console.table(tarefas);
 
tarefas.unshift('Revisar documentacao') // .unshift adiciona o elemento no inicio do array
console.table(tarefas)
 
tarefas.shift() // .shift remove o primeiro elemento do array
console.table(tarefas)
 
tarefas.pop() // .pop remove o ultimo elemento do array
console.table(tarefas)
 
tarefas.splice(1, 2, 'Pinto', 'Pau') // recebe o indice e quantos elementos ele remove
console.table(tarefas)
*/

// -------------------------------------------------------------------------------------------

// const tarefas = ['Estudar js', 'Criar projeto', 'Preparar apresentacao', 'Revisar codigo']

// const executarForEach = (elemento, indice) => {
//     console.log(`${indice + 1}. ${elemento} `)
// }

// tarefas.forEach(executarForEach)

// const arrayNovo = tarefas.map
// ((elemento, indice) => {
//     return elemento + "- Concluido"
// })

// console.table(arrayNovo)

// const tarefasComA = tarefas.filter
// (elemento => elemento.toLowerCase().includes("a"))

// console.log(tarefasComA)

// const IndiceTarefaEncontrada = tarefas.findIndex(elemento => elemento.includes("JS"))

// console.log(IndiceTarefaEncontrada)

// tarefas.splice(IndiceTarefaEncontrada, 1)

// console.log(tarefas)

// const valorFinal = tarefas.reduce((total, t, indice) => 
//     total + t.length, 0)

// console.log(valorFinal)

// const tarefa = {
//     id: 1,
//     titulo: "Aprender sobre objetos",
//     descricao: "Estudar propriedades e métodos",
//     concluida: false,
//     prioridade: "alta",
//     dataCriacao: new Date()
// }

// console.log(tarefa)
// console.log(tarefa?.titulo)
// console.log(tarefa['titulo'])

// const tarefasEspeciais = {
//     "data-criacao": new Date(),
//     "nome da tarefa": "nome da tarefa separado"
// }

// console.log(tarefasEspeciais["nome da tarefa"])

// console.log(tarefasEspeciais["data-criacao "])


// const prioridades = ["baixo", "media", "alta"]

// const [baixa, media, alta] = prioridades

// console.log(baixa, media, alta)

// const categorias = ["Trabalhos", "Estudos", "Pessoal", "Saúde"]

// const [primeiraCategoria, ... outrasCategorias] = categorias

// console.log(primeiraCategoria, outrasCategorias)

// const projetoTaskMaster = {
//     nome: "TaskMaster",
//     version: "1.0",
//     autor: "Curso JavaScript",
//     tarefas: [],
// }

// const {nome, version, ... outrasProps} = projetoTaskMaster

// console.log(nome)
// console.log(version)
// console.log(outrasProps)