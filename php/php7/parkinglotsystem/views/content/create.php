<div class="row">
    <ol class="breadcrumb">
        <li><a href="#">
            <em class="fa fa-home"></em>
        </a></li>
        <li class="active">Create</li>
    </ol>
</div><!--/.row-->

<div class="row">
    <div class="col-lg-12">
        <h1 class="page-header">Create</h1>
    </div>
</div><!--/.row-->

<div class="panel panel-container">
    <div class="panel-body">
        <?php if(@get('e') == 'success'): ?>
        <div class="alert alert-success">Successfully added.</div>
        <?php elseif(@get('e') == 'exists'): ?>
        <div class="alert alert-danger">Data is already exists.</div>
        <?php endif; ?>
        <form action="<?= URL; ?>create/post?f=<?= get('f'); ?>" method="post">
            <?php if(@get('f') == 'parkinglot'): ?>
            <div class="form-group">
                <label for="location">Parking Location</label>
                <input type="text" name="location" id="location" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="labelname">Label Lot.</label>
                <input type="text" name="labelname" id="labelname" class="form-control" required>
            </div>
            <?php elseif(@get('f') == 'users'): ?>
            <div class="form-group">
                <label for="idnumber">ID Number</label>
                <input type="text" name="idnumber" id="idnumber" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="fullname">Fullname</label>
                <input type="text" name="fullname" id="fullname" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="address">Address</label>
                <input type="text" name="address" id="address" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="address">Plate No.</label>
                <input type="text" name="plateno" id="plateno" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="address">Car Model</label>
                <input type="text" name="carmodel" id="carmodel" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="address">Contact No.</label>
                <input type="text" name="contactnumber" id="contactnumber" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="type">User Type</label>
                <select name="type" id="type" class="form-control" required>
                    <option value="">-------</option>
                    <option value="employee">Employee</option>
                    <option value="student">Student</option>
                </select>
            </div>
            <?php endif; ?>
            <button type="submit" class="btn btn-md btn-primary form-control">Save</button>
        </form>
    </div>
</div>
