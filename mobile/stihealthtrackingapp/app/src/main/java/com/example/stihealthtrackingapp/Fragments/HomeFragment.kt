package com.example.stihealthtrackingapp.Fragments

import android.content.Context
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.Spinner
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout
import com.android.volley.Request
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.example.stihealthtrackingapp.Adapters.AlertlistAdapter
import com.example.stihealthtrackingapp.DataHandlers.AlertlistHandler
import com.example.stihealthtrackingapp.R
import com.example.stihealthtrackingapp.Urls.Https
import org.json.JSONArray
import org.json.JSONObject
import java.util.*
import kotlin.collections.ArrayList

class HomeFragment: Fragment(), View.OnClickListener {

    private lateinit var mRvalertlist: RecyclerView
    private lateinit var mSrrefresh: SwipeRefreshLayout
    private lateinit var mSalert: Spinner
    private lateinit var mBtnalert: Button

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val fragmentView: View = inflater.inflate(R.layout.fragment_home, container, false)

        this.setupWidgets(fragmentView)

        this.fetchAPIData()

        return fragmentView
    }

    companion object {
        private const val TAG = "HomeFragment"
    }

    override fun onClick(view: View?) {
        when (view) {
            mBtnalert -> {
                try {
                    val queue = Volley.newRequestQueue(activity!!)

                    val request = object: StringRequest(
                        Method.POST,
                        "${Https().HTTPS_POSTALERT}",
                        { response ->
                            Log.i(TAG, response)

                            if (response == "done") {
                                Toast.makeText(
                                    activity!!,
                                    "Successfully submitted! Wait for the authority to respond.",
                                    Toast.LENGTH_LONG
                                ).show()
                            } else {
                                Toast.makeText(
                                    activity!!,
                                    "Unsuccessful request! Try again.",
                                    Toast.LENGTH_LONG
                                ).show()
                            }
                        }, { error ->
                            error.message?.let { message ->
                                Log.e(TAG, message)
                            }
                        }) {
                        override fun getParams(): MutableMap<String, String> {
                            val objects_param: MutableMap<String, String> = HashMap<String, String>()

                            val sharedPref = activity!!.getSharedPreferences("app", Context.MODE_PRIVATE)

                            with ( objects_param ) {
                                put("id", sharedPref.getString("id", "id").toString())
                                put("fullname", sharedPref.getString("fullname", "").toString())
                                put("address", sharedPref.getString("address", "").toString())
                                put("level", mSalert.selectedItem.toString().toLowerCase(Locale.ROOT))
                            }

                            return objects_param
                        }
                    }

                    queue.add(request)
                } catch(e: Exception) {
                    e.message?.let { message ->
                        Log.e(TAG, message)
                    }
                }
            }
        }
    }

    private fun setupWidgets(v: View) {
        mRvalertlist = v.findViewById(R.id.rvalertlist)
        mSrrefresh = v.findViewById(R.id.srRefresh)
        mSalert = v.findViewById(R.id.salerts)
        mBtnalert = v.findViewById(R.id.btnalert)

        this.initializeWidgets()
    }

    private fun initializeWidgets() {
        mBtnalert.setOnClickListener(this)

        mSrrefresh.setOnRefreshListener {
            fetchAPIData()
        }

        val alertList = arrayOf("Notify", "Guarded", "Elevated", "Danger", "Severe")

        val spinnerAdapter: ArrayAdapter<String> = ArrayAdapter<String>(
            requireActivity(),
            android.R.layout.simple_spinner_item, alertList)

        spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

        mSalert.adapter = spinnerAdapter
    }

    private fun fetchAPIData() {
        mSrrefresh.isRefreshing = true

        try {
            val queue = Volley.newRequestQueue(activity!!)

            val sharedPref = activity!!.getSharedPreferences("app", Context.MODE_PRIVATE)

            val request = StringRequest(
                Request.Method.GET,
                "${Https().HTTPS_GETUSERALERT}?id=${sharedPref.getString("id", "")}",
                { response ->
                    try {
                        val jsonObject = JSONObject(response)
                        val jsonArray: JSONArray = jsonObject.getJSONArray("data")

                        val list: ArrayList<AlertlistHandler> = ArrayList<AlertlistHandler>()

                        for (i in 0 until jsonArray.length()) {
                            val dataObject = jsonArray.getJSONObject(i)

                            list.add(
                                AlertlistHandler(
                                    dataObject.getString("id"),
                                    dataObject.getString("datetime"),
                                    dataObject.getString("level").toUpperCase(Locale.ROOT),
                                    dataObject.getString("status").toUpperCase(Locale.ROOT))
                            )
                        }

                        mRvalertlist.layoutManager = LinearLayoutManager(requireActivity())
                        mRvalertlist.hasFixedSize()

                        mRvalertlist.adapter = AlertlistAdapter(requireActivity(), list)

                        mSrrefresh.isRefreshing = false

                    } catch(e: Exception) {
                        mSrrefresh.isRefreshing = false

                        e.message?.let { message ->
                            Log.e(TAG, message)
                        }
                    }
                }, { error ->
                    mSrrefresh.isRefreshing = false

                    error.message?.let { message ->
                        Log.e(TAG, message)
                    }
                })

            queue.add(request)
        } catch(e: Exception) {
            mSrrefresh.isRefreshing = false
            e.message?.let { message ->
                Toast.makeText(activity!!, message, Toast.LENGTH_LONG).show()
            }
        }
    }
}