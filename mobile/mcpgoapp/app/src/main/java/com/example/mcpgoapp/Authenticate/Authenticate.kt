package com.example.mcpgoapp.Authenticate

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import com.example.mcpgoapp.Views.FragmentsHandler
import com.example.mcpgoapp.Views.LoginView

class Authenticate(context: Context) {

    var context: Context?              = null
    var sharedPref: SharedPreferences? = null

    init {
        this.context    = context
        this.sharedPref = context.getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)
    }

    fun authenticated() {
        if (this.sharedPref!!.getBoolean("login", false)) {
            this.context!!.startActivity(Intent(this.context, FragmentsHandler::class.java))
        }
    }

    fun not_authenticated() {
        if (!this.sharedPref!!.getBoolean("login", true)) {
            this.context!!.startActivity(Intent(this.context, LoginView::class.java))
        }
    }
}