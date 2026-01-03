
const courseButtonEl = document.querySelector('.js-course-list');
const tableEl = document.querySelector('.staff-course-table');

courseButtonEl.addEventListener('click', () => {
    if (!courseButtonEl.classList.contains('selected-button')) {
        courseButtonEl.classList.add('selected-button');
        console.log(courses);
    }

})

document.querySelectorAll(".js-students-button").forEach((button) => {
    button.addEventListener('click', () => {
        const courseCode = button.dataset.courseCode;
    })
})
