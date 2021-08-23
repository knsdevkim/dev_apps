<?php
use backend\core\Database;

class Create {
  function __construct() {

  }

  function get() {
    return panel_view('create');
  }

  function post() {
    switch(@get('f')) {
      case 'parkinglot':
        $data = array(
          'location' => post('location'),
          'label' => post('labelname')
        );

        $isLocationExists = (count((new Database())->select('parkinglot', 'location="' . post('location') . '" AND label="' . post('labelname') . '"')) > 0) ? true : false;

        if(!$isLocationExists) {
          (new Database())->insert('parkinglot', $data);
          address('create?f=parkinglot&e=success');
        } else {
          address('create?f=parkinglot&e=exists');
        }
      break;
      case 'users':
        $data = array(
          'idnumber' => post('idnumber'),
          'fullname' => post('fullname'),
          'address' => post('address'),
          'plateno' => post('plateno'),
          'carmodel' => post('carmodel'),
          'contactnumber' => post('contactnumber'),
          'type' => post('type')
        );

        $isUserExists = (count((new Database())->select('users', 'idnumber="' . post('idnumber') . '" OR plateno="' . post('plateno') . '"')) > 0) ? true : false;

        if($isUserExists <= 0) {
          (new Database())->insert('users', $data);
          address('create?f=users&e=success');
        } else {
          address('create?f=users&e=exists');
        }
      break;
      default:
        exit();
      break;
    }
  }
}
