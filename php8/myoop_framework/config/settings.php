<?php

const URL = 'http://localhost/phpframework/';

const DB_CONFIG = [
    'ENGINE' => 'mysql',
    'HOST' => 'localhost',
    'NAME' => '',
    'USER' => 'root',
    'PASSWORD' => '',
    'PORT' => 3306
];

const MIDDLEWARE = [
  'MIDDLEWARE.PASSWORD.HASHING' => PASSWORD_BCRYPT,
  'MIDDLEWARE.PASSWORD.COST' => 12,
  'MIDDLEWARE.SESSION.NAME' => '_alias.active.session'
];

const TEMPLATE_FOLDER = 'templates';

const STATIC_FOLDER = 'static';
