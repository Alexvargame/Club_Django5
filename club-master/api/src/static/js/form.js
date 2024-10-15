var formfield = document.getElementById('formfield');

function add(){
  let newFieldStack = document.createElement('input');
  newFieldStack.setAttribute('type','text');
  newFieldStack.setAttribute('name','stack');
  newFieldStack.setAttribute('class','text');
  newFieldStack.setAttribute('placeholder','Satck');
  formfield.appendChild(newFieldStack);

  let newFieldGrade = document.createElement('input');
  newFieldGrade.setAttribute('type','text');
  newFieldGrade.setAttribute('name','grade');
  newFieldGrade.setAttribute('class','text');
  newFieldGrade.setAttribute('placeholder','Grade');
  formfield.appendChild(newFieldGrade);
}

function remove(){
  let input_tags = formfield.getElementsByTagName('input');
  if(input_tags.length > 2) {
    formfield.removeChild(input_tags[(input_tags.length) - 1]);
  }
}
