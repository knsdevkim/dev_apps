<?php
# Create your BASE frame layout here with content.

function base_view($content) {
    frame('base', $content);
}

function panel_view($content) {
  frame('panel', $content);
}

function panel_login($content) {
  frame('login', $content);
}

function authenticate_view($content) {
  return frame('syslogin', $content);
}
