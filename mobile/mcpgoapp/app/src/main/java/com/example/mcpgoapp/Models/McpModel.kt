package com.example.mcpgoapp.Models

import io.realm.RealmObject
import io.realm.annotations.PrimaryKey

open class McpModel(
    @PrimaryKey var id: Int = 0,
    var cust_code: String = "",
    var customer: String = "",
    var scode: String = "",
    var salesperson: String = "",
    var ave_nps: String = "",
    var class_label: String = "",
    var address: String = "",
    var area: String = "",
    var odd_even: String = "",
    var branch: String = "",
    var channel: String = "",
    var freq: String = "",
    var day: String = "",
    var cterm: String = "",
    var climit: String = "",
    var sman_type: String = "",
    var gtm: String = "",
    var group: String = "",
    var town: String = "",
    var zip_code: String = "",
    var channel_group: String = "",
    var channel_group2: String = "",
    var chain: String = "",
    var area_class: String = "",
    var old_new: String = "",
    var geolocation: String = ""
): RealmObject()