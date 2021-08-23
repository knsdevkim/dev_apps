package com.example.mcpgoapp.Fragments

import android.content.Context
import com.example.mcpgoapp.Handlers.SearchHandlers
import com.example.mcpgoapp.Recyclers.SearchRecycler

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.EditText
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.mcpgoapp.Models.McpModel
import com.example.mcpgoapp.R
import com.example.mcpgoapp.Utils.ModelController
import com.google.gson.Gson
import io.realm.Realm
import io.realm.RealmResults
import io.realm.kotlin.where
import org.json.JSONArray
import java.util.*
import kotlin.collections.ArrayList

class Search: Fragment() {

    private lateinit var realm: Realm

    private lateinit var searchHandler: ArrayList<SearchHandlers>
    private lateinit var searchAdapter: SearchRecycler

    private lateinit var search: EditText
    private lateinit var recyclerview: RecyclerView

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?):
            View? {
        val root: View = LayoutInflater.from(activity!!).inflate(R.layout.search, container, false)
        this.run(root)
        return root
    }

    override fun onDestroy() {
        super.onDestroy()
        this.realm.close()
    }

    companion object {
        private const val TAG = "Search"
    }

    private fun run(v: View) {
        this.pullData()
        this.loadWidgets(v)
        this.pushDataToRecycler()
        this.search()
    }

    private fun loadWidgets(v: View) {
        this.search       = v.findViewById(R.id.search)
        this.recyclerview = v.findViewById(R.id.rv)
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
        val dataFilter: ArrayList<SearchHandlers> = ArrayList<SearchHandlers>()

        for (data in this.searchHandler) {
            when {
                data.customer.toLowerCase(Locale.ROOT).contains(queryString.toLowerCase(Locale.ROOT)) -> {
                    dataFilter.add(data)
                }
                data.gtm.toLowerCase(Locale.ROOT).contains(queryString.toLowerCase(Locale.ROOT)) -> {
                    dataFilter.add(data)
                }
                data.salesperson.toLowerCase(Locale.ROOT).contains(queryString.toLowerCase(Locale.ROOT)) -> {
                    dataFilter.add(data)
                }
            }
        }

        this.searchAdapter.filterList(dataFilter)
    }

    private fun pullData() {
        val sharedPref = activity!!.getSharedPreferences("mcpgoapp", Context.MODE_PRIVATE)

        // NEED TO RUN THIS IN TO THREAD!
        try {
            this.realm = ModelController().modelInstance()

            var data: RealmResults<McpModel>

            val user_type = sharedPref.getString("user_type", "")

            data = if (user_type != "" && user_type == "3") {
                realm.where<McpModel>()
                        .equalTo("salesperson", sharedPref.getString("fullname", ""))
                        .distinct("customer")
                        .findAllAsync()!!
            } else if (user_type != "" && user_type == "2") {
                realm.where<McpModel>()
                        .equalTo("gtm",  sharedPref.getString("fullname", ""))
                        .distinct("customer").findAllAsync()!!
            } else {
                realm.where<McpModel>().distinct("customer").findAllAsync()!!
            }

            val dataJSON: String = Gson().toJson(realm.copyFromRealm(data))

            val jsonArray = JSONArray(dataJSON)

            this.searchHandler = ArrayList<SearchHandlers>()

            for (i in 0 until jsonArray.length()) {
                val dataObject = jsonArray.getJSONObject(i)
                if (dataObject.getString("gtm") != "OTHERS") {
                    searchHandler.add(SearchHandlers(dataObject.getString("id"),
                            dataObject.getString("gtm"), 
                            dataObject.getString("salesperson"),
                            dataObject.getString("customer")))
                }
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

        this.searchAdapter = SearchRecycler(
                activity!!,
                activity!!.supportFragmentManager,
                this.searchHandler
        )

        this.recyclerview.adapter = this.searchAdapter
    }
}