$(document).ready(function(){
    var todo_id = $("#todo-id").val();
    //console.log(todo_id);

    $.ajax({
        url : "https://jsonplaceholder.typicode.com/todos/"+todo_id,
        type : "GET",
        success : function(todo){
            $("#todoid").text(todo.id);
            $("#user-id").text(todo.userId);
            $("#title").text(todo.title);
            $("#completed").text(todo.completed);       
        },

        error : function(error){
            console.log(error);
        }   
    });


 });