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
import com.example.mcpgoapp.Fragments.CustomerDetails
import com.example.mcpgoapp.Handlers.CustomerHandlers
import com.example.mcpgoapp.R

class CustomerRecycler(val context: Context, val childFragment: FragmentManager, val list: ArrayList<CustomerHandlers>):
        RecyclerView.Adapter<CustomerRecycler.ViewHolder>() {
    class ViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val view    = view.findViewById<Button>(R.id.view)
        val ivProfile = view.findViewById<ImageView>(R.id.ivProfile)
        val tvTitle   = view.findViewById<TextView>(R.id.tvTitle)
        val tvName    = view.findViewById<TextView>(R.id.tvName)
        val tvDay     = view.findViewById<TextView>(R.id.day)
    }

    private var dataList: ArrayList<CustomerHandlers> = this.list

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.list, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.ivProfile.setImageResource(R.drawable.customer)
        holder.tvTitle.text = "CUSTOMER"
        holder.tvName.text = this.dataList[position].name
        holder.tvDay.visibility = View.VISIBLE
        holder.tvDay.text = this.dataList[position].day

        holder.view.setOnClickListener {
            val fragment = CustomerDetails()

            val bundle = Bundle()
            bundle.putString("id", this.dataList[position].id)

            val fragmentManager     = childFragment
            val fragmentTransaction = fragmentManager.beginTransaction()

            fragment.arguments = bundle

            fragmentTransaction.replace(R.id.flFragment, fragment)
            fragmentTransaction.addToBackStack(null)
            fragmentTransaction.commit()
        }
    }

    override fun getItemCount(): Int {
        return this.dataList.size
    }

    fun filterList(dataFilter: ArrayList<CustomerHandlers>) {
        this.dataList = dataFilter
        notifyDataSetChanged()
    }
}