/* Inspired by : https://codepen.io/obc/pen/ypDmg */
/* Te iubesc pisoi */
/* @_tomesch */

// Add values to the values array and see what happens :)
var values = [250,10000,340,290];

drawChart(values,".chart",30) // You can adjust the margin between each bar by changing 10 to whatever you like

function drawChart(data,selector,padding){
  var max = Math.max.apply(Math, data);
	var chart = document.querySelector(selector);
	var barwidth = ((chart.offsetWidth-(values.length-1)*padding-(data.length)*10)/data.length);
	var sum = data.reduce(function(pv, cv) { return pv + cv; }, 0);
	var left = 0;
	for (var i in data){
	  var newbar = document.createElement('div');
	  newbar.setAttribute("class", "bar");
	  newbar.style.width=barwidth+"px";
	  newbar.style.height=((data[i]/max)*100)+"%";
	  newbar.style.left=left+"px";
	  chart.appendChild(newbar);
	  left += (barwidth+padding+10);
	}
}