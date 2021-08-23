<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Parking Lot System</title>
	<link href="<?= URL; ?>public/css/bootstrap.min.css" rel="stylesheet">
	<link href="<?= URL; ?>public/css/font-awesome.min.css" rel="stylesheet">
	<link href="<?= URL; ?>public/css/datepicker3.css" rel="stylesheet">
	<link href="<?= URL; ?>public/css/styles.css" rel="stylesheet">

	<!--[if lt IE 9]>
	<script src="js/html5shiv.js"></script>
	<script src="js/respond.min.js"></script>
	<![endif]-->
</head>
<body>
	<nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse"><span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span></button>
				<a class="navbar-brand" href=""><span>ParkingLot</span>Admin</a>
				<ul class="nav navbar-top-links navbar-right">
					<li class="dropdown"><a class="dropdown-toggle count-info" data-toggle="dropdown" href="#">
						<em class="fa fa-cogs"></em><span class="label label-info"></span>
					</a>
						<ul class="dropdown-menu dropdown-alerts">
							<li><a href="<?= URL; ?>logout">
								<div><em class="fa fa-arrow-left"></em> Log Out</div>
							</a></li>
							<li class="divider"></li>
						</ul>
					</li>
				</ul>
			</div>
		</div><!-- /.container-fluid -->
	</nav>
	<div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
		<div class="divider"></div>
		<ul class="nav menu">
			<li><a href="<?= URL; ?>panel"><em class="fa fa-dashboard">&nbsp;</em> Dashboard</a></li>
			<li><a href="<?= URL; ?>scanner" target="_blank"><em class="fa fa-qrcode">&nbsp;</em> Scanner</a></li>
			<li class="parent "><a data-toggle="collapse" href="#sub-item-1">
				<em class="fa fa-navicon">&nbsp;</em> Data Entry <span data-toggle="collapse" href="#sub-item-1" class="icon pull-right"><em class="fa fa-plus"></em></span>
				</a>
				<ul class="children collapse" id="sub-item-1">
					<li><a class="" href="<?= URL; ?>view?f=parkinglot">
						<span class="fa fa-arrow-right">&nbsp;</span> Parking Lot
					</a></li>
					<li><a class="" href="<?= URL; ?>view?f=users">
						<span class="fa fa-arrow-right">&nbsp;</span> Users
					</a></li>
				</ul>
			</li>
			<li><a class="" href="<?= URL; ?>report">
				<span class="fa fa-table">&nbsp;</span> Report &amp; Analysis
			</a></li>
		</ul>
	</div><!--/.sidebar-->

	<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">
		<?php pagecontent(); ?>
	</div>	<!--/.main-->

	<script src="<?= URL; ?>public/js/jquery-1.11.1.min.js"></script>
	<script src="<?= URL; ?>public/js/bootstrap.min.js"></script>
	<script src="<?= URL; ?>public/js/chart.min.js"></script>
	<script src="<?= URL; ?>public/js/chart-data.js"></script>
	<script src="<?= URL; ?>public/js/easypiechart.js"></script>
	<script src="<?= URL; ?>public/js/easypiechart-data.js"></script>
	<script src="<?= URL; ?>public/js/bootstrap-datepicker.js"></script>
	<script src="<?= URL; ?>public/js/custom.js"></script>
	<script>
		window.onload = function () {
            var chart2 = document.getElementById("bar-chart").getContext("2d");
			window.myBar = new Chart(chart2).Bar(barChartData, {
			responsive: true,
			scaleLineColor: "rgba(0,0,0,.2)",
			scaleGridLineColor: "rgba(0,0,0,.05)",
			scaleFontColor: "#c5c7cc"
			});
        };
	</script>

</body>
</html>
<?php pagecontent(); ?>
