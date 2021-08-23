<?php
namespace backend\core {
    /*
    * @class InitializerEngines
    * @method: initializeApp
    * - This class will boot the first load of all important process of the system.
    * */

    class InitializerEngines {
        # Method that will generate and parse the url.
        function initializeURL() {
            # Get the paramater passes in the url.
            # Return to null if there is no parameter passes.
            $pathURL = filter_var(@$_SERVER['PATH_INFO'], FILTER_SANITIZE_URL) ?: null;
            # Check if patchURL variable passes a parameter
            # From the URL.
            if($pathURL) {
                # Remove the left and right '/'.
                $cleanPatchURL = ltrim(rtrim($pathURL, '/'), '/');
                # Parse the patched URL in to array and return.
                return explode('/', $cleanPatchURL);
            } else {
                # Return an empty array if there is no array passes.
                return array();
            }
        }
    }
}