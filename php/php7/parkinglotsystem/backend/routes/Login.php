<?php
use backend\core\Database;

class Login {
    function __construct() {
        session();

        if(@get_session('isLogin')) {
            address('panel');
        }
    }

    function get() {
        return authenticate_view('syslogin');
    }

    function post() {
        $userEmail = post('username');
        $userPassword = post('password');

        $fetchData = (new Database())->select(
            'users',
            'idnumber="' . $userEmail . '"'
        );

        if(@sizeof($fetchData) > 0) {
            foreach($fetchData as $field) {
                $dbUserId = $field['id'];
                $dbUserLevel = $field['level'];
                $dbPassword = $field['password'];
                $dbUserFullname = $field['fullname'];
            }

            if(password_verify($userPassword, $dbPassword)) {
                set_session('isLogin', true);
                set_session('userid', $dbUserId);
                set_session('level', $dbUserLevel);
                set_session('userfullname', $dbUserFullname);

                address('panel');
            } else {
                address('login?status=invalid');
            }
        } else {
            address('login?status=invalid');
        }
    }
}