const addButtonEl = document.querySelector('.js-add-button');
const dropButtonEl = document.querySelector('.js-drop-button');

const placeholderText = document.querySelector('.js-course-input');
const submitButton = document.querySelector('.js-course-submit');

addButtonEl.addEventListener('click', () => {
    if (! addButtonEl.classList.contains('add-selected')) {
        addButtonEl.classList.add('add-selected');
        dropButtonEl.classList.remove('drop-selected');

        submitButton.innerHTML = 'Add';
        submitButton.classList.add('add-selected');
        submitButton.classList.remove('drop-selected');
        submitButton.value = 'add';
    }
})

dropButtonEl.addEventListener('click', () => {
    if (! dropButtonEl.classList.contains('drop-selected')) {
        dropButtonEl.classList.add('drop-selected');
        addButtonEl.classList.remove('add-selected');

        submitButton.innerHTML = 'Drop';
        submitButton.classList.add('drop-selected');
        submitButton.classList.remove('add-selected');
        submitButton.value = 'delete';
    }
})