const app = Vue.createApp({
    data() {
        return {
            title: "Todo App",
            newTodo: '',
            todos: []
        }
    },
    methods: {
        addToDo() {
            if (this.newTodo === '') 
                alert('Please enter a task')
            else{
                this.todos.push({
                    title: this.newTodo,
                    done: false,
                })
                this.newTodo = ''
            }
        },
        removeToDo(todo) {
            const todoIndex = this.todos.indexOf(todo)
            this.todos.splice(todoIndex, 1)
        },
        allDone() {
            this.todos.forEach(todo => {
                todo.done = true
            })
        },
        removeAll() {
            if(this.todos.length > 0)
                this.todos.splice(0, this.todos.length)
            else
                alert('No task to delete')
        }
    }
})

app.mount('#app')