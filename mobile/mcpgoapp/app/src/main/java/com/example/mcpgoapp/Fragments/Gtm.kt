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
import androidx.core.widget.addTextChangedListener
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.mcpgoapp.Handlers.GtmHandlers
import com.example.mcpgoapp.Models.McpModel
import com.example.mcpgoapp.R
import com.example.mcpgoapp.Recyclers.GtmRecycler
import com.example.mcpgoapp.Utils.ModelController
import com.google.gson.Gson
import io.realm.Realm
import io.realm.RealmResults
import io.realm.kotlin.where
import org.json.JSONArray
import org.json.JSONObject
import java.util.*
import kotlin.collections.ArrayList

class Gtm: Fragment() {

    private lateinit var realm: Realm

    private lateinit var gtmHandler: ArrayList<GtmHandlers>
    private lateinit var gtmAdapter: GtmRecycler

    private lateinit var search: EditText
    private lateinit var recyclerview: RecyclerView

    override fun onCreateView(
            inflater: LayoutInflater, 
            container: ViewGroup?, 
            savedInstanceState: Bundle?): 
            View? {
        val root: View = LayoutInflater.from(activity!!).inflate(R.layout.gtm, container, false)
        this.run(root)
        return root
    }

    override fun onDestroy() {
        super.onDestroy()
        this.realm.close()
    }
    
    companion object {
        private const val TAG = "Gtm"
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
        val dataFilter: ArrayList<GtmHandlers> = ArrayList<GtmHandlers>()

        for (data in this.gtmHandler) {
            if (data.name.toLowerCase(Locale.ROOT).contains(queryString.toLowerCase(Locale.ROOT))) {
                dataFilter.add(data)
            }
        }

        this.gtmAdapter.filterList(dataFilter)
    }

    private fun pullData() {
        // NEED TO RUN THIS IN TO THREAD!
        try {
            this.realm = ModelController().modelInstance()

            val data: RealmResults<McpModel> = realm.where<McpModel>().distinct("gtm").findAllAsync()!!
            val dataJSON: String = Gson().toJson(realm.copyFromRealm(data))

            val jsonArray = JSONArray(dataJSON)

            this.gtmHandler = ArrayList<GtmHandlers>()

            for (i in 0 until jsonArray.length()) {
                val dataObject = jsonArray.getJSONObject(i)
                if (dataObject.getString("gtm") != "OTHERS") {
                    gtmHandler.add(GtmHandlers(dataObject.getString("gtm")))
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

        this.gtmAdapter = GtmRecycler(
                activity!!,
                activity!!.supportFragmentManager,
                this.gtmHandler
        )

        this.recyclerview.adapter = this.gtmAdapter
    }
}