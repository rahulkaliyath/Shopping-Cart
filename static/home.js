console.log("Hey  helooo");

var minus=document.getElementById('prod-1-minus');
var plus=document.getElementById('prod-1-plus');
var qty=document.getElementById('prod-1-quantity');


var minus=document.querySelectorAll(".button-minus");
var qty_field=document.querySelectorAll(".quantity-field");
var plus=document.querySelectorAll(".button-plus");
var button_cart=document.querySelectorAll(".button-cart");
var plus_cart=document.querySelectorAll(".plus-btn");
var minus_cart=document.querySelectorAll(".minus-btn");


plus.forEach(function(e){
	e.addEventListener('click',function(){
		id= e.id.slice(13, e.id.length);
		var qty_field=document.getElementById('qty-prod-id-'+id);
		qty_field.value=parseInt(qty_field.value,10)+1;
})
});


plus_cart.forEach(function(e){
	e.addEventListener('click',function(){
		id= e.id.slice(13, e.id.length);
		var qty_field=document.getElementById('cart-qty-id-'+id);
		qty_field.value=parseInt(qty_field.value,10)+1;
})
});

minus.forEach(function(e){
	e.addEventListener('click',function(){
		id= e.id.slice(9, e.id.length);
		var qty_field=document.getElementById('qty-prod-id-'+id);
		qty_field.value=parseInt(qty_field.value,10)-1;
})
});

minus_cart.forEach(function(e){
	e.addEventListener('click',function(){
		id= e.id.slice(14, e.id.length);
		var qty_field=document.getElementById('cart-qty-id-'+id);
		qty_field.value=parseInt(qty_field.value,10)-1;
})
});


function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.querySelector(".row").classList.remove('blur');
   document.querySelector(".navbar").classList.remove('blur');
}

function openNav() {
 document.getElementById("mySidebar").style.width = "520px";
 document.querySelector(".row").classList.add('blur');
 document.querySelector(".navbar").classList.add('blur');
}




