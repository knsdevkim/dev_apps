<div class="row">
    <ol class="breadcrumb">
        <li><a href="#">
            <em class="fa fa-home"></em>
        </a></li>
        <li class="active">Logs</li>
    </ol>
</div><!--/.row-->

<div class="row">
    <div class="col-lg-12">
        <h1 class="page-header">Logs</h1>
    </div>
</div><!--/.row-->

<div class="panel panel-container">
    <div class="panel-body">
        <div class="table-responsive">
            <table class="table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Time</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(sizeof(data()) > 0): ?>
                        <?php foreach(data() as $field): ?>
                        <tr>
                            <td><?= $field['date']; ?></td>
                            <td><?= $field['time']; ?></td>
                            <td><?= ucwords($field['status']); ?></td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>
