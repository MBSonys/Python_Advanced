document.getElementById("test_button").addEventListener("click", () => {
    let question_count = document.getElementById("question_count").value;
    let answer_count = document.getElementById("answer_count").value;
    let wrapper_to_append = document.getElementById("test_table");
    for (var i = 0; i < question_count; i++) {
        var question_label = document.createElement("label");
        question_label.setAttribute('for', "test_question_" + i);
        question_label.innerHTML = "Klausimas nr: " + (i + 1);
        var question_input = document.createElement("input");
        question_input.setAttribute("name", "test_question");
        question_input.setAttribute("id", "test_question_" + i);
        wrapper_to_append.append(question_label, question_input)
        for (var j = 0; j < answer_count; j++) {
            var answer_label = document.createElement("label");
            answer_label.setAttribute("for", 'test_answer_' + j);
            answer_label.innerHTML = "Atsakymas nr: " + (j + 1);
            var answer_input = document.createElement("input");
            answer_input.setAttribute("id", "test_answer_" + j );
            answer_input.setAttribute("name", "test_answer");
            answer_input.setAttribute('size', '40');
            wrapper_to_append.append(answer_label, answer_input);
        };
        var right_answer_label = document.createElement('label');
        right_answer_label.setAttribute('for', "right_answer");
        right_answer_label.innerHTML = 'Teisingi atsakymai klausymui nr:' + (i+1);
        var right_answer_input = document.createElement('input');
        right_answer_input.setAttribute("placeholder", "Pvz. 1 arba 2,3");
        right_answer_input.setAttribute("id", "right_answer")
        right_answer_input.setAttribute("name", "right_answer")
        wrapper_to_append.append(right_answer_label, right_answer_input);
    };
}, {once: true});