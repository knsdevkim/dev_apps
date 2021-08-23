<?php
use backend\core\Database;

class Android {
    function register() {
        $data = array(
            'idnumber' => post('idnumber'),
            'fullname' => post('fullname'),
            'address' => post('address'),
            'plateno' => post('plateno'),
            'carmodel' => post('carmodel'),
            'contactnumber' => post('contactnumber'),
            'type' => post('type'),
            'level' => 'pending'
          );
  
          $isUserExists = (count((new Database())->select('users', 'idnumber="' . post('idnumber') . '" OR plateno="' . post('plateno') . '"')) > 0) ? true : false;
  
          if($isUserExists <= 0) {
            (new Database())->insert('users', $data);
            print('ok');
          } else {
            print('exists');
          }
    }

    function login() {
        $idnumber = post('idnumber');

        $check = (new Database())->select('users', 'idnumber="' . $idnumber . '" AND level="normal"');

        if(count($check) > 0) {
            print($idnumber);
        } else {
            print('error');
        }
    }

    function logs() {
        $id = (new Database())->select('users', 'idnumber="' . get('idnumber') . '"');
        
        $json = '';
        $json .= '{"data":';
        $json .= json_encode((new Database())->select('logs', 'user=' . $id[0]['id']));
        $json .= '}';

        print($json);
    }

    function getparkinglot() {
        $data = (new Database())->select('parkinglot');

        $json = '';

        $json .= '{"data":';
        $json .= json_encode($data);
        $json .= '}';

        print($json);
    }
}