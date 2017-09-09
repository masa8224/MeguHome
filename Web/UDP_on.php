<?php
    	$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
    	$msg = $_POST["data"];
    	$len = strlen($msg);
    	socket_sendto($sock, $msg, $len, 0, '192.168.88.246', 8888);
    	socket_close($sock);
?>