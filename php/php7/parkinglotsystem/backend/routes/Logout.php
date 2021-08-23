<?php
class Logout {
    function __construct() {
        session();
    }

    function get() {
        session_kill();
        address('login');
    }
}