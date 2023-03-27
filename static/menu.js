function createMenu(parentObject) {
    const classs = document.createElement("a");
    classs.href = "/class";
    classs.innerHTML = 'class';
    const nauczyciele = document.createElement("a");
    nauczyciele.href = "/teacher";
    nauczyciele.innerHTML = 'teacher';
    const subjects = document.createElement("a");
    subjects.href = "/subject";
    subjects.innerHTML = 'subjects';
    const index = document.createElement("a");
    index.href = "/student";
    index.innerHTML = 'students';
    const marks = document.createElement("a");
    marks.href = "/marks";
    marks.innerHTML = 'marks';
    parentObject.appendChild(classs);
    parentObject.appendChild(nauczyciele);
    parentObject.appendChild(subjects);
    parentObject.appendChild(index);
    parentObject.appendChild(marks);
}
