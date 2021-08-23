<?php
use backend\core\Database;

class View {
  function __construct() {

  }

  function get() {
    set_data(
      array(
        'users' => (new Database())->select('users'),
        'parkinglot' => (new Database())->select('parkinglot')
      )
    );
    return panel_view('view');
  }

  function logs() {
    set_data((new Database())->select('logs', 'user=' . get('id')));
    return panel_view('logs');
  }

  function accept() {
    (new Database())->update('users', array(
      'level' => 'normal'
    ), 'id=' . get('id'));

    address('view?f=users&status=ok');
  }
}
