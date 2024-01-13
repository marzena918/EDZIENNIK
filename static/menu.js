function createMenu(parentObject) {
    const classs = document.createElement("a");
    classs.href = "/class";
    classs.innerHTML = 'class';
    const parents = document.createElement("a");
    parents.href="/parents"
    parents.innerHTML ='parents'
    const nauczyciele = document.createElement("a");
    nauczyciele.href = "/teacher";
    nauczyciele.innerHTML = 'teacher';
    const subjects = document.createElement("a");
    subjects.href = "/subject";
    subjects.innerHTML = 'subjects';
    const index = document.createElement("a");
    index.href = "/student";
    index.innerHTML = 'students';
    parentObject.appendChild(nauczyciele);
    parentObject.appendChild(subjects);
    parentObject.appendChild(index);
    parentObject.appendChild(classs);
    parentObject.appendChild(parents);
}
