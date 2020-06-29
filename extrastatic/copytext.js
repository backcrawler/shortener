function copyFunction() {
  let copyText = document.getElementById("myRef");
  console.log("Copytext: ",copyText.href ) // debug

   /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.href);

  alert("Copied to clipboard: " + copyText.href+ ' !');
}