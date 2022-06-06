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

function contactUs(){
	let name = document.querySelector('.contact-input .name').value;
	let email = document.querySelector('.contact-input .email').value;
	let phone = document.querySelector('.contact-input .phone').value;
	let message = document.querySelector('.contact-input .message').value;
	if(name != '' && email != '' && phone != '' && message != '')
		alert(name + ', спасибо за Ваше сообщение. Мы обязательно рассмотрим его, и позвоним Вам по номеру: '+ phone + 'в течение дня или пришлем вам ответ, на адрес: ' + email+'.');
	else alert('Необходимо заполнить каждое поле.')
}