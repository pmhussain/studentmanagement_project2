<script
src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js">
</script>
<script
src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js">
</script>
<script>
const xValues = ["Students", "Staff", "Courses", "Subjects",];
const yValues = [{{students}}, {{staff}}, {{courses}},{{subjects}},];
const barColors = ["red", "green","blue","orange",];

new Chart("myChart", {
type: "bar",
data: {
  labels: xValues,
  datasets: [{
    backgroundColor: barColors,
    data: yValues
  }]
},
options: {

scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
            min: 0
          }
          }]
},
legend: {display: false},
title: {
display: true,
text: "Statistics"
}
}
});
</script>
