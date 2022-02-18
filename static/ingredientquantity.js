
function onIngredientsSelectionChanged(select) {

  console.log(select.value);
  var options = select && select.options;
  var opt;
  document.getElementById("quantitycontainer").innerHTML = "";

  for (var i=0, iLen=options.length; i<iLen; i++) {
    opt = options[i];

    if (opt.selected) {
     // result.push(opt.value || opt.text);
      var textbox = document.createElement("input");
      textbox.type = "text";
      textbox.placeholder = opt.value;
     //  textboxes.push())
     document.getElementById("quantitycontainer").appendChild(textbox);
    }
   }
  
 
  
}
// let other=  document.getElementById("otheringredients").value.split(",");