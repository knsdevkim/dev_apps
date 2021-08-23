package com.example.mcpgoapp.Https

class Urls {
    // private val URL_CONFIG = "http://10.59.26.38:8000/api"
    // PUBLIC IP
    private val URL_CONFIG = "http://58.69.1.106:8069/api"
    // SERVER private val URL_CONFIG = "http://192.168.128.163:8069/api"
    // LOCAL IP private val URL_CONFIG = "http://192.168.86.25:8000/api"

    val API_USERNAME = "admin"
    val API_PASSWORD = "password@123"

    val URL_API_LOGIN    = "${URL_CONFIG}/login/"
    val URL_API_SYNC     = "${URL_CONFIG}/getall/"
    val URL_API_DATA     = "${URL_CONFIG}/mcpdata/"
    val URL_API_REGISTER = "${URL_CONFIG}/createuser/"
}