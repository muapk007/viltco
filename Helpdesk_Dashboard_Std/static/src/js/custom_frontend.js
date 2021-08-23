    $(document).ready(function(){
        $(".add-row").click(function(){
            var name = $("#name").val();
            var email = $("#email").val();
            var address = $("#address").val();
            var work_position = $("#work_position").val();
            var lines = $("#lines").val();
            var markup = "<tr><td>" + name + "</td><td>" + email + "</td><td>" + address + "</td><td>" + work_position + "</td><td>" + lines + "</td></tr>";
            $("table tbody").append(markup);
        });
        
        
    });    

$(function() {
    $('#work_position').change(function() {
        localStorage.setItem('todoData', this.value);
    });
    if(localStorage.getItem('todoData')){
        $('#work_position').val(localStorage.getItem('todoData'));
    }
});



    $(document).ready(function(){
        $(".add-child-row").click(function(){
            var name = $("#name").val();
            var age = $("#age").val();
            var gender = $("#gender").val();
            var markup = "<tr><td>" + name + "</td><td>" + age + "</td><td>" + gender + "</td></tr>";
            $("table tbody").append(markup);
        });
        
        
    }); 


//

$(document).ready(function(){

var i=2;
  $(".addmore").on('click',function(){
    var data="<tr><td>"+i+".</td>";
        data +="<td><input type='text' id='name"+i+"' name='name[]'/></td> <td><input type='text' id='age"+i+"' name='age[]'/></td><td><input type='text' id='gender"+i+"' name='gender[]'/></td></tr>";
        $('table').append(data);
        i++;
});
    
    
    });