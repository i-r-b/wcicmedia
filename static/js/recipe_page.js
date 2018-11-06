beautifyRows();
setGlobalNames();


function beautifyRows() {
  var recipeTable = document.getElementById('recipe_table');
  var rows = recipeTable.getElementsByTagName('tr');
  var numberOfRowsPlusOne = rows.length;
  for(var i=1; i<numberOfRowsPlusOne; i++){
    var inputCells = rows[i].getElementsByTagName('input');
      for(var j=0; j<inputCells.length; j++){
        inputCells[j].className ='form-control';
        inputCells[j].required ='True';
      };
    var selectCells = rows[i].getElementsByTagName('select');
      for(var k=0; k<selectCells.length; k++){
        selectCells[k].className ='custom-select';
        selectCells[k].required ='True';
      };
  };
};

function setGlobalNames() {
    var recipeTable = document.getElementById('recipe_table');
    var bodyOfTable = recipeTable.getElementsByTagName('tbody')[0];
    var ogsteprow = document.getElementById('steprow');
    var ogphsteprow = document.getElementById('phstep');
    var ogsteristep = document.getElementById('steristep');
    phrow = ogphsteprow.cloneNode(true);
    steprow = ogsteprow.cloneNode(true);
    sterilizerow = ogsteristep.cloneNode(true);
    ogsteprow.setAttribute('id','ogsteprow');
    bodyOfTable.removeChild(ogphsteprow);
    bodyOfTable.removeChild(ogsteristep);
};

function addRow(rowtype) {
  var recipeTable = document.getElementById('recipe_table');
  var bodyOfTable = recipeTable.getElementsByTagName('tbody')[0];
  bodyOfTable.append(rowtype);
  if (rowtype.id=='steprow'){
    renameAndRecopyStepRow();
  } else if (rowtype.id == 'phstep') {
    document.getElementById('pHbutton').setAttribute('hidden',true);
  } else if (rowtype.id == 'steristep') {
    document.getElementById('sterilizeButton').setAttribute('hidden',true);
  }
};

function renameAndRecopyStepRow() {
  var ogsteprow = document.getElementById('steprow')
  steprow = ogsteprow.cloneNode(true);
  ogsteprow.setAttribute('id','ogsteprow')
}

function changeformsetattrs() {
  var numberOfRows = document.getElementsByTagName('tr');
  var numberOfStepRows = 0
  for(var i=0; i<numberOfRows.length; i++){
    if(numberOfRows[i].id == 'ogsteprow'){
      numberOfStepRows++
    }
  }
  console.log(numberOfStepRows);
}



// BUTTON script

$('.zip-button').on('click', function() {
	if ($('.contact-button-wrapper').hasClass('selected') == false) {
		$('.contact-button-wrapper').addClass('selected');
	}
});

$('.epk-button-half').on('click', function() {
	if ($('.contact-button-wrapper').hasClass('selected') == true) {
		$('.contact-button-wrapper').removeClass('selected');
	}
});
