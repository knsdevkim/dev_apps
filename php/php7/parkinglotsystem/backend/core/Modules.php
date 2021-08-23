<?php
namespace backend\core {
    /*
    * @class: Modules
    * @extends: InitializerEngines
    * - This will be the class for all the work of the system file.
    *   It is a very important class which all the process from the front and back-end
    *   will be work at here.
    *
    *
    * */

    class Modules extends InitializerEngines {
        private $fetchURL = null; # -> This will store the return value of initialized URL from the method of extended class.

        # Initialize the priority process.
        function __construct() {
            # Load the first process.
            # Which will check the URL
            # If there is parameter loaded or not.
            $this->fetchURL = $this->initializeURL();
        }

        # This method handle all the request from the URL.
        function run() {
            # Get the fetched url and store on this variable.
            $__URL = $this->fetchURL;
            
            # Check the length of the url array 0 means there is no url parameter passes.
            if(sizeof($__URL) > 0) {
                # Store the url [0] value in class variable.
                $class = ucfirst($__URL[0]);
                # Access the file to the folder ; base on the class name url.
                $file_class = 'backend/routes/' . $class . '.php';
                # Check if the file exists
                if(file_exists($file_class)) {
                    # Include the class file.
                    include_once($file_class);
                } else {
                    # If the class file does not exists load 
                    # the 404 Bad Request.
                    systemInterface('error/badrequest');
                }

                # Check the size of parameter send by the URL.
                if(sizeof($__URL) == 1) {
                    # Always use this as is this is the get request
                    # default view.
                    (new $class())->get();
                } else if(sizeof($__URL) == 2) {
                    # Parameter 2 in the URL request serve as 
                    # retrieving method from the class.
                    (new $class())->{$__URL[1]}();
                } else {
                    systemInterface('error/badrequest');
                }
            } else {
                # If the array return to zero.
                # You may load here the default view for 
                # Front-end user.
                $class = ucfirst(DEFAULT_CONTROLLER);
                # Access the file to the folder ; base on the class name url.
                $file_class = 'backend/routes/' . $class . '.php';
                # Check if the file exists
                if(file_exists($file_class)) {
                    # Include the class file.
                    include_once($file_class);
                } else {
                    # If the class file does not exists load 
                    # the 404 Bad Request.
                    systemInterface('error/badrequest');
                }

                (new $class())->get();
            }
        }
    }
}