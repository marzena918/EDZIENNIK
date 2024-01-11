function createMenu(parentObject) {
    const marksForStudents = document.createElement("a");
    marksForStudents.href='/marksForStudents';
    marksForStudents.innerHTML='marks for student';
    const marksForParents = document.createElement("a");
    marksForParents.href='/marks_for_parents';
    marksForParents.innerHTML= 'marks for parent';
    const lessonPlanForStudent = document.createElement("a");
    lessonPlanForStudent.href='/LessonPlanForStudents';
    lessonPlanForStudent.innerHTML = 'LessonPlanForStudents';
    const classs = document.createElement("a");
    classs.href = "/class";
    classs.innerHTML = 'class';
    const parents = document.createElement("a");
    parents.href="/parents"
    parents.innerHTML ='parents'
    const LessonPlanForParents = document.createElement("a");
    LessonPlanForParents.href="/LessonPlanForParents"
    LessonPlanForParents.innerHTML ='LessonPlanForParents'
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
    const configurationHours = document.createElement("a");
    configurationHours.href = "/configuration_hours";
    configurationHours.innerHTML = 'configuration hours';
    const lessonPlan = document.createElement("a");
    lessonPlan.href="/lessonPlan";
    lessonPlan.innerHTML= 'lesson plan';
    const attendance = document.createElement("a");
    attendance.href = "/attendance";
    attendance.innerHTML = 'attendance';
    parentObject.appendChild(attendance);
    parentObject.appendChild(lessonPlan);
    parentObject.appendChild(configurationHours);
    parentObject.appendChild(nauczyciele);
    parentObject.appendChild(subjects);
    parentObject.appendChild(index);
    parentObject.appendChild(marks);
    parentObject.appendChild(classs);
    parentObject.appendChild(parents);
    parentObject.appendChild(LessonPlanForParents);
    parentObject.appendChild(lessonPlanForStudent);
    parentObject.appendChild(marksForParents);
    parentObject.appendChild(marksForStudents);
}
