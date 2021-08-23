<div class="row">
    <ol class="breadcrumb">
        <li><a href="#">
            <em class="fa fa-home"></em>
        </a></li>
        <li class="active">Dashboard</li>
    </ol>
</div><!--/.row-->

<div class="row">
    <div class="col-lg-12">
        <h1 class="page-header">Dashboard</h1>
    </div>
</div><!--/.row-->

<div class="panel panel-container">
    <div class="row">
        <a href="<?= URL; ?>view?f=parkinglot">
            <div class="col-xs-6 col-md-3 col-lg-3 no-padding">
                <div class="panel panel-teal panel-widget border-right">
                    <div class="row no-padding"><em class="fa fa-xl fa-exclamation-triangle color-blue"></em>
                        <div class="text-large">Parking Lot</div>
                    </div>
                </div>
            </div>
        </a>
        <a href="<?= URL; ?>view?f=users">
            <div class="col-xs-6 col-md-3 col-lg-3 no-padding">
                <div class="panel panel-blue panel-widget border-right">
                    <div class="row no-padding"><em class="fa fa-xl fa-users color-orange"></em>
                        <div class="text-large">Users</div>
                    </div>
                </div>
            </div>
        </a>
    </div><!--/.row-->
</div>
