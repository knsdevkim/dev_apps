<?php
# This helper will be use in the front-end user function
# To connect the base frame to content frame layout.

# This function will be use in Base frame in layout.
function frame($root, $content) {
	global $pagecontent;
	$pagecontent = $content;
	include_once(dirname(__DIR__) . '/views/base/' . $root . '.php');
}

# This function will be use in Content frame inside the Base layout.
function pagecontent() {
	global $pagecontent;
	include_once(dirname(__DIR__) . '/views/content/' . $pagecontent . '.php');
}

# This function will be use in system interface error.
function systemInterface($file) {
	include_once(dirname(__DIR__) . '/views/' . $file . '.php');
}
