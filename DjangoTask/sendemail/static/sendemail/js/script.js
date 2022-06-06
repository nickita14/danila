const iconMenu = document.querySelector('.menu-icon')

if (iconMenu) {
	const menuBody = document.querySelector('.menu-body-small')
	iconMenu.addEventListener("click", function(e){
		iconMenu.classList.toggle('active');
		menuBody.classList.toggle('active');
	});
}

function follow(){
	let value = document.querySelector('.footer-input').value;
	if (value != ''){
		document.querySelector('.coll button').innerText = 'Вы подписались';
		document.querySelector('.footer-input').style.border = '0px';
	}
	else{
		document.querySelector('.footer-input').style.border = '1px solid red';
		document.querySelector('.footer-input').style.background = '#FF8F8F'; 
	}
}

