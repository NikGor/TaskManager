document.addEventListener("DOMContentLoaded", function() {
    // Общая диаграмма
    const overallCtx = document.getElementById('overallChart').getContext('2d');
    const overallData = {
        labels: ['Открытые задачи', 'Завершенные задачи'],
        datasets: [{
            data: [document.getElementById('total_open_tasks').value, document.getElementById('total_tasks').value - document.getElementById('total_open_tasks').value],
            backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
            borderWidth: 1
        }]
    };
    new Chart(overallCtx, {
        type: 'pie',
        data: overallData
    });

    // Диаграммы проектов
    const projectCards = document.querySelectorAll('.card.mb-3'); // Используйте более специфичный селектор, чтобы выбрать только карточки проектов
    projectCards.forEach((projectCard, index) => {
        const projectCtx = projectCard.querySelector(`canvas`).getContext('2d');
        const openTasksValue = projectCard.querySelector('.open_tasks').value;
        const totalTasksValue = projectCard.querySelector('.total_tasks').value;
        const projectData = {
            labels: ['Открытые задачи', 'Завершенные задачи'],
            datasets: [{
                data: [openTasksValue, totalTasksValue - openTasksValue],
                backgroundColor: ['rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)'],
                borderColor: ['rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)'],
                borderWidth: 1
            }]
        };
        new Chart(projectCtx, {
            type: 'pie',
            data: projectData
        });
    });
});
