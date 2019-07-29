let table = document.body.firstElementChild;
for (let i = 0; i < 4; i++) {
		table.rows[i].cells[i].style.backgroundColor = 'orange';
		table.rows[i].cells[7-i].style.backgroundColor = '#663300'; //brown	
		table.rows[i].cells[i+4].style.backgroundColor = 'yellow';	
		table.rows[1].cells[0].style.backgroundColor = 'red';	
		table.rows[2].cells[3].style.backgroundColor = 'red';	
		table.rows[3].cells[6].style.backgroundColor = 'red';	
}
