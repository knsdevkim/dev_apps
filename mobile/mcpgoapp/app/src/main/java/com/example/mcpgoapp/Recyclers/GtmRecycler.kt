package com.example.mcpgoapp.Recyclers

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.fragment.app.FragmentManager
import androidx.recyclerview.widget.RecyclerView
import com.example.mcpgoapp.Fragments.Sales
import com.example.mcpgoapp.Handlers.GtmHandlers
import com.example.mcpgoapp.R
import java.util.*
import kotlin.collections.ArrayList

class GtmRecycler(val context: Context, val childFragment: FragmentManager, val list: ArrayList<GtmHandlers>):
        RecyclerView.Adapter<GtmRecycler.ViewHolder>() {
    class ViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val layout    = view.findViewById<Button>(R.id.view)
        val ivProfile = view.findViewById<ImageView>(R.id.ivProfile)
        val tvTitle   = view.findViewById<TextView>(R.id.tvTitle)
        val tvName    = view.findViewById<TextView>(R.id.tvName)
    }

    private var dataList: ArrayList<GtmHandlers> = this.list

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.list, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.ivProfile.setImageResource(R.drawable.gtm)
        holder.tvTitle.text = "GTM"
        holder.tvName.text = this.dataList[position].name

        holder.layout.setOnClickListener {
            val fragment = Sales()

            val fragmentManager     = childFragment
            val fragmentTransaction = fragmentManager.beginTransaction()

            val bundle = Bundle()

            bundle.putString("gtm", holder.tvName.text.toString())

            fragment.arguments = bundle

            fragmentTransaction.replace(R.id.flFragment, fragment)
            fragmentTransaction.addToBackStack(null)
            fragmentTransaction.commit()
        }
    }

    override fun getItemCount(): Int {
        return this.dataList.size
    }

    fun filterList(dataFilter: ArrayList<GtmHandlers>) {
        this.dataList = dataFilter
        notifyDataSetChanged()
    }
}