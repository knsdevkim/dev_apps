<div class="row">
  <?php if(@get('status') == 'invalid'): ?>
    <div class="alert alert-danger">Invalid username or password.</div>
  <?php endif; ?>
  <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">
    <div class="login-panel panel panel-default">
      <div class="panel-heading"></div>
      <div class="panel-body">
        <form action="<?= URL; ?>login/post" method="post" role="form">
          <fieldset>
            <div class="form-group">
              <input class="form-control" placeholder="Username" name="username" type="text" autofocus="">
            </div>
            <div class="form-group">
              <input class="form-control" placeholder="Password" name="password" type="password">
            </div>
            <button type="submit" class="btn btn-primary form-control">SEARCH</button>
          </fieldset>
        </form>
      </div>
    </div>
  </div><!-- /.col-->
</div><!-- /.row -->
