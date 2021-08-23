<?php
use backend\core\Database;

class Report {
	function __construct() {

	}

	function get() {
		return panel_view('report');
	}
}