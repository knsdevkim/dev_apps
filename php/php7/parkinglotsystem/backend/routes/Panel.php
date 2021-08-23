<?php
use backend\core\Database;

class Panel {
  function __construct() {
    session();

    if(@!get_session('isLogin')) {
        address('login');
    }
  }

  function get() {
    return panel_view('dashboard');
  }
}
