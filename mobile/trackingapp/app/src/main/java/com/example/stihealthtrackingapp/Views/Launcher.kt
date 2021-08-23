package com.example.stihealthtrackingapp.Views

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.util.Log
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.example.stihealthtrackingapp.R
import com.example.stihealthtrackingapp.Urls.Https
import org.json.JSONObject

class Launcher: AppCompatActivity(), View.OnClickListener {

    private lateinit var mLayoutsplashscreen: LinearLayout
    private lateinit var mLayoutlogin: LinearLayout
    private lateinit var mProgress: ProgressBar
    private lateinit var mTvmessage: TextView
    private lateinit var mEtusername: EditText
    private lateinit var mEtpassword: EditText
    private lateinit var mBtnlogin: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.launcher)

        this.isAuthenticated()

        this.firstLoad()
        this.setupWidgets()
    }
    
    companion object {
        private const val TAG = "Launcher"
        private const val mInterval: Long = 7000
    }

    @SuppressLint("SetTextI18n")
    override fun onClick(view: View) {
        when ( view ) {
            mBtnlogin -> {
                val username = mEtusername.text.toString()
                val password = mEtpassword.text.toString()

                if (username == "" || password == "") {
                    mTvmessage.text = "Provide both membership account and password."
                    mTvmessage.visibility = View.VISIBLE
                } else {
                    mTvmessage.visibility = View.INVISIBLE
                    mProgress.visibility = View.VISIBLE
                    mBtnlogin.isEnabled = false

                    object: Thread() {
                        override fun run() {
                            super.run()

                            try {
                                val queue = Volley.newRequestQueue(applicationContext)

                                val request = object: StringRequest(
                                        Method.POST,
                                        Https().HTTPS_LOGIN,
                                        { response ->
                                            mProgress.visibility = View.INVISIBLE

                                            when (response) {
                                                "pending" -> {
                                                    mTvmessage.text = "Your account still pending or blocked by admin. Please wait to activate."
                                                    mTvmessage.visibility = View.VISIBLE
                                                }
                                                "invalid_login" -> {
                                                    mTvmessage.text = "Invalid credentials."
                                                    mTvmessage.visibility = View.VISIBLE
                                                }
                                                else -> {
                                                    try {
                                                        mTvmessage.visibility = View.INVISIBLE

                                                        val jsonObject = JSONObject(response)
                                                        val jsonArray = jsonObject.getJSONArray("data")

                                                        var login: Boolean = false
                                                        var id: String = ""
                                                        var fullname: String = ""
                                                        var address: String = ""

                                                        for (i in 0 until jsonArray.length()) {
                                                            val dataObject = jsonArray.getJSONObject(i)

                                                            login = true
                                                            id = dataObject.getString("id")
                                                            fullname = dataObject.getString("fullname")
                                                            address = dataObject.getString("address")
                                                        }

                                                        val sharedPref = getSharedPreferences("app", MODE_PRIVATE)

                                                        with ( sharedPref.edit() ) {
                                                            putBoolean("login", login)
                                                            putString("id", id)
                                                            putString("fullname", fullname)
                                                            putString("address", address)
                                                            apply()
                                                        }

                                                        startActivity(Intent(applicationContext, Main::class.java).also { intent ->
                                                            intent.flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
                                                            finish()
                                                        })

                                                    } catch (e: Exception) {
                                                        mTvmessage.text = "Something went wrong. Try again."
                                                        mTvmessage.visibility = View.VISIBLE
                                                    }
                                                }
                                            }
                                        }, { error ->
                                    error.message?.let { message ->
                                        Log.e(TAG, message)
                                        mTvmessage.text = "Error in server, Try again."
                                        mTvmessage.visibility = View.VISIBLE
                                    }

                                }) {
                                    override fun getParams(): MutableMap<String, String> {
                                        val objects_parameter: MutableMap<String, String> = HashMap<String, String>()

                                        objects_parameter["username"] = username
                                        objects_parameter["password"] = password

                                        return objects_parameter
                                    }
                                }

                                queue.add(request)
                            } catch(e: Exception) {

                            } finally {
                                this@Launcher.runOnUiThread {
                                    mProgress.visibility = View.INVISIBLE
                                    mBtnlogin.isEnabled = true
                                }
                            }

                            sleep(10000)
                        }
                    }.start()
                }
            }
        }
    }

    private fun isAuthenticated() {
        val sharedPref = getSharedPreferences("app", MODE_PRIVATE)

        if (sharedPref.getBoolean("login", false)) {
            startActivity(Intent(this, Main::class.java).also { intent ->
                intent.flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
                finish()
            })
        }
    }

    private fun setupWidgets() {
        mLayoutsplashscreen = findViewById(R.id.layoutsplashscreen)
        mLayoutlogin = findViewById(R.id.layoutlogin)
        mProgress = findViewById(R.id.progress)
        mTvmessage = findViewById(R.id.tvmessage)
        mEtusername = findViewById(R.id.etusername)
        mEtpassword = findViewById(R.id.etpassword)
        mBtnlogin = findViewById(R.id.btnlogin)

        this.initializeWidgets()
    }

    private fun initializeWidgets() {
        mBtnlogin.setOnClickListener(this)

        mTvmessage.visibility = View.INVISIBLE
        mProgress.visibility = View.INVISIBLE
        mLayoutlogin.visibility = View.GONE
    }

    private fun firstLoad() {
        Looper.myLooper().let { looper ->
            Handler(looper!!).postDelayed({
                mLayoutsplashscreen.visibility = View.GONE
                mLayoutlogin.visibility = View.VISIBLE
            }, mInterval)
        }
    }
}