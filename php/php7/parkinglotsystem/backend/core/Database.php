<?php
namespace backend\core {
	/**
	 *
	 * Use PHP Data Object as extension for DATABASE and queries.
	 *
	 */

	use \PDO;

	/**
	 *
	 * @class: Database
	 * @extend: PDO
	 * - This class will handle the process of pulling and pushing data in database.
	 *
	 */

    class Database extends PDO {

		# This construct method will use the parent construct to establish connection
		# to database.
    	function __construct() {
			# Check if the const DATABASE_NAME provided
			# Then establish the connection if provided.
    		if(!empty(DATABASE_NAME)) {
    			parent::__construct('mysql:host=' . DATABASE_HOST . ';dbname=' . DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD);
				# Set error handler in PDO.
				parent::setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    		}
    	}

		/**
		 *
		 * @method: Select Query.
		 *
		 */
    	function select($table, $condition = '', $cols = '*') {
			# Check if the condition provided.
			$condition = ($condition == '') ? '' : ' WHERE ' . $condition;
			# Query string.
			$query = 'SELECT ' . $cols . ' FROM ' . $table . $condition . ';';
			# Prepare and execute query.
			$sth = $this->prepare($query);
			$sth->execute();
			# Set the fetch mode.
    	$sth->setFetchMode(PDO::FETCH_ASSOC);

			# Return the result of the query.
    	return $sth->fetchAll();
		}

		/**
		 *
		 * @method: Insert Query
		 *
		 *
		 */
		function insert($table, $data) {
			# Join the array keys to this variable
			$keys = implode(array_keys($data), ', ');
			# Join the array values to this variable
			$values = '"' . implode(array_values($data), '", "') . '"';
			# Query string.
			$query = 'INSERT INTO ' . $table . '(' . $keys . ') VALUES(' . $values . ');';
			# Execute the query and return.
			return $this->exec($query);
		}

		/**
		 *
		 * @method: Update Query
		 *
		 *
		 */
		function update($table, $data, $condition) {
			# Sort the array to ascending order base on the key of array.
			ksort($data);
			# This will handle the update string keys and datas.
			$update = "";
			# Get each key , data and join together.
			foreach($data as $key => $value) {
				# concatenate the result.
				$update .= $key . '="' . $value . '", ';
			}

			# Remove the right ',' from the result of loop.
			$update = rtrim($update, ', ');

			#Query string
			$query = 'UPDATE ' . $table . ' SET ' . $update . ' WHERE ' . $condition . ';';
			# Execute the query and return.
			return $this->exec($query);
		}

		/**
		 *
		 * @method: Delete Query
		 *
		 *
		 */
		function delete($table, $condition) {
			# Query string.
			$query = 'DELETE FROM ' . $table . ' WHERE ' . $condition . ';';
			return $this->exec($query);
		}

		/**
		 *
		 * @method: Truncate Query
		 *
		 *
		 */
		function truncate($table) {
			# Query string
			$query = 'TRUNCATE TABLE ' . $table . ';';
			# Execute and return.
			return $this->exec($query);
		}

		/**
		 *
		 * @method: Independent Query
		 *
		 *
		 */
		function query($query) {
			# Prepare and execute the query
			$sth = $this->prepare($query);
			$sth->execute();
			# set the fetch mode to associative array.
			$sth->setFetchMode(PDO::FETCH_ASSOC);
			return $sth->fetchAll();
		}
    }
}
