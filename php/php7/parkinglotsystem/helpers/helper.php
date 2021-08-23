<?php
/**
 * This file consist all the function helpers available
 * to use in entire system framework.
 *
 */

/**
 *
 * @method: set_data()
 * - This function will set the data
 *
 */
function set_data($data) {
    global $set_data;
    $set_data = $data;
}

/**
 *
 * @method: data()
 * - This function will get the data set from the
 *   function / method set_data().
 *
 */
function data() {
    global $set_data;
    return $set_data;
}

/**
 *
 * @method: session()
 * - Start the session with name default _session.
 */
function session($name = '_session') {
    session_name($name);
    return session_start();
}

/**
 *
 * @method: session_kill();
 * - This will end the session process and delete all
 *   session stored
 *
 */
function session_kill() {
    unset($_SESSION);
    session_destroy();
}

/**
 *
 * @method: set_session()
 * - Set session key , value.
 *   Note: always to start the session before using this.
 *
 */
function set_session($key, $value) {
    return $_SESSION[$key] = $value;
}

/**
 *
 * @method: get_session()
 * - Get the session value by the key.
 *   Note: always to start the session before using this.
 *
 */
function get_session($key) {
    return $_SESSION[$key];
}

/**
 *
 * @method: post()
 * - This will handle post data from POST request.
 *
 */
function post($key = '') {
    return (!empty($key)) ? $_POST[$key] : $_POST;
}

/**
 *
 * @method: get()
 * - This will handle post data from GET request.
 *
 */
function get($key = '') {
    return (!empty($key)) ? $_GET[$key] : $_GET;
}

/**
 *
 * @method: address()
 * - An referer to address to the provided link.
 *
 */
function address($address, $url = URL) {
    return header('Location: ' . $url . $address);
}
