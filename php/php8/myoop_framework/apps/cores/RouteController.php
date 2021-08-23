<?php
namespace apps\cores {

  class RouteController {
    private $path = null;

    public function __construct() {
      if(!empty($_SERVER['PATH_INFO'])) {
        $path = filter_var(@$_SERVER['PATH_INFO'], FILTER_SANITIZE_URL) ?: null;
        if($path != null) {
          $path = ltrim(rtrim($path, '/'), '/');
          $path = explode('/', $path);
          $this->path = $path;
        }
      }
      $this->urlParameter();
    }

    private function urlParameter() {
      try {
        if(!is_null($this->path)) { $class = ucfirst($this->path[0]); } else { $class = ucfirst(DEFAULT_CLASS_VIEW); }
        $class_file = 'apps/views/' . $class . '.php';
        if(file_exists($class_file)) {
          include_once($class_file);
          if(class_exists(ucfirst($class))) {
            $class_method = new (ucfirst($class))();
            $this->subRoute($class_method);
          } else { die('No class found in path.'); }
        } else {
          die('No file found in path.');
        }
      } catch(Exception $e) { die($e->getMessage()); }
    }

    private function subRoute($class) {
      if(!is_null($this->path)) {
        if(count($this->path) > 1) {
          $method = $this->path[1];
          if(count($this->path) > 2) {
            $class->$method(array_slice($this->path, 2, count($this->path)));
          } else { $class->$method(); }
        } else {
          if(method_exists($class, 'get')) {
            $class->get();
          } else { die('No method found get() by default from your views.'); }
        }
      } else {
        if(method_exists($class, 'get')) {
          $class->get();
        } else { die('No method found get() by default from your views.'); }
      }
    }
  }
}

