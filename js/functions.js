getData();

// $(document).ready(function() {
  // setTimeout(function(){ 
	

  // }, 1000);
// });

function getData() {

	jQuery.ajax({
		type: "GET",
		url: "./getData.php",
		dataType: "json",
		success: function (result) {
			aData = eval(result);
			turn();
			points();
			$('table#tbl1').remove();
			tableCreate();
			fillTable();
			console.log(aData);
			

			
			setTimeout(function(){ getData() }, 3000);
		},

	})

}




function tableCreate() {
    var dringo = document.getElementById("dringo");
    var tbl = document.createElement('table');
	tbl.setAttribute("id", 'tbl1');
    tbl.setAttribute('border', '2');
    var tbdy = document.createElement('tbody');
	//rijen
    for (var i = 0; i < aData[0][1]; i++) {
        var tr = document.createElement('tr');
		var trid = "r"+i;
			tr.setAttribute("id", trid);
			//kolommen
        for (var j = 0; j < aData[0][0]; j++) {
            var td = document.createElement('td');
			
            td.appendChild(document.createTextNode('\u0020'))
            tr.appendChild(td)
			var tdid = "c"+i+j;
			td.setAttribute("id", tdid);
            
        }
        tbdy.appendChild(tr);
    }
    tbl.appendChild(tbdy);
    dringo.insertBefore(tbl, dringo.childNodes[2])
	

}

function fillTable() {
	var l_aData = aData.length;
	kleur_rood =[];
	kleur_geel =[];
	
	var i,j,k;
	//net begonnen, eerste rij, eerste ltter weergeven
	if (l_aData ==1 && aData[0][2]!=''){
		document.getElementById('c00').textContent = aData[0][2][0];
		document.getElementById('c00').style.background = "red";
	}
	
	//loopen over aantal woorden
	for (i = 1; i < l_aData; ++i) {
		woordletters_count = [];
		aData[i][2] = Array.from(new Set(aData[i][2])).join("");

		var l_data_geel = aData[i][2].length;
		var l_aData_i = aData[i][0].length;
		//console.log(l_aData_i);
		//console.log(i);
		
		

		
		//loopen over aantal letters van woord
		for (j = 0; j < l_aData_i; ++j) {
          rood_cid=1;
			if (typeof woordletters_count[aData[i][0][j]] == 'undefined') {woordletters_count[aData[i][0][j]]=0;}	
			var cid = "c"+(i-1)+j;
			//console.log(cid);
			document.getElementById(cid).textContent = aData[i][0][j];	
			//is letter een niet-'_' dan rood
			if (aData[i][1][j] != '_'){
				kleur_rood.push(cid);
				rood_cid=0;
			}
			
			
			
			//loopen over aantal letters in bijna_goed 
			for (k=0; k<l_data_geel; ++k){
				a=(aData[i][0].match(new RegExp(aData[i][2][k], "g") || [])); //invoer (dyn)
				if (a== null){a=0;}
				else {a=a.length;}
				b=(aData[0][2].match(new RegExp(aData[i][2][k], "g") || [])); //antwoord (statisch)
				if (b== null){b=0;}
				else {b=b.length;}
				if (b== null){b=0;}
				c=(aData[i][1].match(new RegExp(aData[i][2][k], "g") || [])); //rood (dyn per invoer)
				if (c== null){c=0;}
				else {c=c.length;}

				geel_check=b;

				
				//wanneer letter van woord overeenkomt met letter van bijna_goed
				if (aData[i][0][j]==aData[i][2][k] && rood_cid!=0 && woordletters_count[aData[i][0][j]]<geel_check ) {
					kleur_geel.push(cid);
					woordletters_count[aData[i][0][j]]+=1;
					
				}
			}
console.log(woordletters_count);
		}
	
	}
	

colorTable();	
}	

function colorTable() {

var kleur_geel_unique = kleur_geel.filter(function(elem, index, self) {
    return index == self.indexOf(elem);
})

//console.log(kleur_geel_unique);	
//console.log(kleur_rood);
//rood
var i;
for (i = 0; i < kleur_rood.length; ++i) {

	document.getElementById(kleur_rood[i]).style.background = "red";	

	}	
	
	
for (i=0; i < kleur_geel_unique.length; ++i) {

	document.getElementById(kleur_geel_unique[i]).appendChild(document.createElement("div")).className="cirkel_geel";

}	

	


}

function turn() {
	if (aData[0][3]=='False') {
		
		document.getElementById("cteam1").style.background = "linear-gradient(to top, #fefc4a 0%,#f1da36 40%)";
		document.getElementById("cteam2").style.background = "linear-gradient(to bottom, #6582b2 0%,#093f60 100%)";
	}
	if (aData[0][3]=='True') {
		document.getElementById("cteam1").style.background = "linear-gradient(to bottom, #6582b2 0%,#093f60 100%)";
		document.getElementById("cteam2").style.background = "linear-gradient(to top, #fefc4a 0%,#f1da36 40%)";
	}	
		
}

function points() {
	document.getElementById("cteam1").getElementsByTagName("P").item(1).textContent = aData[0][4];
	document.getElementById("cteam2").getElementsByTagName("P").item(1).textContent = aData[0][5];
	
	
	
}



