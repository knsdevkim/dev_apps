<?php
  ini_set('display_errors', true);
  error_reporting( E_ALL );

  foreach(glob('config/*.php') as $configuration) {
    include_once($configuration);
  }

  foreach(glob('helpers/cores/*.php') as $helpers) {
    include_once($helpers);
  }

  foreach(glob('helpers/*.php') as $helpers) {
    include_once($helpers);
  }

  spl_autoload_register(function($class) {
    $class = str_replace('\\', '/', $class) . '.php';
    if( file_exists($class) ) include_once($class);
  });

  use \apps\cores\Route;
  use \apps\cores\Base;

  (new Route());
?>
