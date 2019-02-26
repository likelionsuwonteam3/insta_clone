(function update_screen_size() {
  document.getElementById("ban-monitor").style.width = window.innerWidth + "px";
  document.getElementById("ban-monitor").style.height =
    window.innerHeight + "px";
  if (window.innerWidth < 576) {
    document.getElementById("ban-monitor").style.display = "none";
  }
})();
