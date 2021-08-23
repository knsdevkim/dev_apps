package com.example.mcpgoapp.Views

import android.annotation.SuppressLint
import android.content.Context
import android.content.DialogInterface
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Color
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.util.Base64
import android.util.Log
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.widget.*
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import com.android.volley.*
import com.android.volley.toolbox.*
import com.example.mcpgoapp.Authenticate.Authenticate
import com.example.mcpgoapp.Https.Urls
import com.example.mcpgoapp.Permission.Permission
import com.example.mcpgoapp.R
import com.example.mcpgoapp.Utils.ModelController
import kotlinx.android.synthetic.main.registration_dialog.*
import org.json.JSONArray
import org.json.JSONObject
import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.HashMap

class LoginView: AppCompatActivity(), View.OnClickListener {

    private lateinit var mSplashscreen: LinearLayout
    private lateinit var mLogin: LinearLayout

    private lateinit var mEtemployeeid: EditText
    private lateinit var mEtpassword: EditText

    private lateinit var mMessage: TextView
    private lateinit var mRegister: TextView

    private lateinit var mButtonlogin: Button

    private lateinit var mProgresslogin: ProgressBar

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        this.initializeLocalServer()
        this.run()
    }

    companion object {
        private const val TAG                    = "LoginView"
        private const val mInterval: Long        = 5000
    }

    private fun run() {
        Permission(this).initializePermissions()
        Authenticate(this).authenticated()
        this.loadWidgets()
        this.loadScreen()

    }

    private fun initializeLocalServer() {
        ModelController().modelInitialize(this)
    }

    private fun loadWidgets() {
        mSplashscreen  = findViewById(R.id.linearLayoutSplashscreen)
        mLogin         = findViewById(R.id.linearLayoutLogin)

        mEtemployeeid  = findViewById(R.id.etEmployeeID)
        mEtpassword    = findViewById(R.id.etPassword)

        mMessage       = findViewById(R.id.tvMessage)
        mRegister      = findViewById(R.id.register)

        mButtonlogin   = findViewById(R.id.btnLogin)

        mProgresslogin = findViewById(R.id.progressLogin)

        mProgresslogin.visibility = View.INVISIBLE
        mLogin.visibility         = View.GONE
        mMessage.visibility       = View.GONE

        this.initializeClickListener()
    }

    private fun initializeClickListener() {
        mButtonlogin.setOnClickListener(this)
        mRegister.setOnClickListener(this)
    }

    private fun loadScreen() {
        Looper.myLooper()?.let {
            looper ->
            Handler(looper).postDelayed({
                mSplashscreen.visibility = View.GONE
                mLogin.visibility        = View.VISIBLE


            }, mInterval)
        }
    }

    @SuppressLint("SetTextI18n", "InflateParams")
    override fun onClick(v: View?) {
        when ( v ) {
            mButtonlogin -> {
                this.processlogin()
            }
            mRegister -> {
                val alertDialogBuilder: AlertDialog.Builder = AlertDialog.Builder(this)
                val view = LayoutInflater.from(this).inflate(R.layout.registration_dialog, null, false)
                this.registration(view)

                alertDialogBuilder.setView(view)
                alertDialogBuilder.setCancelable(false)
                alertDialogBuilder.setNegativeButton("CLOSE") { _ : DialogInterface, _ ->

                }

                val dialog = alertDialogBuilder.create()
                dialog.show()
            }
        }
    }

    private fun registration(v: View) {
        val errorFirstname       = v.findViewById<TextView>(R.id.errorFirstname)
        val errorLastname        = v.findViewById<TextView>(R.id.errorLastname)
        val errorEmail           = v.findViewById<TextView>(R.id.errorEmail)
        val errorMcp             = v.findViewById<TextView>(R.id.errorMcp)
        val errorUsername        = v.findViewById<TextView>(R.id.errorUsername)
        val errorPassword        = v.findViewById<TextView>(R.id.errorPassword)
        val errorConfirmPassword = v.findViewById<TextView>(R.id.errorConfirmPassword)

        val etFirstname       = v.findViewById<EditText>(R.id.firstname)
        val etLastname        = v.findViewById<EditText>(R.id.lastname)
        val etEmail           = v.findViewById<EditText>(R.id.email)
        val spnAccountType    = v.findViewById<Spinner>(R.id.account_type)
        val spnMcp            = v.findViewById<Spinner>(R.id.mcp_data)
        val etUsername        = v.findViewById<EditText>(R.id.username)
        val etPassword        = v.findViewById<EditText>(R.id.password)
        val etConfirmPassword = v.findViewById<EditText>(R.id.confirmpassword)

        val queue = Volley.newRequestQueue(this)

        val gtmListOption   = ArrayList<String>()
        val salesListOption = ArrayList<String>()

        var arrayMcpAdapter: ArrayAdapter<String>

        errorMcp.setTextColor(resources.getColor(R.color.colorI))
        errorMcp.text = "MCP options syncing for registration, Please wait . . . "

        val request = object : StringRequest(
                Method.GET,
                Urls().URL_API_DATA,
                { response ->
                    try {
                        val jsonArray = JSONArray(response)

                        for (i in 0 until jsonArray.length()) {
                            val dataObject = jsonArray.getJSONObject(i)
                            if (!gtmListOption.contains(dataObject.getString("gtm"))) {
                                gtmListOption.add(dataObject.getString("gtm"))
                            }
                            if (!salesListOption.contains(dataObject.getString("salesperson"))) {
                                salesListOption.add(dataObject.getString("salesperson"))
                            }
                        }

                        arrayMcpAdapter = ArrayAdapter<String>(this,
                                android.R.layout.simple_spinner_item, gtmListOption)

                        arrayMcpAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

                        spnMcp.adapter = arrayMcpAdapter

                        errorMcp.text = ""
                    } catch(e: Exception) {
                        errorMcp.setTextColor(resources.getColor(R.color.colorG))
                        errorMcp.text = "Could not get mcp data, Please check your network."
                        e.message?.let { error ->
                            Log.e(TAG, error)
                        }
                    }
                }, { error ->
                    errorMcp.setTextColor(resources.getColor(R.color.colorG))
                    errorMcp.text = "Could not get mcp data, Please check your network."
                    error.message?.let { message ->
                        Log.e(TAG, message)
                    }
                }
        ) {
            override fun getHeaders(): MutableMap<String, String> {
                val mutableHeaders: MutableMap<String, String> = HashMap<String, String>()

                val credentials_authentication = "${Urls().API_USERNAME}:${Urls().API_PASSWORD}"

                mutableHeaders["Content-Type"]  = "application/json"
                mutableHeaders["Authorization"] = "Basic " + Base64.encodeToString(credentials_authentication.toByteArray(), Base64.NO_WRAP)

                return mutableHeaders
            }

            override fun getBodyContentType(): String {
                return "application/json"
            }
        }

        request.retryPolicy = DefaultRetryPolicy(
                5000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT
        )

        queue.add(request)

        spnAccountType.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
                val getAccountType = spnAccountType.getItemAtPosition(position).toString()
                if (getAccountType == "SALESPERSON") {

                    arrayMcpAdapter = ArrayAdapter<String>(this@LoginView,
                    android.R.layout.simple_spinner_item, salesListOption)

                    arrayMcpAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

                    spnMcp.adapter = arrayMcpAdapter

                } else {
                    arrayMcpAdapter = ArrayAdapter<String>(this@LoginView,
                            android.R.layout.simple_spinner_item, gtmListOption)

                    arrayMcpAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

                    spnMcp.adapter = arrayMcpAdapter
                }
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {

            }
        }

        val btncreate         = v.findViewById<Button>(R.id.btncreate)

        btncreate.setOnClickListener {
            if (etFirstname.text.isEmpty()) {
                errorFirstname.text = "* Provide your firstname."
            } else if (etLastname.text.isEmpty()) {
                errorLastname.text = "* Provide your lastname."
            } else if (etEmail.text.isEmpty()) {
                errorEmail.text = "*Provide your email."
            } else if(spnMcp.selectedItem.toString() == "") {
                errorMcp.setTextColor(resources.getColor(R.color.colorG))
                errorMcp.text = "Could not find your mcp select atleast one."
            } else if (etUsername.text.isEmpty()) {
                errorUsername.text = "*Provide your username"
            } else if (etPassword.text.isEmpty()) {
                errorPassword.text = "*Provide your password"
            } else if (etPassword.text.toString() != etConfirmPassword.text.toString()) {
                errorConfirmPassword.text = "*Password mismatch."
            } else {
                errorFirstname.text       = ""
                errorLastname.text        = ""
                errorEmail.text           = ""
                errorMcp.text             = ""
                errorUsername.text        = ""
                errorPassword.text        = ""
                errorConfirmPassword.text = ""

                val dialogCreate = AlertDialog.Builder(this)

                dialogCreate.setView(LayoutInflater.from(this).inflate(R.layout.progress_register, null, false))
                dialogCreate.setCancelable(false)

                val dialog = dialogCreate.create()
                dialog.show()

                var user_type: Int = 2

                if (spnAccountType.selectedItem.toString() == "GTM")
                    user_type = 2

                if (spnAccountType.selectedItem.toString() == "SALESPERSON")
                    user_type = 3

                try {
                    val jsonObject = JSONObject()

                    jsonObject.put("first_name", etFirstname.text.toString())
                    jsonObject.put("last_name", etLastname.text.toString())
                    jsonObject.put("email", etEmail.text.toString())
                    jsonObject.put("user_type", user_type.toString())
                    jsonObject.put("link_mcp", spnMcp.selectedItem.toString())
                    jsonObject.put("username", etUsername.text.toString())
                    jsonObject.put("password", etPassword.text.toString())

                    Log.i(TAG, jsonObject.toString())

                    val request = object : JsonObjectRequest (
                            Method.POST,
                            Urls().URL_API_REGISTER,
                            jsonObject,
                            { _ ->
                                dialog.dismiss()
                                val alertSuccessDialog = AlertDialog.Builder(this)
                                alertSuccessDialog.setMessage("Account has been created! Wait for admin approval.")
                                alertSuccessDialog.setCancelable(false)
                                alertSuccessDialog.setPositiveButton("Ok") {_: DialogInterface, _ ->

                                }

                                val dialog = alertSuccessDialog.create()
                                dialog.show()
                            }, { error ->
                                dialog.dismiss()
                                try {
                                    val response_error = String(error.networkResponse.data, Charsets.UTF_8)

                                    Log.e(TAG, response_error)

                                    val jsonObjectError = JSONObject(response_error)

                                    if (jsonObjectError.has("email")) {
                                        val jsonArrayError = JSONArray(jsonObjectError.getString("email"))
                                        errorEmail.text = jsonArrayError.get(0).toString()
                                    }

                                    if (jsonObjectError.has("username")) {
                                        val jsonArrayError = JSONArray(jsonObjectError.getString("username"))
                                        errorUsername.text = jsonArrayError.get(0).toString()
                                    }

                                    if (jsonObject.has("link_mcp")) {
                                        val jsonArrayError = JSONArray(jsonObjectError.getString("link_mcp"))
                                        errorMcp.text = jsonArrayError.get(0).toString()
                                    }
                                } catch(e: Exception) {
                                    Log.e(TAG, "JSON_ERROR_RESPONSE EXCEPTION: $e")
                                }
                            }
                    ) {
                        override fun getHeaders(): MutableMap<String, String> {
                            return HashMap()
                        }

                        override fun getBodyContentType(): String {
                            return "application/json"
                        }
                    }

                    request.retryPolicy = DefaultRetryPolicy(
                            5000,
                            DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                            DefaultRetryPolicy.DEFAULT_BACKOFF_MULT
                    )

                    Volley.newRequestQueue(this).add(request)
                } catch(e: Exception) {
                    e.message?.let { error ->
                        Log.e(TAG, error)
                    }
                }
            }
        }
    }

    @SuppressLint("SetTextI18n")
    private fun processlogin() {
        val username: String = mEtemployeeid.text.toString()
        val password: String = mEtpassword.text.toString()

        if ( username == "" || password == "" ) {
            mMessage.text       = "Fill both employee id and password."
            mMessage.visibility = View.VISIBLE
        } else {
            mMessage.visibility       = View.INVISIBLE
            mProgresslogin.visibility = View.VISIBLE

            mButtonlogin.isEnabled = false

            Thread() {
                val mUrl  = Urls().URL_API_LOGIN

                val request = object : StringRequest(
                        Method.POST,
                        mUrl,
                        {
                            response ->

                            mProgresslogin.visibility = View.INVISIBLE
                            mMessage.text             = ""

                            mButtonlogin.isEnabled = true

                            try {
                                val jsonObject = JSONObject(response)

                                if (jsonObject.getString("account_status") != "pending") {
                                    startActivity(Intent(this, FragmentsHandler::class.java).also {

                                        val sharedPref = getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)
                                        with ( sharedPref.edit() ) {
                                            putBoolean("login", true)
                                            putString("token", jsonObject.getString("token"))
                                            putString("user_type", jsonObject.getString("user_type"))
                                            putString("fullname", jsonObject.getString("fullname"))
                                            putString("userfullname", jsonObject.getString("userfullname"))
                                            apply()
                                        }

                                        finish()
                                    })
                                } else {
                                    val alertLoginInvalidDialog = AlertDialog.Builder(this)
                                    alertLoginInvalidDialog.setMessage("Your account is still pending to login, wait for admin approval.")
                                    alertLoginInvalidDialog.setCancelable(false)
                                    alertLoginInvalidDialog.setPositiveButton("Ok") {_: DialogInterface, _ ->

                                    }

                                    val dialog = alertLoginInvalidDialog.create()
                                    dialog.show()
                                }
                            } catch(e: Exception) {
                                mMessage.visibility = View.VISIBLE
                                mMessage.text       = "SERVER IS NOT AVAILABLE"

                                mButtonlogin.isEnabled = true
                            }
                        },{
                    error ->
                    error?.message.let {
                        message ->

                        Log.e(TAG, message.toString())

                        mProgresslogin.visibility = View.INVISIBLE
                        mMessage.visibility       = View.VISIBLE
                        mMessage.text             = "Invalid username or password"

                        mButtonlogin.isEnabled = true
                    }
                }) {
                    override fun getParams(): MutableMap<String, String> {
                        val parameters: MutableMap<String, String> = HashMap<String, String>()

                        parameters["username"] = username
                        parameters["password"] = password

                        return parameters
                    }
                }

                request.retryPolicy = DefaultRetryPolicy(
                        5000,
                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT)

                Volley.newRequestQueue(this).add(request)

                Thread.sleep(10000)
            }.start()
        }
    }
}