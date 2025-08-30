const ctx = document.getElementById('invoiceChart').getContext('2d');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025"],
        datasets: [{
            label: "Tax Invoice Totals",
            data: [1300,1275,1250,1225,1200,1175,1150,1125,1100,1100,900],
            backgroundColor: [
                "#007bff","#6610f2","#6f42c1","#e83e8c","#dc3545",
                "#fd7e14","#ffc107","#28a745","#20c997","#17a2b8","#6c757d"
            ]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'bottom' }
        }
    }
});