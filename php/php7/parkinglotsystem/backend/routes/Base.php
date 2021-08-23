<?php
/**
 * @class: Base
 * 
 */

class Base {

    # Load your first process here.
    function __construct() {

    }

    # Get request.
    function get() {
        return base_view('hello');
    }

    # Post request.
    function post() {
    }

    function say() {
        print('hello');
    }
}