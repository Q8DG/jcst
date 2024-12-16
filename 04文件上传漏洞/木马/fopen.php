<?php
    $file = fopen("temp.php", "w");
    fwrite($file, "<?php phpinfo();?>");
?>