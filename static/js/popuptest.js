var reciperow = document.getElementsByClassName('stepformrow')

function addRowToRecipe() {
  var recipeTable = document.getElementById('recipe_table');
  var numberOfRows = recipeTable.getElementsByTagName('tr').length;
  var formIWant = recipeTable.getElementsByTagName('tr')[1].cloneNode(true);
  var bodyOfTable = recipeTable.getElementsByTagName('tbody')[0];
  bodyOfTable.append(formIWant);

  var totalFormInput = document.getElementById('id_steps-TOTAL_FORMS');
  var totalFormInputInitialValue = Number(totalFormInput.value)+1;
  var newDescriptionValue = 'steps-'+(totalFormInputInitialValue - 1)

  var lastrow = recipeTable.getElementsByTagName('tr')[totalFormInputInitialValue]
  // lastrow.getElementsByTagName('th')[0].getElementsByTagName('label')[0].htmlFor = 'id_'+newDescriptionValue
  lastrow.getElementsByTagName('td')[0].getElementsByTagName('input')[0].name = newDescriptionValue+'-number'
  lastrow.getElementsByTagName('td')[0].getElementsByTagName('input')[0].id = 'id_'+newDescriptionValue+'-number'
  lastrow.getElementsByTagName('td')[1].getElementsByTagName('select')[0].name = newDescriptionValue+'-ingredient'
  lastrow.getElementsByTagName('td')[1].getElementsByTagName('select')[0].id = 'id_'+newDescriptionValue+'-ingredient'
  lastrow.getElementsByTagName('td')[2].getElementsByTagName('input')[0].name = newDescriptionValue+'-amount'
  lastrow.getElementsByTagName('td')[2].getElementsByTagName('input')[0].id = 'id_'+newDescriptionValue+'-amount'
  lastrow.getElementsByTagName('td')[3].getElementsByTagName('select')[0].name = newDescriptionValue+'-unit'
  lastrow.getElementsByTagName('td')[3].getElementsByTagName('select')[0].id = 'id_'+newDescriptionValue+'-unit'
  totalFormInput.value = totalFormInputInitialValue;
  console.log('additional form added!');
};

function highlightErrors() {
    var recipeTable = document.getElementById('recipe_table');
    var rows = recipeTable.getElementsByTagName('tr');
    var numberOfRowsPlusOne = rows.length;
    for(var i=1; i<numberOfRowsPlusOne; i++){
      var inputCells = rows[i].getElementsByTagName('input');
        for(var j=0; j<inputCells.length; j++){
          inputCells[j].className ='form-control';
          inputCells[j].required ='True';
        }
      var selectCells = rows[i].getElementsByTagName('select');
        for(var k=0; k<selectCells.length; k++){
          selectCells[k].className ='custom-select';
          selectCells[k].required ='True';
        }
    }
};

function showpHStep() {
  var phrow = document.getElementById('phstep');
  phrow.removeAttribute('hidden');
  console.log('PHSTEP!');
};
