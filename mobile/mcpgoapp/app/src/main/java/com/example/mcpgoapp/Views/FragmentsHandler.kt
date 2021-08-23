package com.example.mcpgoapp.Views

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.Gravity
import android.view.MenuItem
import android.view.View
import android.view.WindowManager
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.ActionBar
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.GravityCompat
import androidx.drawerlayout.widget.DrawerLayout
import androidx.fragment.app.FragmentActivity
import com.example.mcpgoapp.Authenticate.Authenticate
import com.example.mcpgoapp.Fragments.Dashboard
import com.example.mcpgoapp.Fragments.Search
import com.example.mcpgoapp.R
import com.google.android.material.navigation.NavigationView

class FragmentsHandler: AppCompatActivity(), View.OnClickListener {

    private lateinit var home: ImageView
    private lateinit var search: ImageView
    private lateinit var back: ImageView
    private lateinit var headermenu: ImageView

    private lateinit var tvwelcome: TextView

    private lateinit var drawer: DrawerLayout

    private lateinit var navigation_view: NavigationView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.fragmentshandler)
        window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)

        this.run()
    }

    override fun onClick(v: View?) {
        when(v) {
            home -> {
                val fragment = Dashboard()

                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()

                fragmentTransaction.replace(R.id.flFragment, fragment)
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }
            back -> {
                val fm = supportFragmentManager
                fm.popBackStack()
            }

            this.search -> {
                val fragment = Search()

                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()

                fragmentTransaction.replace(R.id.flFragment, fragment)
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }

            this.headermenu -> {
                this.drawer.openDrawer(GravityCompat.START)
            }
        }
    }

    companion object {
        private const val TAG = "FragmentsHandler"
    }

    private fun run() {
        Authenticate(this).not_authenticated()
        this.loadWidgets()
        this.initializeClickListener()
        this.initializeNavigationItemClick()
    }

    private fun loadWidgets() {
        home       = findViewById(R.id.home)
        back     = findViewById(R.id.back)
        search     = findViewById(R.id.search)
        headermenu = findViewById(R.id.header_menu)

        this.tvwelcome   = findViewById(R.id.welcome)

        this.drawer      = findViewById(R.id.drawer)

        this.navigation_view = findViewById(R.id.navigation_view)

        val menuUserDetails = navigation_view.getHeaderView(0).findViewById<TextView>(R.id.menuUserFullname)

        val sharedPref = getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)
        val guess = if (sharedPref.getString("userfullname", "") != "null") sharedPref.getString("userfullname", "") else "ADMIN"
        this.tvwelcome.text = "HELLO! $guess"
        menuUserDetails.text = guess
    }

    private fun initializeNavigationItemClick() {
        this.navigation_view.setNavigationItemSelectedListener { it: MenuItem ->
            when ( it.itemId ) {
                R.id.menusettings -> {
                    Log.i(TAG, "settings clicked")
                    true
                }
                R.id.menuchangepassword -> {
                    Log.i(TAG, "change password clicked")
                    true
                }
                R.id.menulogout -> {
                    val sharedPref = getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)

                    with(sharedPref.edit()) {
                        clear()
                        apply()
                    }

                    startActivity(Intent(this, LoginView::class.java).also {
                        finish()
                    })
                    true
                }
                else -> {
                    true
                }
            }
        }
    }

    override fun onBackPressed() {
        if(this.drawer.isDrawerOpen(GravityCompat.START)) {
            this.drawer.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }

    private fun initializeClickListener() {
        home.setOnClickListener(this)
        search.setOnClickListener(this)
        back.setOnClickListener(this)
        headermenu.setOnClickListener(this)
    }
}