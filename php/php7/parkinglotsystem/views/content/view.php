<?php
    $data = (@get('f') == 'users') ? data()['users'] : data()['parkinglot'];
?>
<div class="row">
    <ol class="breadcrumb">
        <li><a href="#">
            <em class="fa fa-home"></em>
        </a></li>
        <li class="active">View</li>
    </ol>
</div><!--/.row-->

<div class="row">
    <div class="col-lg-12">
        <h1 class="page-header">View</h1>
    </div>
</div><!--/.row-->

<div class="panel panel-container">
    <div class="panel-body">
        <?php if(@get('status') == 'ok'): ?>
        <div class="alert alert-success">Successfully approved.</div>
        <?php endif; ?>
        <a href="<?= URL; ?>create?f=<?= @get('f'); ?>" class="btn btn-primary"><i class="fa fa-plus"></i> New</a>
        <div class="table-responsive">
            <?php if(@get('f') == 'parkinglot'): ?>
            <table class="table">
                <thead>
                    <tr>
                        <th>Parking Lot Location</th>
                        <th>Label Name</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(sizeof($data) > 0): ?>
                        <?php foreach($data as $field): ?>
                        <tr>
                            <td><?= ucwords($field['location']); ?></td>
                            <td><?= ucwords($field['label']); ?></td>
                            <td><?= $field['status']; ?></td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
            <?php elseif(@get('f') == 'users'): ?>
            <table class="table">
                <thead>
                    <tr>
                        <th>ID Number</th>
                        <th>Fullname</th>
                        <th>Plate No.</th>
                        <th>Car Model</th>
                        <th>Type</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(sizeof($data) > 0): ?>
                        <?php foreach($data as $field): ?>
                        <tr>
                            <td><?= strtoupper($field['idnumber']); ?></td>
                            <td><?= ucwords($field['fullname']); ?></td>
                            <td><?= ucwords($field['plateno']); ?></td>
                            <td><?= ucwords($field['carmodel']); ?></td>
                            <td><?= ucwords($field['type']); ?></td>
                            <td>
                                <?php if($field['level'] != 'pending'): ?>
                                    <a href="<?= URL; ?>view/logs?id=<?= $field['id']; ?>" class="btn btn-primary">View Logs</a>
                                <?php else: ?>
                                    <a href="<?= URL; ?>view/accept?id=<?= $field['id']; ?>" class="btn btn-success">Accept User</a>
                                <?php endif; ?>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
            <?php endif; ?>
        </div>
    </div>
</div>
