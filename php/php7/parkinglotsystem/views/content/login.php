<div class="row">
  <?php if(@get('status') == 'success'): ?>
    <div class="alert alert-success"><h1>Hello, <?= get('idnumber'); ?>. Your parkinglot location at <?= get('location'); ?> lot <?= get('lot'); ?>.</h1></div>
  <?php elseif(@get('status') == 'noavailable'): ?>
      <div class="alert alert-danger"><h1>No parking lot available.</h1></div>
  <?php elseif(@get('status') == 'logout'): ?>
        <div class="alert alert-warning"><h1>You are now leaving, Thank you.</h1></div>
  <?php elseif(@get('status') == 'norecord'): ?>
        <div class="alert alert-danger"><h1>No record found for you ID Number.</h1></div>
  <?php endif; ?>
  <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">
    <div class="login-panel panel panel-default">
      <div class="panel-heading"></div>
      <div class="panel-body">
        <form action="<?= URL; ?>scanner/look" method="post" role="form">
          <fieldset>
            <div class="form-group">
              USE YOUR QR CODE / TYPE YOUR ID NUMBER
              <input class="form-control" placeholder="SCAN ID" name="idnumber" type="text" autofocus="">
            </div>
            <button type="submit" class="btn btn-primary form-control">SEARCH</button>
          </fieldset>
        </form>
      </div>
    </div>
  </div><!-- /.col-->
</div><!-- /.row -->
