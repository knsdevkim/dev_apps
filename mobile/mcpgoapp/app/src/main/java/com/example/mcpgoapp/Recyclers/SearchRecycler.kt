package com.example.mcpgoapp.Recyclers

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.fragment.app.FragmentManager
import androidx.recyclerview.widget.RecyclerView
import com.example.mcpgoapp.Fragments.CustomerDetails
import com.example.mcpgoapp.Fragments.Sales
import com.example.mcpgoapp.Handlers.GtmHandlers
import com.example.mcpgoapp.Handlers.SearchHandlers
import com.example.mcpgoapp.R
import java.util.*
import kotlin.collections.ArrayList

class SearchRecycler(val context: Context, val childFragment: FragmentManager, val list: ArrayList<SearchHandlers>):
        RecyclerView.Adapter<SearchRecycler.ViewHolder>() {
    class ViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val view         = view.findViewById<Button>(R.id.view)
        val ivProfile      = view.findViewById<ImageView>(R.id.ivProfile)
        val customername   = view.findViewById<TextView>(R.id.customername)
        val gtm            = view.findViewById<TextView>(R.id.gtm)
        val salesperson    = view.findViewById<TextView>(R.id.salesperson)
    }

    private var dataList: ArrayList<SearchHandlers> = this.list

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.search_list, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.ivProfile.setImageResource(R.drawable.gtm)
        holder.customername.text = this.dataList[position].customer
        holder.gtm.text = this.dataList[position].gtm
        holder.salesperson.text = this.dataList[position].salesperson

        holder.view.setOnClickListener {
            val fragment = CustomerDetails()

            val fragmentManager     = childFragment
            val fragmentTransaction = fragmentManager.beginTransaction()

            val bundle = Bundle()

            bundle.putString("id", this.dataList[position].id)

            fragment.arguments = bundle

            fragmentTransaction.replace(R.id.flFragment, fragment)
            fragmentTransaction.addToBackStack(null)
            fragmentTransaction.commit()
        }
    }

    override fun getItemCount(): Int {
        return this.dataList.size
    }

    fun filterList(dataFilter: ArrayList<SearchHandlers>) {
        this.dataList = dataFilter
        notifyDataSetChanged()
    }
}