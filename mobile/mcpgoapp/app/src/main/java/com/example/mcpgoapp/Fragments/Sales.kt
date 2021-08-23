package com.example.mcpgoapp.Fragments

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import androidx.core.widget.addTextChangedListener
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.mcpgoapp.Handlers.GtmHandlers
import com.example.mcpgoapp.Handlers.SalesHandlers
import com.example.mcpgoapp.Models.McpModel
import com.example.mcpgoapp.R
import com.example.mcpgoapp.Recyclers.GtmRecycler
import com.example.mcpgoapp.Recyclers.SalesRecycler
import com.example.mcpgoapp.Utils.ModelController
import com.google.gson.Gson
import io.realm.Realm
import io.realm.RealmResults
import io.realm.kotlin.where
import org.json.JSONArray
import org.json.JSONObject
import java.util.*
import kotlin.collections.ArrayList

class Sales: Fragment() {

    private lateinit var realm: Realm

    private lateinit var salesHandler: ArrayList<SalesHandlers>
    private lateinit var salesAdapter: SalesRecycler

    private lateinit var search: EditText
    private lateinit var recyclerview: RecyclerView

    private lateinit var person: TextView

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?):
            View? {
        val root: View = LayoutInflater.from(activity!!).inflate(R.layout.sales, container, false)
        this.run(root)
        return root
    }

    override fun onDestroy() {
        super.onDestroy()
        this.realm.close()
    }

    companion object {
        private const val TAG = "Sales"
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
        this.person       = v.findViewById(R.id.person)

        this.loadPerson()
    }

    private fun loadPerson() {
        val bundle = arguments

        this.person.text = bundle!!.getString("gtm", "")
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
        val dataFilter: ArrayList<SalesHandlers> = ArrayList<SalesHandlers>()

        for (data in this.salesHandler) {
            if (data.name.toLowerCase(Locale.ROOT).contains(queryString.toLowerCase(Locale.ROOT))) {
                dataFilter.add(data)
            }
        }

        this.salesAdapter.filterList(dataFilter)
    }

    private fun pullData() {
        // NEED TO RUN THIS IN TO THREAD!

        try {
            this.realm = ModelController().modelInstance()

            val bundle = arguments

            val data: RealmResults<McpModel> = realm.where<McpModel>()
                    .equalTo("gtm", bundle!!.getString("gtm"))
                    .distinct("salesperson")
                    .findAllAsync()!!
            val dataJSON: String = Gson().toJson(realm.copyFromRealm(data))

            val jsonArray = JSONArray(dataJSON)

            this.salesHandler = ArrayList<SalesHandlers>()

            for (i in 0 until jsonArray.length()) {
                val dataObject = jsonArray.getJSONObject(i)
                salesHandler.add(SalesHandlers(dataObject.getString("salesperson")))
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

        this.salesAdapter = SalesRecycler(
                activity!!, activity!!.supportFragmentManager, this.salesHandler
        )

        this.recyclerview.adapter = this.salesAdapter
    }
}