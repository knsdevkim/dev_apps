package com.example.mcpgoapp.Fragments

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.cardview.widget.CardView
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.mcpgoapp.Handlers.CustomerHandlers
import com.example.mcpgoapp.Models.McpModel
import com.example.mcpgoapp.R
import com.example.mcpgoapp.Recyclers.CustomerRecycler
import com.example.mcpgoapp.Utils.ModelController
import com.google.gson.Gson
import io.realm.Realm
import io.realm.RealmResults
import io.realm.kotlin.where
import kotlinx.android.synthetic.main.list.view.*
import org.json.JSONArray
import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.Map

class Customer: Fragment(), View.OnClickListener {

    private lateinit var realm: Realm

    private lateinit var customerHandler: ArrayList<CustomerHandlers>
    private lateinit var customerAdapter: CustomerRecycler

    private lateinit var search: EditText
    private lateinit var recyclerview: RecyclerView

    private lateinit var day: Spinner

    private lateinit var person: TextView

    private lateinit var map: Button

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?):
            View? {
        val root: View = LayoutInflater.from(activity!!).inflate(R.layout.customer, container, false)
        this.run(root)
        return root
    }

    override fun onDestroy() {
        super.onDestroy()
        this.realm.close()
    }

    companion object {
        private const val TAG = "Customer"
    }

    private fun run(v: View) {
        this.pullData()
        this.loadWidgets(v)
        this.pushDataToRecycler()
        this.search()
        this.loadDays()
        this.functionSortDay()
    }

    private fun loadWidgets(v: View) {
        this.search       = v.findViewById(R.id.search)
        this.recyclerview = v.findViewById(R.id.rv)
        this.person       = v.findViewById(R.id.person)
        this.map          = v.findViewById(R.id.map)
        this.day          = v.findViewById(R.id.day)

        this.initializeClickListener()
        this.loadPerson()
    }

    private fun loadDays() {
        val days = arrayListOf("ALL", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")

        val arrayAdapter = ArrayAdapter(activity!!,
                android.R.layout.simple_spinner_item,
                days)

        arrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

        this.day.adapter = arrayAdapter
    }

    private fun functionSortDay() {
        this.day.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
                if ( parent!!.getItemAtPosition(position).toString() == "ALL" ) {
                    pullData()
                    pushDataToRecycler()
                }

                if ( parent.getItemAtPosition(position).toString() != "ALL" ) {
                    val dataFilter: ArrayList<CustomerHandlers> = ArrayList<CustomerHandlers>()

                    for ( data in customerHandler ) {
                        if ( data.day.toLowerCase(Locale.ROOT).contains(parent.getItemAtPosition(position).toString().toLowerCase(Locale.ROOT)) ) {
                            dataFilter.add(data)
                        }
                    }

                    customerAdapter.filterList(dataFilter)
                }
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {

            }
        }
    }

    private fun initializeClickListener() {
        this.map.setOnClickListener(this)
    }

    private fun loadPerson() {
        val bundle = arguments

        this.person.text = bundle!!.getString("salesperson", "")
    }

    private fun search() {
        this.search.addTextChangedListener(object: TextWatcher {
            override fun afterTextChanged(s: Editable?) {
                filter(s.toString())
            }

            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {

            }

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {

            }
        })
    }

    private fun filter(queryString: String) {
        val dataFilter: ArrayList<CustomerHandlers> = ArrayList<CustomerHandlers>()

        for (data in this.customerHandler) {
            if (data.name.toLowerCase(Locale.ROOT).contains(queryString.toLowerCase(Locale.ROOT))) {
                dataFilter.add(data)
            }
        }

        this.customerAdapter.filterList(dataFilter)
    }

    private fun pullData() {
        // NEED TO RUN THIS IN TO THREAD!
        try {
            this.realm = ModelController().modelInstance()

            val bundle = arguments

            val data: RealmResults<McpModel> = realm.where<McpModel>()
                    .equalTo("salesperson", bundle!!.getString("salesperson"))
                    .distinct("customer")
                    .findAllAsync()!!
            val dataJSON: String = Gson().toJson(realm.copyFromRealm(data))

            val jsonArray = JSONArray(dataJSON)

            this.customerHandler = ArrayList<CustomerHandlers>()

            for (i in 0 until jsonArray.length()) {
                val dataObject = jsonArray.getJSONObject(i)
                customerHandler.add(CustomerHandlers(
                        dataObject.getString("id"),
                        dataObject.getString("customer"),
                        dataObject.getString("day")))
            }
        } catch(e: Exception) {
            e.message?.let { message ->
                Log.e(TAG, message)
            }
        } finally {
            this.realm.close()
        }
    }

    private fun pushDataToRecycler() {
        this.recyclerview.layoutManager = LinearLayoutManager(activity!!)
        this.recyclerview.hasFixedSize()

        this.customerAdapter = CustomerRecycler(
                activity!!,
                activity!!.supportFragmentManager,
                this.customerHandler
        )

        this.recyclerview.adapter = this.customerAdapter
    }

    override fun onClick(v: View?) {
        val fragmentManager     = activity!!.supportFragmentManager
        val fragmentTransaction = fragmentManager.beginTransaction()

        when ( v ) {
            this.map -> {
                val fragment = Map()

                fragment.arguments = arguments

                fragmentTransaction.replace(R.id.flFragment, fragment)
                fragmentTransaction.addToBackStack(null)
                fragmentTransaction.commit()
            }
        }
    }
}