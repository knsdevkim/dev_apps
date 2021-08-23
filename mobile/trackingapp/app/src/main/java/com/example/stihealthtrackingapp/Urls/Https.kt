package com.example.stihealthtrackingapp.Urls

class Https {
    val IP: String = "http://192.168.86.25/stihealthmonitoring"

    val HTTPS_LOGIN: String = "${IP}/android/login"
    val HTTPS_GETUSERALERT: String = "${IP}/android/getalerts"
    val HTTPS_GETPROFILEINFO: String = "${IP}/android/getprofileinfo"
    val HTTPS_POSTALERT: String = "${IP}/android/postalert"
}