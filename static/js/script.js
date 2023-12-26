const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
			i.style.fontWeight = 'normal'; 
		})

		li.classList.add('active');
		item.style.fontWeight = 'bold'; 
	})
});