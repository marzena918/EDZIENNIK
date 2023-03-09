async function get_all_subjects(subjectsSelect) {
    const subjects = await (await fetch('/teacher/get_all_subjects')).json();
    for (const i of subjects) {
        const option = document.createElement("option");
        option.value = i.name;
        option.innerHTML = i.name;
        subjectsSelect.appendChild(option);
    }
}

async function addNewTeacher() {
    const subjects = document.getElementById("subject");
    let listSubjects = Array.from(subjects.selectedOptions).map(element => element.value);
    const name = document.getElementById("imie_id").value;
    const last_name = document.getElementById("nazwisko").value;
    const pesel = +document.getElementById("pesel").value;
    const data = {subjects: listSubjects, name: name, last_name: last_name, pesel: pesel}
    await fetch('/teacher/add', {
        method: 'POST', body: JSON.stringify(data),
        headers: {'Content-Type': 'application/json'}
    })
}

async function getSubjectsOfTeacher(id) {
    return await (await fetch(`/teacher/subjectsOfTeacher/${id}`)).json();
}

async function updateDataTeacher(id) {
    const name = document.getElementById("name_id").value;
    const lastName = document.getElementById("lastName_id").value;
    const pesel = document.getElementById("pesel_id").value;
    const subjects = Array.from(document.getElementById("select_id").selectedOptions).map(element => element.value);
    const data = {name: name, lastName: lastName, pesel: pesel, subjects: subjects, id: id}
    await fetch('/teacher/updateData', {
        method: 'PUT', body: JSON.stringify(data),
        headers: {'Content-Type': 'application/json'}
    });
}

async function isPeselExist(pesel) {
    const response = await fetch(`/teacher/check_pesel/${pesel}`)
    return +(await response.text());
}