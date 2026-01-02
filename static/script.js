const stButtonEl = document.querySelector('.js-student-button');
const staffButtonEl = document.querySelector('.js-staff-button');

const stuLoginEl = document.querySelector('.js-login');

//console.log("Script running");

stButtonEl.addEventListener('click', () => {
    //console.log('HEYY');
    if (!stButtonEl.classList.contains("selected-button")) {
        stButtonEl.classList.add('selected-button');
        staffButtonEl.classList.remove('selected-button');

        let stHTML = `<h4 class="login-text">Enter Student ID</h4><form action="/student" method="POST">
                <input class='input-box' type="text" placeholder="ID" name="student-id"><br>
                <input class='input-box' type="password" placeholder="Password" name="student-pass"><br>
                <button class='submit-button login-button' type="submit">Log In</button>
            </form>`;
        stuLoginEl.innerHTML = stHTML;
    }


    })

staffButtonEl.addEventListener('click', () => {
    //console.log('HEYY');
    if (!staffButtonEl.classList.contains("selected-button")) {
        staffButtonEl.classList.add('selected-button');
        stButtonEl.classList.remove('selected-button');
        stuLoginEl.innerHTML = '';

        let staffHTML = `<h4 class="login-text">Enter Staff ID</h4><form action="/staff" method="POST">
                <input class='input-box' type="text" placeholder="ID" name="staff-id"><br>
                <input class='input-box' type="password" placeholder="Password" name="staff-pass"><br>
                <button class='submit-button login-button' type="submit">Log In</button>
            </form>`;
        stuLoginEl.innerHTML = staffHTML;
        
    }

    })