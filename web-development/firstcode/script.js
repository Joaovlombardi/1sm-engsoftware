//Comandos basicos de console


/* console.log('Hello World!');
console.info('Info');
console.warn('Warning');
console.error('Error');

console.table([
    {id: 1, tarefa: 'Estudar'},
    {id: 2, tarefa: 'Prtaicar'}
])

console.group('Grupo de logs')
console.log('Log 1');
console.log('Log 2');   
console.groupEnd()

console.time('Timer');

if(1 == 2){
    console.error('Erro')
}

console.timeEnd('Timer');

let variavelMutavel = 1
console.log(variavelMutavel)

const variavelImutavel = 1

variavelImutavel = 2 */


//Tipos de dados primitivos


/* let texto = "texto"
console.log(typeof texto)

let numero = 1
console.log(typeof numero)

let boolean = true
console.log(typeof boolean)

let semValor
console.log(typeof semValor)

let nulo = null
console.log(typeof nulo)

let uniqueId = Symbol('id')
console.log(typeof uniqueId)

let bigNumero = 10000000000000n
console.log(typeof bigNumero) */


//Tipo de dados complexos


let tarefa = {id: 1, tarefa: 'Estudar'}
console.log(tarefa.id)
console.log(tarefa.tarefa)

let tasks = [
    {id: 1, tarefa: 'Estudar'},
    {id: 2, tarefa: 'Praticar'}
]

console.log(tasks)
console.log(tasks[0]['id'])
console.log(tasks[1].tarefa)

let hoje = new Date()
console.log(hoje)

let lista = ['Estudar', 'Praticar']
console.log(lista)
console.log(lista[0])

let pattern = /^[a-z]$/i;
console.log(pattern)


