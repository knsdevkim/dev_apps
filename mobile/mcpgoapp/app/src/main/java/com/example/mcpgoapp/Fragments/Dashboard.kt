package com.example.mcpgoapp.Fragments

import android.annotation.SuppressLint
import android.content.Context
import android.content.DialogInterface
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AlertDialog
import androidx.cardview.widget.CardView
import androidx.drawerlayout.widget.DrawerLayout
import androidx.fragment.app.Fragment
import com.android.volley.DefaultRetryPolicy
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.example.mcpgoapp.Https.Urls
import com.example.mcpgoapp.Models.McpModel
import com.example.mcpgoapp.R
import com.example.mcpgoapp.Utils.ModelController
import io.realm.Realm
import org.json.JSONArray
import java.util.*
import kotlin.collections.HashMap

class Dashboard: Fragment(), View.OnClickListener {

    private lateinit var realm: Realm

    private lateinit var tvDate: TextView
    private lateinit var tvMedian: TextView
    private lateinit var sync: CardView
    private lateinit var masterdata: CardView
    private lateinit var salesperson: CardView
    private lateinit var customers: CardView

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val root: View = inflater.inflate(R.layout.dashboard, null, false)
        this.run(root)
        return root
    }

    override fun onDestroy() {
        super.onDestroy()
        realm.close()
    }
    
    companion object {
        private const val TAG = "Dashboard"
    }

    private fun run(v: View) {
        realm = ModelController().modelInstance()
        this.loadWidgets(v)
        this.setDateDisplay()
        this.restrictButton()
    }

    private fun restrictButton() {
        val sharedPref = activity!!.getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)

        this.masterdata.visibility  = View.GONE
        this.salesperson.visibility = View.GONE
        this.customers.visibility   = View.GONE

        if (sharedPref.getString("user_type", "") == "1" || sharedPref.getString("user_type", "") == "4") {
            this.masterdata.visibility = View.VISIBLE
        }

        if (sharedPref.getString("user_type", "") == "2") {
            this.salesperson.visibility = View.VISIBLE
        }

        if (sharedPref.getString("user_type", "") == "3") {
            this.customers.visibility = View.VISIBLE
        }
    }

    private fun loadWidgets(v: View) {
        this.tvDate      = v.findViewById(R.id.tvDate)
        this.tvMedian    = v.findViewById(R.id.tvMedian)
        this.sync        = v.findViewById(R.id.sync)
        this.masterdata  = v.findViewById(R.id.masterdata)
        this.salesperson = v.findViewById(R.id.salesperson)
        this.customers   = v.findViewById(R.id.customers)

        this.initializeClickListener()
    }

    private fun initializeClickListener() {
        this.sync.setOnClickListener(this)
        this.masterdata.setOnClickListener(this)
        this.salesperson.setOnClickListener(this)
        this.customers.setOnClickListener(this)
    }

    @SuppressLint("SetTextI18n")
    private fun setDateDisplay() {
        val calendar = Calendar.getInstance()

        val array_months = listOf("January", "February", "March",
                "April", "May", "June", "July",
                "August", "September", "October",
                "November", "December")

        val array_weekdays = listOf("Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday")

        val string_date = "${array_months[calendar.get(Calendar.MONTH)]} ${calendar.get(Calendar.DAY_OF_MONTH)}, ${calendar.get(Calendar.YEAR)} - ${array_weekdays[calendar.get(Calendar.DAY_OF_WEEK) - 1]}"

        this.tvDate.text = string_date

        if (calendar.get(Calendar.HOUR_OF_DAY) >= 12) {
            this.tvMedian.text = "GOOD PM"
        } else {
            this.tvMedian.text = "GOOD AM"
        }
    }

    override fun onClick(v: View?) {
        val sharedPref = activity!!.getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)

        val fragmentManager     = activity!!.supportFragmentManager
        val fragmentTransaction = fragmentManager.beginTransaction()

        when(v) {
            this.sync -> {
                val alertDialog: AlertDialog.Builder = AlertDialog.Builder(activity!!)

                val alertMessage = "You are about to sync a large data from the server of No. 1 Supplier, Inc. and " +
                        "it requires a stable internet connection and time to process, Do you still want to continue?"

                alertDialog.setMessage(alertMessage)
                alertDialog.setCancelable(false)
                alertDialog.setPositiveButton("Yes") { _: DialogInterface, _: Int ->
                    this.sync()
                }
                alertDialog.setNegativeButton("Cancel") { _: DialogInterface, _: Int ->

                }

                val dialog: AlertDialog = alertDialog.create()

                dialog.show()
            }
            this.masterdata -> {
                val fragment = Gtm()

                fragmentTransaction.replace(R.id.flFragment, fragment)
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }
            this.salesperson -> {
                val fragment = Sales()
                val bundle = Bundle()

                bundle.putString("gtm", sharedPref.getString("fullname", "").toString().toUpperCase(Locale.ROOT))

                fragment.arguments = bundle

                fragmentTransaction.replace(R.id.flFragment, fragment)
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }
            this.customers -> {
                val fragment = Customer()
                val bundle = Bundle()

                bundle.putString("salesperson", sharedPref.getString("fullname", "").toString().toUpperCase(Locale.ROOT))

                fragment.arguments = bundle

                fragmentTransaction.replace(R.id.flFragment, fragment)
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }
        }
    }

    @SuppressLint("InflateParams")
    private fun sync() {
        val alertDialog: AlertDialog.Builder = AlertDialog.Builder(activity!!)

        val alertView: View = LayoutInflater.from(activity!!).inflate(R.layout.progress_syncing, null, false)

        alertDialog.setView(alertView)
        alertDialog.setCancelable(false)

        val dialog: AlertDialog = alertDialog.create()

        dialog.show()

        Thread() {
            val queue = Volley.newRequestQueue(activity!!)

            val request = object: StringRequest(
                Method.GET,
                Urls().URL_API_SYNC,
                {
                        response ->

                    try {
                        val jsonArray = JSONArray(response)

                        try {
                            val mcpmasterlist = realm.where(McpModel::class.java).findAll()

                            realm.executeTransaction {
                                mcpmasterlist.deleteAllFromRealm()
                            }

                            for (i in 0 until jsonArray.length()) {
                                val data = jsonArray.getJSONObject(i)

                                realm.executeTransaction {
                                    realm ->
                                    val mcp = realm.createObject(McpModel::class.java, i)

                                    mcp.cust_code      = data.getString("cust_code")
                                    mcp.customer       = data.getString("customer")
                                    mcp.scode          = data.getString("scode")
                                    mcp.salesperson    = data.getString("salesperson")
                                    mcp.ave_nps        = data.getString("ave_nps")
                                    mcp.class_label    = data.getString("class_label")
                                    mcp.address        = data.getString("address")
                                    mcp.area           = data.getString("area")
                                    mcp.odd_even       = data.getString("odd_even")
                                    mcp.branch         = data.getString("branch")
                                    mcp.channel        = data.getString("channel")
                                    mcp.freq           = data.getString("freq")
                                    mcp.day            = data.getString("day")
                                    mcp.cterm          = data.getString("cterm")
                                    mcp.climit         = data.getString("climit")
                                    mcp.sman_type      = data.getString("sman_type")
                                    mcp.gtm            = data.getString("gtm")
                                    mcp.group          = data.getString("group")
                                    mcp.town           = data.getString("town")
                                    mcp.zip_code       = data.getString("zip_code")
                                    mcp.channel_group  = data.getString("channel_group")
                                    mcp.channel_group2 = data.getString("channel_group2")
                                    mcp.chain          = data.getString("chain")
                                    mcp.area_class     = data.getString("area_class")
                                    mcp.old_new        = data.getString("old_new")
                                    mcp.geolocation    = data.getString("geolocation")
                                }
                            }

                            dialog.dismiss()

                            val successAlertDialog: AlertDialog.Builder = AlertDialog.Builder(activity!!)
                            successAlertDialog.setMessage("Successfully synced!")
                            successAlertDialog.setCancelable(false)
                            successAlertDialog.setPositiveButton("Ok") { _: DialogInterface, _: Int ->

                            }

                            val successdialog: AlertDialog = successAlertDialog.create()

                            successdialog.show()
                        } finally {
                            this.realm.close()
                        }
                    } catch(e: Exception) {
                        dialog.dismiss()
                        Log.e(TAG, e.toString())
                    }
                }, {
                        error ->
                    error.message?.let {
                            error ->
                        Log.e(TAG, error.toString())
                    }
                }
            ) {
                override fun getHeaders(): MutableMap<String, String> {
                    val parameters: MutableMap<String, String> = HashMap<String, String>()
                    val sharedPref = activity!!.getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)

                    parameters["Authorization"] = "Token ${sharedPref.getString("token", "").toString()}"

                    return parameters
                }
            }

            request.retryPolicy = DefaultRetryPolicy(
                60000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT
            )

            queue.add(request)
        }.start()
    }
}