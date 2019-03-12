function swapStatus(){
    var statusline = document.getElementById('statusline');
    var startbutton = document.getElementById('startbutton');
    var hiddenRows = document.getElementsByClassName('selectreagent');
    var numhidrow = hiddenRows.length;
    console.log(hiddenRows)
    if (statusline.innerHTML == 'Status: Queued') {
      statusline.innerHTML = 'Status: In Progress';
      startbutton.innerHTML = 'Re-queue';
    } else if (statusline.innerHTML == 'Status: In Progress') {
      statusline.innerHTML = 'Status: Queued';
      startbutton.innerHTML = 'Start Recipe';
    }
    for(var i=0; i<numhidrow; i++){
      if(statusline.innerHTML == 'Status: Queued'){
        hiddenRows[i].setAttribute('hidden','true');
      } else if(statusline.innerHTML == 'Status: In Progress'){
        hiddenRows[i].removeAttribute('hidden');
      }
    }
}
