<?php
use backend\core\Database;

class Scanner {
    function __construct() {
        
    }

    function get() {
        panel_login('login');
    }

    function look() {
        $idnumber = post('idnumber');
        $focus_idnumber = $idnumber;

        $is_idnumber_exists = (new Database())->select('users', 'idnumber="' . $idnumber . '"');

        if(sizeof($is_idnumber_exists) > 0) {
            $lookup = (new Database())->select('parkinglot', 'reserve="' . $idnumber . '"');

            $idnumber = (new Database())->select('users', 'idnumber="' . $idnumber . '"');
            $idnumber = $idnumber[0]['id'];

            if(sizeof($lookup) <= 0) {
                $is_available = (new Database())->select('parkinglot', 'status="AVAILABLE"');

                if(sizeof($is_available) > 0) {
                    $lot_id = $is_available[0]['id'];
                    $data = array(
                        'status' => 'OCCUPY',
                        'reserve' => $focus_idnumber
                    );

                    (new Database())->insert('logs', array(
                        'time' => date('h:m a'),
                        'date' => date('M d, Y'),
                        'user' => $idnumber,
                        'status' => 'PARKED'
                    ));

                    (new Database())->update('parkinglot', $data, 'id=' . $lot_id);
                    address('scanner?status=success&idnumber=' . $focus_idnumber . '&location=' . $is_available[0]['location'] . '&lot=' . $is_available[0]['label']);
                } else {
                    address('scanner?status=noavailable');
                }
            } else {
                $lot_id = $lookup[0]['id'];
                $data = array(
                    'status' => 'AVAILABLE',
                    'reserve' => ''
                );

                (new Database())->insert('logs', array(
                    'time' => date('h:m a'),
                    'date' => date('M d, Y'),
                    'user' => $idnumber,
                    'status' => 'PARK OUT'
                ));

                (new Database())->update('parkinglot', $data, 'id=' . $lot_id);
                address('scanner?status=logout');
            }
        } else {
            address('scanner?status=norecord');
        }
    }
}