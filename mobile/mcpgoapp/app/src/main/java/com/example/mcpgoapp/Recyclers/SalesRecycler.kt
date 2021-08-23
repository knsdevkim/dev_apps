package com.example.mcpgoapp.Recyclers

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.RelativeLayout
import android.widget.TextView
import androidx.fragment.app.FragmentManager
import androidx.recyclerview.widget.RecyclerView
import com.example.mcpgoapp.Fragments.Customer
import com.example.mcpgoapp.Fragments.Sales
import com.example.mcpgoapp.Handlers.GtmHandlers
import com.example.mcpgoapp.Handlers.SalesHandlers
import com.example.mcpgoapp.R

class SalesRecycler(val context: Context, val childFragment: FragmentManager, val list: ArrayList<SalesHandlers>):
        RecyclerView.Adapter<SalesRecycler.ViewHolder>() {
    class ViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val view    = view.findViewById<Button>(R.id.view)
        val ivProfile = view.findViewById<ImageView>(R.id.ivProfile)
        val tvTitle   = view.findViewById<TextView>(R.id.tvTitle)
        val tvName    = view.findViewById<TextView>(R.id.tvName)
    }

    private var dataList: ArrayList<SalesHandlers> = this.list

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.list, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.ivProfile.setImageResource(R.drawable.sales)
        holder.tvTitle.text = "SALESPERSON"
        holder.tvName.text = this.dataList[position].name

        holder.view.setOnClickListener {
            val fragment = Customer()

            val fragmentManager     = childFragment
            val fragmentTransaction = fragmentManager.beginTransaction()

            val bundle = Bundle()

            bundle.putString("salesperson", holder.tvName.text.toString())

            fragment.arguments = bundle

            fragmentTransaction.replace(R.id.flFragment, fragment)
            fragmentTransaction.addToBackStack(null)
            fragmentTransaction.commit()
        }
    }

    override fun getItemCount(): Int {
        return this.dataList.size
    }

    fun filterList(dataFilter: ArrayList<SalesHandlers>) {
        this.dataList = dataFilter
        notifyDataSetChanged()
    }
}