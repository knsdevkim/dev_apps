package com.example.stihealthtrackingapp.Views

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import com.example.stihealthtrackingapp.Fragments.HomeFragment
import com.example.stihealthtrackingapp.Fragments.ProfileFragment
import com.example.stihealthtrackingapp.R

class Main: AppCompatActivity(), View.OnClickListener {

    private lateinit var mHome: ImageView
    private lateinit var mProfile: ImageView
    private lateinit var mLogout: ImageView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main)

        this.isNotAuthenticated()

        this.setupWidgets()
    }
    
    companion object {
        private const val TAG = "Main"
    }

    override fun onClick(view: View) {
        when ( view ) {
            mHome -> {
                Log.i(TAG, "home button clicked")
                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()
                fragmentTransaction.replace(R.id.fragmentview, HomeFragment())
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }
            mProfile -> {
                Log.i(TAG, "profile button clicked")
                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()
                fragmentTransaction.replace(R.id.fragmentview, ProfileFragment())
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }
            mLogout -> {
                this.logout()
            }
        }
    }

    private fun setupWidgets() {
        mHome = findViewById(R.id.home)
        mProfile = findViewById(R.id.profile)
        mLogout = findViewById(R.id.exit)

        this.initializeWidgets()
    }

    private fun initializeWidgets() {
        mHome.setOnClickListener(this)
        mProfile.setOnClickListener(this)
        mLogout.setOnClickListener(this)
    }

    private fun isNotAuthenticated() {
        val sharedPref = getSharedPreferences("app", MODE_PRIVATE)

        if (!sharedPref.getBoolean("login", false)) {
            startActivity(Intent(this, Launcher::class.java).also { intent ->
                intent.flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
                finish()
            })
        }
    }

    private fun logout() {
        val sharedPref = getSharedPreferences("app", MODE_PRIVATE)

        with ( sharedPref.edit() ) {
            clear()
            apply()
        }

        startActivity(Intent(this, Launcher::class.java).also { intent ->
            intent.flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
            finish()
        })
    }
}