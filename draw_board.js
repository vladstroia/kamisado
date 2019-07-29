let table = document.body.firstElementChild;
// coloring the table
table.rows[1].cells[0].style.backgroundColor = 'red';	
table.rows[2].cells[3].style.backgroundColor = 'red';	
table.rows[3].cells[6].style.backgroundColor = 'red';	
table.rows[0].cells[5].style.backgroundColor = 'red';	

table.rows[0].cells[2].style.backgroundColor = 'purple';	
table.rows[1].cells[7].style.backgroundColor = 'purple';	
table.rows[2].cells[4].style.backgroundColor = 'purple';	
table.rows[3].cells[1].style.backgroundColor = 'purple';	

table.rows[0].cells[6].style.backgroundColor = 'green';	
table.rows[1].cells[3].style.backgroundColor = 'green';	
table.rows[2].cells[0].style.backgroundColor = 'green';	
table.rows[3].cells[5].style.backgroundColor = 'green';	

for (let i = 0; i < 4; i++) {
	table.rows[i].cells[i].style.backgroundColor = 'orange';
	table.rows[i].cells[7-i].style.backgroundColor = '#663300'; //brown	
	table.rows[i].cells[i+4].style.backgroundColor = 'yellow';	
	table.rows[i].cells[3-i].style.backgroundColor = 'pink';
}
// first half finished
// mirroring the second half
for (let i = 4; i < 8; i++) {
	for (let j = 0 ; j < 8; j++) {
		table.rows[i].cells[j].style.backgroundColor =
			table.rows[7-i].cells[7-j].style.backgroundColor;
}
}





