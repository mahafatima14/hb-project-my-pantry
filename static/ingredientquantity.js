// console.log('js is working')
// create a feature which takes in 

function populatequantitycontainer(ingredients){
  document.getElementById("quantitycontainer").innerHTML = "";

  for (var i=0, iLen=ingredients.length; i<iLen; i++) {
   

    
     // result.push(opt.value || opt.text);
      const textbox = document.createElement("input");
      textbox.name = "quantity_"+ ingredients[i]
      textbox.type = "text";
      textbox.placeholder = ingredients[i];
     //  textboxes.push())
     document.getElementById("quantitycontainer").appendChild(textbox);
    
  }

}


function onIngredientsSelectionChanged(select) {
  
  const ingredients = []
  console.log(select.value);
  var options = select && select.options;
  var opt;
  

  for (var i=0, iLen=options.length; i<iLen; i++) {
    opt = options[i];

    if (opt.selected) {
      ingredients.push(opt.value)
      
  
     
    }
   }
populatequantitycontainer(ingredients)
 
  
}
function onIngredientsSelectionChangedtext(input) {

  console.log(input.value);


  const ingredientinput =  input.value.split(",");

populatequantitycontainer(ingredientinput)

}