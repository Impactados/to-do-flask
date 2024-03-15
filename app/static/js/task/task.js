$(document).ready(function() {
    loadData()
})

async function loadData(){
    await fetch('/api/v1/get_task/1', {
        method: 'GET',
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      })
      .then(response => response.json())
      .then(json => {
            data = json.data
            console.log(data)
            data.forEach(element => {
                const taskList = document.getElementById('task-list');
                const taskItem = document.createElement('li');
                taskItem.classList.add('list-group-item');
                taskItem.innerHTML = `<strong>${element[1]}</strong>: ${element[2]}`;
                taskList.appendChild(taskItem);
          
            });
      })
}

function addTask() {
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-description').value;
  
    if (title && description) {
      // Simulando uma requisição AJAX
      fetch('/api/v1/task', {
        method: 'POST',
        body: JSON.stringify(
            { 
                title: title, 
                description: description, 
                user_id: 1 
            }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      })
      .then(response => response.json())
      .then(json => {
        const taskList = document.getElementById('task-list');
        const taskItem = document.createElement('li');
        taskItem.classList.add('list-group-item');
        taskItem.innerHTML = `<strong>${title}</strong>: ${description}`;
        taskList.appendChild(taskItem);
      })
      .catch(err => console.error('Erro ao adicionar a tarefa:', err));
    } else {
      alert('Por favor, preencha todos os campos.');
    }
  }
  