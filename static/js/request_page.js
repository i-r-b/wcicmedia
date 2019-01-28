function swapStatus(){
    var statusline = document.getElementById('statusline');
    var startbutton = document.getElementById('startbutton')
    if (statusline.innerHTML == 'Status: Queued') {
      statusline.innerHTML = 'Status: In Progress';
      startbutton.innerHTML = 'Re-queue';
    } else if (statusline.innerHTML == 'Status: In Progress') {
      statusline.innerHTML = 'Status: Queued';
      startbutton.innerHTML = 'Start Recipe';
    }
}
