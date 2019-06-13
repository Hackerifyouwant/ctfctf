<?php

class MyFirstCTF {
    protected $test = "ls";
    function __wakeup()
    {
        print "Wake up yo!<br>";
        system("echo ".$this->test);
    }
}

$obj= new MyfirstCTF();

echo serialize($obj);




