//Functions for table.html



//global array to hold each row's input id's, in order to keep track of if the following functions ran on that input.
const ids=[];
const rows=[];

function isit(z){
    //
        //if a row's input id is not in the array, the function has not run. So we can add that id to the array to keep track if the function executed on that particular id.
        if (ids.indexOf(z) === -1){
        ids.push(z);
         return false;
    }
    else{
        //stop the function if this id already executed before.
        return true;
    }
}


 function set_id(x){
    //set a random number to the row's input id, so each id is unique.
    var r = Math.floor(Math.random() * 1000 );
     x.setAttribute("id", r);
     
 }
 

function addRow(e){
   
    
    //grab table so we can insert row
    var table= document.getElementById("table2");


    //if function already ran for this id, return.
    if (isit(e) === true){
        return;
    }
    else{

    var row = table.insertRow();
    //grab original row so we can copy innerhtml to the new row
    var original = document.getElementById("rowToClone")
    row.innerHTML = original.innerHTML;
    row.setAttribute('onclick','addEdit(this)')
    //grab input element within new row, so we can set its id to unique
    var input = row.querySelector('input');
    set_id(input);
    }
    }


function addEdit(elem){
   
    if(rows.length === 0){
    
    var row = elem;
    var cell = row.querySelector("td");
    rows.push(cell);
    console.log(rows);
    cell.innerHTML = '<i style="text-align: center; float: center;" class="fa-solid fa-pen fa-bounce"></i>';
    }
    else{
        rows[0].innerHTML="";
        rows.pop();
        addEdit(elem);
    }
 
}
