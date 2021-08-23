<?php

function render($file) {
  return include_once(dirname(__DIR__, 2) . '/' . TEMPLATE_FOLDER . '/' . $file . '.php');
}

function frame($root, $page) {
  global $pagecontent;
  $pagecontent = $page;
  return render($root);
}

function pagecontent() {
  global $pagecontent;
  return include_once(dirname(__DIR__, 2) . '/' . TEMPLATE_FOLDER . '/' . $pagecontent . '.php');
}

function static_folder($file) {
  return URL . STATIC_FOLDER . '/' . $file;
}

function redirect($address) {
  return header('Location: ' . URL . $address);
}

function secure_password($password) {
  return password_hash($password, MIDDLEWARE['MIDDLEWARE.PASSWORD.HASHING'], array('cost' => MIDDLEWARE['MIDDLEWARE.PASSWORD.COST']));
}

function url($url = '') {
  return URL . $url;
}
