function save_word(){
	let value = document.querySelector('.curds-text').value.trim();
	if(value != '') {
		localStorage.setItem('word', (value) );
		document.location.href = "shop/shop.html";
	}
}

function search_curds(){
		let value = localStorage.getItem('word');
		let counter = 0;
		if(value) {
			let names = document.querySelectorAll('.name-link');
			names.forEach(function(name){
				if (counter < 1){
					document.querySelector('.all-products h2').innerHTML = 'Найденные товары';
					document.querySelector('.all-products').insertAdjacentHTML('beforeend', '<button class="show-products" type="button" onclick="showAll();">Показать все товары</button>');
				}
				counter++;
				if(name.innerText.toLowerCase().search(value.toLowerCase()) == -1){
					name.innerHTML = name.innerText;
					name.parentNode.parentNode.parentNode.style.display = 'none';
				}
				else{

					const top_value = document.querySelector('.all-products').getBoundingClientRect().top;
					console.log(top_value);

					window.scrollTo({
					    top: top_value,
					    behavior: "smooth"
					});
					let str = name.innerText;
					name.innerHTML = highlights(str,name.innerText.toLowerCase().search(value.toLowerCase()), value.length);	
					
					setTimeout(function(){
						name.innerHTML = str;	
					}, 5000);
				}
			});
		}
}

function highlights(str, pos, len){
	return str.slice(0, pos) + '<mark>' + str.slice(pos, pos + len) + '</mark>' + str.slice(pos + len);
}

function showAll(){
	document.querySelector('.all-products h2').innerHTML = 'Все наши товары';
	document.querySelector('.show-products').remove();
	let elems = document.querySelectorAll('.product-box');
	for(let i = 0; i < elems.length; i++){
		elems[i].style.display = 'block';
	}
	localStorage.clear();
}